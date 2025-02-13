library(tidyverse)
library(dplyr)
library(stringr)
library(janitor)


# Set `_F4Carto` and `5FCarto` directories
dir_F4Carto <- "./F4Carto-raw-10"
dir_5FCarto <- "./5FCarto-raw"
dir_inputs <- "./inputs"
dir_output <- "./results_defaults"

# Find all subdirectories in dir_F4Carto
mapnames <- list.dirs(dir_F4Carto, full.names = FALSE, recursive = FALSE)

# Function to process each mapname
process_mapname <- function(mapname) {

	# Construct file paths
	file_F4Carto <- file.path(dir_F4Carto, mapname, "area_error.csv")
	nfo_csv_F4Carto <- file.path(dir_F4Carto, mapname, paste0(mapname, "_F4Carto.csv"))
	file_5FCarto <- file.path(dir_5FCarto, paste0(mapname, "_time_report.csv"))

	# Read and clean CSV files
	area_error_F4Carto <- read_csv(file_F4Carto) |> clean_names() |>
		# Get area error from second last row
		tail(2) |> head(1) |> pull(max_relative_area_error)

	metrics_F4Carto <- read_csv(nfo_csv_F4Carto) |>
		mutate(
			round = as.integer(round),
			time = as.numeric(str_remove(time, " Second"))
		) |>
		# Remove last two rows
		slice_head(n = -2) |>
		# Calculate cumulative time
		mutate(total_time = cumsum(time)) |>
		# Get last row
		tail(1)

	df_5FCarto <- read_csv(file_5FCarto) |> clean_names() |>
		mutate(time_at_n = cumsum(time_s))

	# Find first iteration where 5FCarto area error <= area error
	metrics_5FCarto_at_n <- df_5FCarto |>
		filter(max_area_error <= area_error_F4Carto) |>
		slice(1)

	metrics_5FCarto <- tail(df_5FCarto, 1)


	# Return a data frame row
	tibble(
		mapname = mapname,
		F4Carto_n_iter = metrics_F4Carto$round,
		`5FCarto_n_defeated` = metrics_5FCarto_at_n$integration_number,
		F4Carto_min_relative_area_error_reached = area_error_F4Carto,
		`5FCarto_max_relative_area_error_at_n` = metrics_5FCarto_at_n$max_area_error,
		F4Carto_time = metrics_F4Carto$total_time,
		`5FCarto_time_at_n` = metrics_5FCarto_at_n$time_at_n,
		`5FCarto_final_error` = metrics_5FCarto$max_area_error,
		`5FCarto_total_time` = metrics_5FCarto$time_at_n
	)
}

# Apply the function to each mapname and combine results
results <- map_dfr(mapnames, process_mapname)

# Write the results to csv file in dir_output
dir.create(dir_output, recursive = TRUE)
write_csv(results, file.path(dir_output, "time_and_area_error_comparison.csv"))
