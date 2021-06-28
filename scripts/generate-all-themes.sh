# Dark themes
#=============
python generate-theme-dark.py blue-270-30 270 30
python generate-theme-dark.py gold-90-210 90 210
python generate-theme-dark.py green-120-240 120 240
python generate-theme-dark.py green-150-270 150 270
python generate-theme-dark.py orange-60-300 60 300
python generate-theme-dark.py purple-300-60 300 60
python generate-theme-dark.py purple-320-80 320 80
python generate-theme-dark.py red-30-270 30 270
python generate-theme-dark.py teal-210-90 210 90

# Light themes
#==============
python generate-theme-light.py blue-270-30-light 270 30
python generate-theme-light.py gold-90-210-light 90 210
python generate-theme-light.py green-120-240-light 120 240
python generate-theme-light.py green-150-270-light 150 270
python generate-theme-light.py orange-60-300-light 60 300
python generate-theme-light.py purple-300-60-light 300 60
python generate-theme-light.py purple-320-80-light 320 80
python generate-theme-light.py red-30-270-light 30 270
python generate-theme-light.py teal-210-90-light 210 90

# Remove quotes around "true" in generated themes so it becomes a boolean instead of a string
sed -i 's/\"true\"/true/g' *color-theme.json
