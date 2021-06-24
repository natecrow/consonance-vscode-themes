from colormath.color_objects import LCHabColor, sRGBColor
from colormath.color_conversions import convert_color

from sys import argv
import json


def main():
    if (len(argv) > 3):
        name = str(argv[1])
        hue = int(argv[2])
        hue2 = int(argv[3]) # +/- 120 from primary hue - whichever looks better

        generateUniColorVsCodeTheme(name, hue, hue2)
    else:
        print('Expecting color theme name, primary LCH hue value, and secondary LCH hue value.')


def generateUniColorVsCodeTheme(name, hue, hue2):
    '''
    Generates VS Code color theme JSON file from given hues and name.
    Filename is generated automatically based on given name.
    '''
    colors = _generateThemeHexValues(hue, hue2)
    filename = name.lower().replace(' ', '-').replace('&', 'and') + '-color-theme.json'
    with open(filename, 'w') as f:
        json.dump(_generateJsonContent(name, colors), f, indent='\t')
    print('Generated color theme:', filename)


def _generateThemeHexValues(hue, hue2):
    '''
    Takes two Lch hue values from 0-360 and generates list of hex values for color theme.
    '''
    obs = '2'
    ill = 'd50'
    # TODO: handle RGB colors that aren't in LCH range, e.g. LCH(70, 50, 260)
    lch_colors = {
        # EDITOR
        # bgs
        'bg0':          LCHabColor(10, 0, 0, obs, ill),
        'bg1':          LCHabColor(15, 0, 0, obs, ill),
        'bg2':          LCHabColor(25, 0, 0, obs, ill),
        # fgs
        'fg0':          LCHabColor(40, 15, hue2, obs, ill),
        'fg1':          LCHabColor(60, 15, hue2, obs, ill),
        'fg2':          LCHabColor(80, 15, hue2, obs, ill),
        'fg3':          LCHabColor(90, 15, hue2, obs, ill),
        # color
        'color0':       LCHabColor(50, 20, hue, obs, ill),
        'color1':       LCHabColor(60, 50, hue, obs, ill),
        'color2':       LCHabColor(70, 20, hue, obs, ill),
        'color3':       LCHabColor(80, 50, hue, obs, ill),
        # red, green, blue, orange
        'red':          LCHabColor(60, 50, 25, obs, ill),
        'orange':       LCHabColor(60, 50, 55, obs, ill),
        'green':        LCHabColor(60, 50, 145, obs, ill),
        'blue':         LCHabColor(60, 50, 265, obs, ill),
        'darkRed':      LCHabColor(20, 20, 25, obs, ill),
        'darkOrange':   LCHabColor(20, 20, 55, obs, ill),
        'darkBlue':     LCHabColor(20, 20, 265, obs, ill),

        # UI / NON-EDITOR
        'bg1.5':                LCHabColor(20, 0, 0, obs, ill),
        'bg3':                  LCHabColor(30, 0, 0, obs, ill),
        'bg3.5':                LCHabColor(40, 0, 0, obs, ill),
        'focusBorder':          LCHabColor(40, 40, hue, obs, ill),
        'hoverBg':              LCHabColor(47, 40, hue, obs, ill),
        'btnBadgeBg':           LCHabColor(40, 25, hue, obs, ill),
        'btnBadgeHoverBg':      LCHabColor(47, 25, hue, obs, ill),
        'findMatchBg':          LCHabColor(35, 25, hue, obs, ill),
        'findMatchHlBg':        LCHabColor(25, 20, hue, obs, ill),
        'progressBarBg':        LCHabColor(45, 50, hue, obs, ill),
        'editorWordHlStrongBg': LCHabColor(60, 50, hue2, obs, ill),
        'black':                LCHabColor(0, 0, 0, obs, ill),

        # TERMINAL
        "term.foreground":          LCHabColor(75, 15, hue2, obs, ill),
        "term.background":          LCHabColor(10, 0, 0, obs, ill),
        "term.ansiBlack":           LCHabColor(0, 0, 0, obs, ill),
        "term.ansiBrightBlack":     LCHabColor(45, 15, hue2, obs, ill),
        "term.ansiBlue":            LCHabColor(45, 15, hue2, obs, ill),
        "term.ansiBrightBlue":      LCHabColor(45, 15, hue2, obs, ill),
        "term.ansiCyan":            LCHabColor(60, 20, hue, obs, ill),
        "term.ansiBrightCyan":      LCHabColor(60, 20, hue, obs, ill),
        "term.ansiGreen":           LCHabColor(60, 50, hue, obs, ill),
        "term.ansiBrightGreen":     LCHabColor(60, 50, hue, obs, ill),
        "term.ansiMagenta":         LCHabColor(45, 50, hue, obs, ill),
        "term.ansiBrightMagenta":   LCHabColor(45, 50, hue, obs, ill),
        "term.ansiRed":             LCHabColor(75, 20, hue, obs, ill),
        "term.ansiBrightRed":       LCHabColor(75, 20, hue, obs, ill),
        "term.ansiYellow":          LCHabColor(75, 50, hue, obs, ill),
        "term.ansiBrightYellow":    LCHabColor(75, 50, hue, obs, ill),
        "term.ansiWhite":           LCHabColor(90, 15, hue2, obs, ill),
        "term.ansiBrightWhite":     LCHabColor(90, 15, hue2, obs, ill)
    }

    rgb_colors = {}
    for key, value in lch_colors.items():
        rgb_r, rgb_g, rgb_b = convert_color(
            value, sRGBColor).get_upscaled_value_tuple()
        rgb_colors[key] = "#%02x%02x%02x" % (
            _clamp(rgb_r), _clamp(rgb_g), _clamp(rgb_b))

    return rgb_colors


def _clamp(x):
    return max(0, min(x, 255))


def _generateJsonContent(name, colors):
    '''
    Generates the JSON file for the color theme.
    Colors is the dict of hex values.
    '''
    return {
        'name': name,
        'colors': {
            'editor.background': colors['bg0'],
            'editor.foreground': colors['fg2'],
            'editor.lineHighlightBackground': colors['bg1'],
            'editor.selectionBackground': colors['bg2'],
            'editorCursor.foreground': colors['fg2'],
            'editorWhitespace.foreground': colors['fg0'],

            # base colors (used as defaults unless overwritten by more specific rule)
            "descriptionForeground": colors['fg2'] + 'b3',
            "errorForeground": colors['red'],
            "focusBorder": colors['focusBorder'] + 'cc',
            "foreground": colors['fg2'],
            "icon.foreground": colors['fg2'],
            "selection.background": colors['bg3.5'] + '80',

            # UI
            "activityBar.background": colors['bg2'],
            "activityBar.foreground": colors['fg3'],
            "activityBarBadge.background": colors['btnBadgeBg'],
            "activityBarBadge.foreground": colors['fg3'],
            "badge.background": colors['bg3'],
            "badge.foreground": colors['fg3'],
            "button.background": colors['btnBadgeBg'],
            "button.foreground": colors['fg3'],
            "button.hoverBackground": colors['btnBadgeHoverBg'],
            "debugToolBar.background": colors['bg1.5'],
            "diffEditor.insertedTextBackground": colors['green'] + '33',
            "diffEditor.removedTextBackground": "#ff000033",
            "dropdown.background": colors['bg1'],
            "dropdown.foreground": colors['fg3'],
            "editor.findMatchBackground": colors['findMatchBg'],
            "editor.findMatchBorder": colors['color1'],
            "editor.findMatchHighlightBackground": colors['findMatchHlBg'],
            "editor.findRangeHighlightBackground": colors['bg2'] + '66',
            "editor.hoverHighlightBackground": colors['bg3'] + '40',
            "editor.inactiveSelectionBackground": colors['bg2'] + 'a4',
            "editor.lineHighlightBorder": colors['bg1'],
            "editor.linkedEditingBackground": colors['color0'] + '4d',
            "editor.selectionHighlightBackground": colors['color2'] + '18',
            "editor.wordHighlightBackground": colors['color1'] + '30',
            "editor.wordHighlightStrongBackground": colors['editorWordHlStrongBg'] + '30',
            "editorBracketMatch.background": colors['bg3.5'] + '1a',
            "editorBracketMatch.border": colors['fg1'],
            "editorCodeLens.foreground": colors['fg2'],
            "editorError.foreground": colors['red'],
            "editorGroup.border": colors['fg0'],
            "editorGroup.dropBackground": colors['bg3'] + '80',
            "editorGroup.emptyBackground": colors['bg0'],
            "editorGroupHeader.noTabsBackground": colors['bg0'],
            "editorGroupHeader.tabsBackground": colors['bg1'],
            "editorGutter.addedBackground": colors['green'],
            "editorGutter.background": colors['bg0'],
            "editorGutter.deletedBackground": colors['red'],
            "editorGutter.modifiedBackground": colors['blue'],
            "editorHoverWidget.background": colors['bg1'],
            "editorHoverWidget.border": colors['bg0'],
            "editorIndentGuide.activeBackground": colors['bg3.5'],
            "editorIndentGuide.background": colors['bg2'],
            "editorInfo.foreground": colors['color3'],
            "editorLineNumber.activeForeground": colors['fg2'],
            "editorLineNumber.foreground": colors['fg0'],
            "editorLink.activeForeground": colors['color1'],
            "editorOverviewRuler.addedForeground": colors['green'] + '99',
            "editorOverviewRuler.border": colors['fg1'] + '4d',
            "editorOverviewRuler.commonContentForeground": colors['fg1'] + '66',
            "editorOverviewRuler.currentContentForeground": colors['fg2'] + '80',
            "editorOverviewRuler.deletedForeground": colors['red'] + '99',
            "editorOverviewRuler.errorForeground": colors['red'] + 'b3',
            "editorOverviewRuler.findMatchForeground": colors['orange'] + '7e',
            "editorOverviewRuler.incomingContentForeground": colors['blue'] + '80',
            "editorOverviewRuler.infoForeground": colors['blue'],
            "editorOverviewRuler.modifiedForeground": colors['blue'] + '99',
            "editorOverviewRuler.rangeHighlightForeground": colors['blue'] + '99',
            "editorOverviewRuler.selectionHighlightForeground": colors['fg1'] + 'cc',
            "editorOverviewRuler.warningForeground": colors['orange'],
            "editorOverviewRuler.wordHighlightForeground": colors['fg1'] + 'cc',
            "editorOverviewRuler.wordHighlightStrongForeground": colors['fg2'] + 'cc',
            "editorRuler.foreground": colors['fg0'],
            "editorSuggestWidget.background": colors['bg1'],
            "editorSuggestWidget.border": colors['bg0'],
            "editorSuggestWidget.foreground": colors['fg3'],
            "editorSuggestWidget.highlightForeground": colors['color1'],
            "editorSuggestWidget.selectedBackground": colors['bg1.5'],
            "editorUnnecessaryCode.opacity": colors['black'] + 'c0',
            "editorWarning.foreground": colors['orange'],
            "editorWidget.background": colors['bg1'],
            "editorWidget.border": colors['bg3'],
            "extensionButton.prominentBackground": colors['focusBorder'],
            "extensionButton.prominentHoverBackground": colors['hoverBg'],
            "gitDecoration.conflictingResourceForeground": colors['blue'],
            "gitDecoration.deletedResourceForeground": colors['red'],
            "gitDecoration.ignoredResourceForeground": colors['fg1'],
            "gitDecoration.modifiedResourceForeground": colors['orange'],
            "gitDecoration.untrackedResourceForeground": colors['green'],
            "input.background": colors['bg0'],
            "input.foreground": colors['fg2'],
            "input.placeholderForeground": colors['fg1'],
            "inputOption.activeBorder": colors['color1'] + '00',
            "inputValidation.errorBackground": colors['darkRed'],
            "inputValidation.errorBorder": colors['red'],
            "inputValidation.infoBackground": colors['darkBlue'],
            "inputValidation.infoBorder": colors['blue'],
            "inputValidation.warningBackground": colors['darkOrange'],
            "inputValidation.warningBorder": colors['orange'],
            "list.activeSelectionBackground": colors['bg1.5'],
            "list.activeSelectionForeground": colors['fg3'],
            "list.dropBackground": colors['bg2'],
            "list.focusBackground": colors['bg2'],
            "list.highlightForeground": colors['fg3'],
            "list.hoverBackground": colors['bg1.5'],
            "list.inactiveSelectionBackground": colors['bg1.5'],
            "list.inactiveSelectionForeground": colors['fg3'],
            "merge.currentContentBackground": colors['green'] + '33',
            "merge.currentHeaderBackground": colors['green'] + '80',
            "merge.incomingContentBackground": colors['blue'] + '33',
            "merge.incomingHeaderBackground": colors['blue'] + '80',
            "notifications.background": colors['bg1'],
            "panel.border": colors['fg1'] + '59',
            "panelTitle.activeForeground": colors['fg3'],
            "peekView.border": colors['color1'],
            "peekViewEditor.background": colors['bg1'] + '66',
            "peekViewEditor.matchHighlightBackground": colors['findMatchHlBg'],
            "peekViewEditorGutter.background": colors['bg1'] + '66',
            "peekViewResult.background": colors['bg1'],
            "peekViewResult.fileForeground": colors['fg3'],
            "peekViewResult.matchHighlightBackground": colors['findMatchHlBg'],
            "peekViewResult.selectionBackground": colors['color1'] + '33',
            "peekViewResult.selectionForeground": colors['fg3'],
            "peekViewTitle.background": colors['bg1'] + '66',
            "peekViewTitleDescription.foreground": colors['fg2'] + 'b3',
            "peekViewTitleLabel.foreground": colors['fg3'],
            "progressBar.background": colors['progressBarBg'],
            "scrollbar.shadow": colors['black'],
            "scrollbarSlider.activeBackground": colors['fg1'] + '80',
            "scrollbarSlider.background": colors['bg3'] + '80',
            "scrollbarSlider.hoverBackground": colors['bg3.5'] + '80',
            "sideBar.background": colors['bg1'],
            "sideBarSectionHeader.background": colors['bg1.5'],
            "sideBarTitle.foreground": colors['fg2'],
            "statusBar.background": colors['bg2'],
            "statusBar.debuggingBackground": colors['bg2'],
            "statusBar.debuggingForeground": colors['fg3'],
            "statusBar.foreground": colors['fg2'],
            "statusBar.noFolderBackground": colors['bg2'],
            "statusBarItem.hoverBackground": colors['bg3'],
            "tab.activeBackground": colors['bg0'],
            "tab.activeForeground": colors['fg3'],
            "tab.border": colors['bg0'],
            "tab.inactiveBackground": colors['bg1.5'],
            "tab.inactiveForeground": colors['fg3'] + '80',
            "tab.unfocusedActiveForeground": colors['fg3'] + '80',
            "tab.unfocusedInactiveForeground": colors['fg3'] + '40',
            "textLink.activeForeground": colors['color1'],
            "textLink.foreground": colors['color1'],
            "titleBar.activeBackground": colors['bg3'],
            "titleBar.activeForeground": colors['fg3'],
            "titleBar.inactiveBackground": colors['bg3'],
            "titleBar.inactiveForeground": colors['fg2'],
            "widget.shadow": colors['black'] + '5c',

            # TERMINAL
            "terminal.foreground":          colors['term.foreground'],
            "terminal.background":          colors['term.background'],
            "terminal.ansiBlack":           colors['term.ansiBlack'],
            "terminal.ansiBrightBlack":     colors['term.ansiBrightBlack'],
            "terminal.ansiBlue":            colors['term.ansiBlue'],
            "terminal.ansiBrightBlue":      colors['term.ansiBrightBlue'],
            "terminal.ansiCyan":            colors['term.ansiCyan'],
            "terminal.ansiBrightCyan":      colors['term.ansiBrightCyan'],
            "terminal.ansiGreen":           colors['term.ansiGreen'],
            "terminal.ansiBrightGreen":     colors['term.ansiBrightGreen'],
            "terminal.ansiMagenta":         colors['term.ansiMagenta'],
            "terminal.ansiBrightMagenta":   colors['term.ansiBrightMagenta'],
            "terminal.ansiRed":             colors['term.ansiRed'],
            "terminal.ansiBrightRed":       colors['term.ansiBrightRed'],
            "terminal.ansiYellow":          colors['term.ansiYellow'],
            "terminal.ansiBrightYellow":    colors['term.ansiBrightYellow'],
            "terminal.ansiWhite":           colors['term.ansiWhite'],
            "terminal.ansiBrightWhite":     colors['term.ansiBrightWhite'],
        },
        'tokenColors': [
            {
                'name': 'Keyword, storage, tag',
                'scope': [
                    'keyword',
                    'storage',
                    'entity.name.tag',
                ],
                'settings': {
                    'foreground': colors['fg1']
                }
            },
            {
                'name': 'HTML tag',
                'scope': [
                    'entity.name.tag.html'
                ],
                'settings': {
                    'foreground': colors['color3']
                }
            },
            {
                'name': 'CSS Tag',
                'scope': [
                    'entity.name.tag.css'
                ],
                'settings': {
                    'foreground': colors['color1']
                }
            },
            {
                'name': 'Storage type, attribute',
                'scope': [
                    'storage.type',
                    'entity.other.attribute-name'
                ],
                'settings': {
                    'foreground': colors['fg1'],
                    'fontStyle': 'italic'
                }
            },
            {
                'name': 'Entity',
                'scope': [
                    'entity.name',
                    'entity.other.inherited-class',
                ],
                'settings': {
                    'foreground': colors['fg2']
                }
            },
            {
                'name': 'Library entity',
                'scope': 'support',
                'settings': {
                    'foreground': colors['fg2'],
                    'fontStyle': 'italic'
                }
            },
            {
                'name': 'Variable',
                'scope': [
                    'variable',
                    'variable.language',
                    'variable.parameter'
                ],
                'settings': {
                    'foreground': colors['color2']
                }
            },
            {
                'name': 'Library variable',
                'scope': [
                    'support.variable',
                    'support.other.variable'
                ],
                'settings': {
                    'foreground': colors['color2']
                }
            },
            {
                'name': 'Constant',
                'scope': [
                    'constant',
                    'constant.numeric',
                    'constant.language',
                    'constant.character.escape',
                    'constant.other',
                    'keyword.other.unit.px.css'
                ],
                'settings': {
                    'foreground': colors['color3']
                }
            },
            {
                'name': 'Library constant',
                'scope': 'support.constant',
                'settings': {
                    'foreground': colors['color3'],
                    'fontStyle': ''
                }
            },
            {
                'name': 'String',
                'scope': 'string',
                'settings': {
                    'foreground': colors['color1']
                }
            },
            {
                'name': 'Comment',
                'scope': 'comment',
                'settings': {
                    'foreground': colors['color0'],
                    'fontStyle': 'italic'
                }
            },
            {
                'name': 'Diff delete',
                'scope': 'markup.deleted',
                'settings': {
                    'foreground': colors['red']
                }
            },
            {
                'name': 'Diff insert',
                'scope': 'markup.inserted',
                'settings': {
                    'foreground': colors['green']
                }
            },
            {
                'name': 'Diff change',
                'scope': 'markup.changed',
                'settings': {
                    'foreground': colors['blue']
                }
            },
            {
                'name': 'Markup heading',
                'scope': [
                    'markup.heading',
                    'entity.name.section'
                ],
                'settings': {
                    'foreground': colors['color3']
                }
            },
            {
                'name': 'Markup styling',
                'scope': [
                    'markup.bold',
                    'markup.italic',
                    'markup.underline'
                ],
                'settings': {
                    'foreground': colors['color1']
                }
            },
            {
                'name': 'Markup quote',
                'scope': [
                    'markup.quote',
                    'markup.raw.inline',
                    'markup.raw.block'
                ],
                'settings': {
                    'foreground': colors['color0']
                }
            },
            {
                "name": "Invalid",
                "scope": "invalid",
                "settings": {
                    "foreground": colors['red']
                }
            }
        ],
        "semanticHighlighting": "true",
        "semanticTokenColors": {
            "method.declaration": {
                "foreground": colors['fg3'],
                "bold": "true"
            },
            "function.declaration": {
                "foreground": colors['fg3'],
                "bold": "true"
            }
        }
    }


if __name__ == '__main__':
    main()
