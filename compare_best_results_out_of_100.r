library(tidyverse)
library(dplyr)
library(stringr)
library(janitor)

# Set `_F4Carto`, `5FCarto`, and `flow-based` directories
dir_F4Carto <- "./F4carto-raw-100"
dir_5FCarto <- "./5FCarto-raw-100"
dir_flow_based <- "./flow-based-raw-100"
# dir_flow_based <- "./5FCarto-raw-100"

# Find all subdirectories in dir_F4Carto
mapnames <- list.dirs(dir_F4Carto, full.names = FALSE, recursive = FALSE)

# Function to process each mapname
process_mapname <- function(mapname) {
	# Construct file paths
	file_F4Carto <- file.path(dir_F4Carto, mapname, "area_error.csv")
	file_5FCarto <- file.path(dir_5FCarto, paste0(mapname, "_time_report.csv"))
	file_flow_based <- file.path(dir_flow_based, paste0(mapname, "_time_report.csv"))

	# Read and clean CSV files
	df_F4Carto <- read_csv(file_F4Carto) |> clean_names()
	df_5FCarto <- read_csv(file_5FCarto) |> clean_names()
	df_flow_based <- read_csv(file_flow_based) |> clean_names()

	# Extract required metrics
	metrics_F4Carto <- df_F4Carto |>
		summarise(
			min_error = min(max_relative_area_error, na.rm = TRUE),
			min_error_row = which.min(max_relative_area_error) - 1
		)

	metrics_F5Carto <- df_5FCarto |>
		slice(which.min(max_area_error))

	metrics_flow_based <- df_flow_based |>
		slice(which.min(max_area_error))

	# Return a data frame row
	tibble(
		mapname = mapname,
		F4Carto_min_relative_area_error_reached = metrics_F4Carto$min_error,
		F4Carto_n_iter = metrics_F4Carto$min_error_row,
		`5FCarto_min_relative_area_error_reached` = metrics_F5Carto$max_area_error,
		`5FCarto_n_iter` = metrics_F5Carto$integration_number,
		flow_based_min_relative_area_error_reached = metrics_flow_based$max_area_error,
		flow_based_n_iter = metrics_flow_based$integration_number
	)
}

# Apply the function to each mapname and combine results
results <- map_dfr(mapnames, process_mapname)

# Write the results to a CSV file
write_csv(results, "results_best_out_of_100.csv")
