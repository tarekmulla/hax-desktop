echo "\n\nBundles the application and all its dependencies into a single package (.app)"
pyinstaller --noconfirm --windowed --name="HaX" \
            --icon="haxdesktop/images/icon.png" \
            --add-data="haxdesktop/assets:assets" \
            haxdesktop/main.py

echo "\n\nCreate a release folder"
mkdir -p release/macos
rm -rf release/macos/*

echo "\n\nCopy the app bundle to the release folder"
cp -r "dist/HaX.app" release/macos

echo "If the dmg already exists, delete it"
test -f "release/HaX.dmg" && rm "release/HaX.dmg"

echo "\n\nCreating the new release:"
create-dmg \
  --volname "HaX" \
  --volicon "haxdesktop/images/icon.png" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "HaX.app" 175 120 \
  --hide-extension "HaX.app" \
  --app-drop-link 425 120 \
  "release/HaX.dmg" \
  "release/macos/"

echo "\n\nCleanup temp files"
rm -rf dist
rm -rf build
rm -rf release/macos
rm hax.spec

echo "\n\nMacOS Release package (dmg) created successfully"
