import plistlib
import yaml
import sys
import os

def build_shortcut(yaml_path, output_path):
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    
    # Basic conversion logic (to be expanded)
    # iOS .shortcut files are binary plists.
    with open(output_path, 'wb') as f:
        plistlib.dump(data, f, fmt=plistlib.FMT_BINARY)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python builder.py <yaml_path> <output_path>")
        sys.exit(1)
    build_shortcut(sys.argv[1], sys.argv[2])
