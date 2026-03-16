def write_results(result_df, grouped_df, output_path_filtered, output_path_grouped):

    result_df.coalesce(1).write \
        .mode("overwrite") \
        .option("header", True) \
        .csv(output_path_filtered)

    grouped_df.coalesce(1).write \
        .mode("overwrite") \
        .option("header", True) \
        .csv(output_path_grouped)