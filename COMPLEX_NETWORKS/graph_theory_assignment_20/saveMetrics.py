# To save metrics as text file
def save_metrics_as_file(summary_metrics, output_file):
    with open(output_file, 'w') as f:
        for key, value in summary_metrics.items():
            if isinstance(value, (list, tuple)):
                value_str = ', '.join(map(str, value))
                f.write(f"{key}: {value_str}\n")
            else:
                f.write(f"{key}: {value}\n")