import sys
from pathlib import Path


def build_command_map(plugin_dir):
	command_map = {}
	plugin_dir_path = Path(plugin_dir)
	for plugin in plugin_dir_path.iterdir():
		# skip __init__ and __pycache__
		if "__" in str(plugin):
			continue

		plugin_loc_fixed = str(plugin).replace("/", ".")

		if plugin_loc_fixed not in sys.modules:
			__import__(plugin_loc_fixed)

		plugin_module = sys.modules[plugin_loc_fixed]
		plugin_name, entrance_function = plugin_module.register()
		command_map[plugin_name] = entrance_function

	return command_map


def main():
	if len(sys.argv) == 1:
		print("need an argument")
		return
	
	command_map = build_command_map("plugins")

	if sys.argv[1] not in command_map.keys():
		print(f"unrecognized command: {sys.argv[1]}")
		return

	ret = command_map[sys.argv[1]](sys.argv[2:])
	print(f"{ret=}")


if __name__ == "__main__":
	main()
