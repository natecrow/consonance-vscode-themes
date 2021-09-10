# Dark themes
#=============
# python generate-theme-dark.py blue 270 30
# python generate-theme-dark.py cyan 225 105
# python generate-theme-dark.py gold 90 210
# python generate-theme-dark.py green 135 255
# python generate-theme-dark.py orange 45 285
# python generate-theme-dark.py purple 315 75
# python generate-theme-dark.py teal 180 300

# Light themes
#==============
python generate-theme-light.py blue 270 30
python generate-theme-light.py cyan 225 105
python generate-theme-light.py gold 90 210
python generate-theme-light.py green 135 255
python generate-theme-light.py orange 45 285
python generate-theme-light.py purple 315 75
python generate-theme-light.py teal 180 300

# Remove quotes around "true" in generated themes so it becomes a boolean instead of a string
sed -i 's/\"true\"/true/g' *color-theme.json
