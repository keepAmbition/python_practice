import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    from modules.actions import execute_from_command_line
    execute_from_command_line(sys.argv)