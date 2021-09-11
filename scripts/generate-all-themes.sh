# Dark themes
#=============
python generate-theme-dark.py blue 270 30
python generate-theme-dark.py gold 90 210
python generate-theme-dark.py green 140 260
python generate-theme-dark.py orange 55 295
python generate-theme-dark.py purple 315 75
python generate-theme-dark.py teal 205 85

# Remove quotes around "true" in generated themes so it becomes a boolean instead of a string
sed -i 's/\"true\"/true/g' *color-theme.json
