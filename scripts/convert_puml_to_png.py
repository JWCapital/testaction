import os
import subprocess

def convert_puml_to_png(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Find all PUML files in the input directory
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".puml"):
                puml_file = os.path.join(root, file)
                # Create the output PNG file path
                name = os.path.splitext(file)[0]
                png_file = os.path.join(output_dir, f"{name}.png")
                print(f"Rendering | File: {puml_file} | Output: {png_file}")
                # Execute the PlantUML command to render the PUML file to PNG
                subprocess.run(["plantuml", "-tpng", f"-o{output_dir}", puml_file], check=True)

def main():
    input_dir = os.getenv('INPUT_DIR', './docs/diagrams')
    output_dir = os.getenv('OUTPUT_DIR', './docs/images')
    convert_puml_to_png(input_dir, output_dir)

if __name__ == "__main__":
    main()
