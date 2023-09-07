# Function to save analysis results to a text file
def save_analyzed_results_as_file(analysis_results, output_file):
    with open(output_file, 'a') as f:
        f.write("\nAnalysis Results :\n")
        for key, value in analysis_results.items():
            if isinstance(value, (list, tuple)):
                value_str = ', '.join(map(str, value))
                f.write(f"{key}: {value_str}\n")
            else:
                f.write(f"{key}: {value}\n")