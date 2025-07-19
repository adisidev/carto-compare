library(tidyverse)

qlcf <- read_csv("/Users/adi/github/carto-compare/5FC-JUL19-QLCF-5_to_15/final_results.csv.csv")

# rename 'mean' column to 'avg'
qlcf <- qlcf |>
  rename(avg = mean)

qlcf |>
	group_by(parameter_qlcf) |>
	summarise(
		mean = mean(avg, na.rm = TRUE),
		min = min(avg, na.rm = TRUE),
		max = max(avg, na.rm = TRUE),
		median = median(avg, na.rm = TRUE),
		std = sd(avg, na.rm = TRUE),
		sum = sum(avg, na.rm = TRUE)
	) |>
	# sort by mean (increasing)
	arrange(mean) |>
	write_csv("19JUL-qlcf_summary-minus.csv")




