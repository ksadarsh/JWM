#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# License: GPLv2
#
# Copyright (C) 2016 Ovidiu M <mrovi9000@gmail.com>
# Modified by Johan Malm <jgm323@gmail.com>
#

# Python 3 compatibility
from __future__ import print_function
from codecs import open

import argparse
import gettext
import locale
import os
import sys


icon_size = 24
icon_theme_name = ""
strings = {
  "Back": "Back",
  "Back[am]": "ወደ ኋላ",
  "Back[ar]": "إلى الخلف",
  "Back[ast]": "Atrás",
  "Back[be]": "Назад",
  "Back[bg]": "Назад",
  "Back[bn]": "পূর্ববর্তী",
  "Back[ca]": "Endarrere",
  "Back[cs]": "Zpět",
  "Back[da]": "Tilbage",
  "Back[de]": "_Zurück",
  "Back[el]": "Πίσω",
  "Back[eo]": "Malantaŭen",
  "Back[es]": "Atrás",
  "Back[et]": "Tagasi",
  "Back[eu]": "Atzera",
  "Back[fa_IR]": "بازگشت",
  "Back[fi]": "Edellinen",
  "Back[fr]": "Précédent",
  "Back[gl]": "Recuar",
  "Back[he]": "אחורה",
  "Back[hr]": "Natrag",
  "Back[hu]": "Vissza",
  "Back[id]": "Kembali",
  "Back[is]": "Til baka",
  "Back[it]": "Indietro",
  "Back[ja]": "戻る",
  "Back[kk]": "Артқа",
  "Back[ko]": "뒤로",
  "Back[lt]": "Atgal",
  "Back[lv]": "Atpakaļ",
  "Back[ms]": "Undur",
  "Back[nb]": "Tilbake",
  "Back[nl]": "Terug",
  "Back[nn]": "Tilbake",
  "Back[oc]": "Precedent",
  "Back[pa]": "ਪਿੱਛੇ",
  "Back[pl]": "Wstecz",
  "Back[pt_BR]": "Voltar",
  "Back[pt]": "Recuar",
  "Back[ro]": "Înapoi",
  "Back[ru]": "Назад",
  "Back[sk]": "Späť",
  "Back[sq]": "Prapa",
  "Back[sr]": "Назад",
  "Back[sv]": "Bakåt",
  "Back[te]": "వెనుకకు",
  "Back[th]": "ถอยกลับ",
  "Back[tr]": "Geri",
  "Back[ug]": "ئارقىسىغا",
  "Back[uk]": "Назад",
  "Back[ur_PK]": "پیچھے",
  "Back[ur]": "پیچھے",
  "Back[vi]": "Quay lui",
  "Back[zh_CN]": "后退",
  "Back[zh_HK]": "往前",
  "Back[zh_TW]": "往前",
  "Other": "Other",
  "Other[af]": "Ander",
  "Other[ar]": "أخرى",
  "Other[as]": "অন্যান্য",
  "Other[ast]": "Otres",
  "Other[be]": "Іншыя",
  "Other[be@latin]": "Inšyja",
  "Other[bg]": "Други",
  "Other[bn]": "অন্যান্য",
  "Other[bn_IN]": "অন্যান্য",
  "Other[br]": "All",
  "Other[ca]": "Altres",
  "Other[cs]": "Ostatní",
  "Other[cy]": "Eraill",
  "Other[da]": "Andre",
  "Other[de]": "Sonstige",
  "Other[dz]": "གཞན།",
  "Other[el]": "Άλλα",
  "Other[en_CA]": "Other",
  "Other[en_GB]": "Other",
  "Other[eo]": "Alia",
  "Other[es]": "Otras",
  "Other[es_VE]": "Otras",
  "Other[et]": "Muu",
  "Other[eu]": "Bestelakoak",
  "Other[fa]": "غیره",
  "Other[fi]": "Muut",
  "Other[fr]": "Autre",
  "Other[frp]": "Autres",
  "Other[fur]": "Altri",
  "Other[ga]": "Eile",
  "Other[gl]": "Outros",
  "Other[gn]": "Amboae",
  "Other[gu]": "અન્ય",
  "Other[he]": "אחר",
  "Other[hi]": "अन्य",
  "Other[hr]": "Ostalo",
  "Other[hu]": "Egyéb",
  "Other[hy]": "Այլ",
  "Other[id]": "Lainnya",
  "Other[io]": "Altra",
  "Other[is]": "Aðrir",
  "Other[it]": "Altro",
  "Other[ja]": "その他",
  "Other[ka]": "სხვა",
  "Other[kk]": "Басқалар",
  "Other[ko]": "기타",
  "Other[ku]": "Yên din",
  "Other[ky]": "Башкалар",
  "Other[lt]": "Kitos",
  "Other[lv]": "Citas programmas",
  "Other[mai]": "आन",
  "Other[mg]": "Hafa",
  "Other[mk]": "Други",
  "Other[ml]": "മറ്റുളളവ",
  "Other[mn]": "Бусад",
  "Other[mr]": "अन्य",
  "Other[ms]": "Lain-lain",
  "Other[nb]": "Annet",
  "Other[ne]": "अन्य",
  "Other[nl]": "Overig",
  "Other[nn]": "Andre",
  "Other[oc]": "Autre",
  "Other[or]": "ଅନ୍ଯାନ୍ଯ",
  "Other[pa]": "ਹੋਰ",
  "Other[pl]": "Inne",
  "Other[ps]": "نور",
  "Other[pt]": "Outras",
  "Other[pt_BR]": "Outros",
  "Other[ro]": "Altele",
  "Other[ru]": "Прочие",
  "Other[rw]": "Ikindi",
  "Other[si]": "වෙනත්",
  "Other[sk]": "Ostatné",
  "Other[sl]": "Drugo",
  "Other[sq]": "Tjetër",
  "Other[sr]": "Остало",
  "Other[sr@latin]": "Ostalo",
  "Other[sv]": "Övriga",
  "Other[ta]": "மற்றவை",
  "Other[te]": "ఇతర",
  "Other[th]": "อื่นๆ",
  "Other[tr]": "Diğer",
  "Other[ug]": "باشقىلار",
  "Other[uk]": "Інші",
  "Other[ur]": "دیگر",
  "Other[ur_PK]": "دیگر",
  "Other[uz@cyrillic]": "Бошқа",
  "Other[vi]": "Khác",
  "Other[xh]": "Ezinye",
  "Other[zh_CN]": "其它",
  "Other[zh_HK]": "其它",
  "Other[zh_TW]": "其它"
}


# Computes a list of the current locale names, in most specific to least specific order.
# The empty string is always the last element.
def get_current_locale_names():
  # E.g. "en_US"
  lang = locale.getlocale()[0] or "en_US"
  # ["en", "US"]
  lang_parts = lang.split("_")
  locale_names = [""]
  for i in range(len(lang_parts)):
    locale_names.append("_".join(lang_parts[:i+1]))
  # ["en_US", "en", ""]
  locale_names = list(reversed(locale_names))
  return locale_names


def which(cmd):
  try:
    for path in os.environ["PATH"].split(os.pathsep):
      full = os.path.join(path, cmd)
      if os.path.isfile(full) and os.access(full, os.X_OK):
        return full
  except:
    pass
  return None


def internationalized(entry):
  # Now entry is a dict of tag -> value, with tag like "Name", "Name[en]", "Name[en_US]"
  # We modify it so that the value of "Name" is replaced with the value of the most specific tag
  # that matches the current locale.
  # We create a two-level tree:
  # tag => name, suffix => value
  # Where name is the tag name (e.g. "Name") and suffix is the tag's locale (e.g. "en_US" or "").
  tree = {}
  for tag in entry:
    if "[" in tag:
      name, suffix = tag.replace("]", "").split("[", 1)
    else:
      name = tag
      suffix = ""
    if name not in tree:
      tree[name] = {}
    tree[name][suffix] = entry[tag]
  # Collapse into a tag => value dict, using the most specific matching suffix.
  # Keep the old names in keys with the value "_pmenu_raw_" + tag
  locale_names = get_current_locale_names()
  entry = {}
  for name in tree:
    if "" in tree[name]:
      entry["_pmenu_raw_" + name] = tree[name][""]
    for suffix in locale_names:
      if suffix in tree[name]:
        entry[name] = tree[name][suffix]
        if not suffix and entry[name]:
          entry[name] = _(entry[name])
        break
  return entry


# Reference: http://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-1.1.html
# Loads a Desktop Entry file into a dictionary key -> value
# A special key "_path" stores the path of the file
def read_desktop_entry(path):
  entry = {}
  with open(path, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
    inside = False
    for line in lines:
      if line.startswith("["):
        inside = line == "[Desktop Entry]"
        continue
      if inside:
        if "=" in line:
          k, v = line.split("=", 1)
          entry[k] = v
  entry["_path"] = path
  return internationalized(entry)


# Reference: http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html
# Reference: http://standards.freedesktop.org/basedir-spec/basedir-spec-0.8.html
def get_setting_locations():
  locations = ["/usr/share", "/usr/local/share", os.path.expanduser("~/.local/share")]
  if "XDG_DATA_DIRS" in os.environ:
    dirs = os.environ["XDG_DATA_DIRS"]
    if dirs:
      dirs = dirs.split(":")
      for d in dirs:
        while d.endswith("/"):
          d = d[:-1]
        if d not in locations:
          locations.append(d)
  return locations


# Loads all Desktop Entry files with type "Directory" into a dictionary name -> entry
# Reference: http://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-1.1.html
def load_categories():
  categories = {}
  for d in get_setting_locations():
    d = d + "/desktop-directories/"
    for (dirpath, dirnames, filenames) in os.walk(d):
      for filename in filenames:
        entry = read_desktop_entry(os.path.join(dirpath, filename))
        if "_pmenu_raw_Name" in entry and "Type" in entry and entry["Type"] == "Directory":
          categories[normalize_category(entry["_pmenu_raw_Name"])[-1]] = entry
  if "Other" not in categories:
    categories["Other"] = {"Name": strings["Other"], "Icon": "applications-other", "_path": "auto-generated"}
  return categories


# Returns a list of alternate, more generic categories for a given category name
# Reference: http://standards.freedesktop.org/menu-spec/latest/apas02.html
def normalize_category(c):
  if c in ["Network", "Email", "Dialup", "InstantMessaging", "Chat", "IRCClient", "Feed", "FileTransfer", "HamRadio",
           "News", "P2P", "RemoteAccess", "Telephony", "TelephonyTools", "VideoConference", "WebBrowser"]:
    return [c, "Internet"]
  if c in ["Game", "ActionGame", "AdventureGame", "ArcadeGame", "BoardGame", "BlocksGame", "CardGame", "KidsGame",
           "LogicGame", "RolePlaying", "Shooter", "Simulation", "SportsGame", "StrategyGame", "Sports", "Amusement"]:
    return [c, "Games"]
  if c in ["Utility", "TextTool", "TextTools", "Archiving", "Compression", "FileTool", "FileTools", "Calculator",
           "Clock", "TextEditor"]:
    return [c, "Accessories", "Utilities"]
  if c in ["Building", "Debugger", "IDE", "GUIDesigner", "Profiling", "RevisionControl", "Translation",
           "WebDevelopment", "ParallelComputing", "Database", "ArtificialIntelligence", "Programming"]:
    return [c, "Development"]
  if c in ["Calendar", "ContactManagement", "Dictionary", "Chart", "Finance", "FlowChart", "PDA", "ProjectManagement",
           "Presentation", "Spreadsheet", "WordProcessor", "Publishing", "Viewer"]:
    return [c, "Office"]
  if c in ["2DGraphics", "VectorGraphics", "RasterGraphics", "3DGraphics", "Scanning", "OCR", "Photography",
           "ImageProcessing"]:
    return [c, "Graphics"]
  if c in ["AudioVideo", "Player", "Audio", "Video", "Midi", "Mixer", "Sequencer", "Tuner", "TV", "AudioVideoEditing",
           "Recorder", "DiscBurning", "Adult"]:
    return [c, "Multimedia", "Sound & Video"]
  if c in ["Construction", "Astronomy", "Biology", "Chemistry", "ComputerScience", "DataVisualization", "Economy",
           "Electricity", "Geography", "Geology", "Geoscience", "Maps", "Math", "NumericalAnalysis", "MedicalSoftware",
           "Physics", "Robotics", "Electronics", "Engineering"]:
    return [c, "Science"]
  if c in ["Literature", "Art", "Languages", "History", "Humanities", "Spirituality"]:
    return [c, "Education", "Science"]
  if c in ["Emulator", "FileManager", "TerminalEmulator", "Filesystem", "Monitor"]:
    return [c, "System"]
  if c in ["Settings", "Security", "Accessibility"]:
    return [c, "Preferences"]
  return [c]


# Returns a list of suggested categories for a given application name (useful if no category is specified or found)
def suggest_categories(app_name):
  app_name = app_name.lower()
  if "network" in app_name or "google" in app_name or "cisco" in app_name or "mail" in app_name or "youtube" in app_name:
    return normalize_category("Network")
  return ["Other"]


def get_cmd(app):
  if "Exec" in app:
    cmd = ""
    if "Path" in app and app["Path"]:
      cmd += "cd " + app["Path"] + ";"
    exe = ""
    percent = False
    for c in app["Exec"]:
      if not percent:
        if c == "%":
          percent = True
        else:
          exe += c
      else:
        if c == "%":
          exe += c
          percent = False
        else:
          pass
    cmd += exe
    if "Terminal" in app and app["Terminal"] == "true":
      cmd = "x-terminal-emulator -e '" + cmd + "'"
    return cmd
  return None


# Returns the start menu hierarchy and the main application categories
# The menu is a dictionary category-name -> list of application entries
# The categories are in the same form as returned by load_categories()
def load_applications(wm, static=False):
  categories = load_categories()
  menu = {}
  for d in get_setting_locations():
    d = d + "/applications/"
    for (dirpath, dirnames, filenames) in os.walk(d):
      for filename in filenames:
        try:
          entry = read_desktop_entry(os.path.join(dirpath, filename))
        except:
          continue
        cmd = get_cmd(entry)
        if "Type" in entry and entry["Type"] == "Application" and cmd and ("NoDisplay" not in entry or not entry["NoDisplay"]):
          entry["cmd"] = cmd
          if "Name" not in entry:
            entry["Name"] = filename.replace(".desktop", "")
            entry["Name"] = entry["Name"][:1].upper() + entry["Name"][1:]
          app_categories = []
          if "Categories" in entry:
            app_categories = [s.strip() for s in entry["Categories"].split(";") if s.strip()]
          app_categories.append("")
          added = False
          for c in app_categories:
            options = []
            if c:
              if c not in categories:
                options = normalize_category(c)
              else:
                options = [c]
            else:
              options = suggest_categories(entry["_pmenu_raw_Name"])
            for o in options:
              if o in categories:
                if o not in menu:
                  menu[o] = []
                menu[o].append(entry)
                added = True
                break
            if added:
              break
  for c in menu:
    menu[c] = sorted(menu[c], key=lambda item: item["Name"])
  if wm == "openbox":
    menu[""] = [None]
    if which("obconf"):
      menu[""] += [
        internationalized({"_path": "", "Name": "Settings", "Icon": "obconf", "cmd": "obconf"})]
    if static:
      menu[""] += [
        internationalized({"_path": "", "Name": "Reload", "Icon": "reload", "cmd": "sh -c 'pmenu.py --mode openbox-static --wm openbox > ~/.config/openbox/menu.xml ; openbox --reconfigure'"}),
      ]
    if which("slock"):
      menu[""] += [
        internationalized({"_path": "", "Name": "Lock Screen", "Icon": "system-lock-screen", "cmd": "slock"}),
      ]
    menu[""] += [
      internationalized({"_path": "", "Name": "Log Out", "Icon": "system-log-out", "cmd": "openbox --exit"})
    ]
  elif wm == "xfce":
    menu[""] = [
      None,
      internationalized({"_path": "", "Name": "Settings", "Icon": "preferences-desktop", "cmd": "xfce4-settings-manager"}),
      internationalized({"_path": "", "Name": "Lock Screen", "Icon": "system-lock-screen", "cmd": "xflock4"}),
      internationalized({"_path": "", "Name": "Log Out", "Icon": "system-log-out", "cmd": "xfce4-session-logout"})
    ]
  # TODO add support for other DEs
  return menu, categories


def cat_file(path):
  if path and os.path.isfile(path):
    with open(path, encoding='utf-8') as data_file:
      print(data_file.read())


# Called when the menu is closed, exits
def gtk_destroy(obj):
  import gobject
  gobject.timeout_add(100, gtk.main_quit)


# Called when an application menu item is clicked, executes the application
def gtk_activate(obj, app):
  try:
    os.system(app["cmd"])
  except:
    pass
  sys.exit(0)


# Loads an image given an icon name or path
def gtk_load_image(name):
  image = gtk.Image()
  if "/" in name:
    if os.path.isfile(name):
      pixbuf = gtk.gdk.pixbuf_new_from_file_at_size(name, icon_size, icon_size)
      image.set_from_pixbuf(pixbuf)
      return image
  image.set_from_icon_name(name, gtk.ICON_SIZE_DND)
  image.set_pixel_size(icon_size)
  return image


def gtk_position_menu(menu, x, y):
  if x == None and y == None:
    return
  mx, my, mods = menu.get_screen().get_root_window().get_pointer()
  if x == None:
    x = mx
  if y == None:
    y = my
  win = menu.get_property("window").get_toplevel()
  _, _, w, h, _ = win.get_geometry()
  screen = win.get_screen()
  sw = screen.get_width()
  sh = screen.get_height()

  x1 = x2 = y1 = y2 = None
  panel_x1 = panel_x2 = panel_y1 = panel_y2 = None
  has_panel = False
  try:
    x1 = int(os.environ["TINT2_BUTTON_ALIGNED_X1"])
    x2 = int(os.environ["TINT2_BUTTON_ALIGNED_X2"])
    y1 = int(os.environ["TINT2_BUTTON_ALIGNED_Y1"])
    y2 = int(os.environ["TINT2_BUTTON_ALIGNED_Y2"])
    panel_x1 = int(os.environ["TINT2_BUTTON_PANEL_X1"])
    panel_x2 = int(os.environ["TINT2_BUTTON_PANEL_X2"])
    panel_y1 = int(os.environ["TINT2_BUTTON_PANEL_Y1"])
    panel_y2 = int(os.environ["TINT2_BUTTON_PANEL_Y2"])
    has_panel = True
  except:
    pass

  if not has_panel:
    if x + w > sw:
      # Overflow, change direction, hang from the same point
      x -= w
    if y + h > sh:
      # Overflow, change direction, hang from the same point
      y -= h
  else:
    # Positions:
    #   [x, y, xreversed, yreversed, score]
    # Score (for horizontal direction, similar for vertical):
    # * +10 if left == x1
    # * +10 if right == x2
    # * +30 if left == panel_x1
    # * +20 if right == panel_x2
    # * -10 if left < panel_x1
    # * -5  if right > panel_x2
    # * -99 if right > sw
    # * -99 if left < 0
    positions = []
    for point in [(x1, y1), (x2, y2)]:
      for xrev in [False, True]:
        for yrev in [False, True]:
          positions.append([point[0], point[1], xrev, yrev, 0])
    for p in positions:
      xrev = p[2]
      yrev = p[3]
      left = p[0] if not xrev else p[0] - w
      top = p[1] if not yrev else p[1] - h
      right = left + w
      bottom = top + h
      score = p[4]
      #
      score += 10 if left == x1 else 0
      score += 10 if right == x2 else 0
      score += 30 if left == panel_x1 else 0
      score += 20 if right == panel_x2 else 0
      score -= 10 if left < panel_x1 else 0
      score -= 5  if right > panel_x2 else 0
      score -= 99 if left < 0 else 0
      score -= 99 if right > sw else 0
      #
      score += 10 if top == y1 and not yrev else 0
      score += 10 if bottom == y2 and yrev else 0
      score += 30 if top == panel_y1 else 0
      score += 20 if bottom == panel_y2 else 0
      score -= 10 if top < panel_y1 else 0
      score -= 5  if bottom > panel_y2 else 0
      score -= 99 if top < 0 else 0
      score -= 99 if bottom > sh else 0
      #
      p[4] = score
    p = max(positions, key=lambda p: p[4])
    xrev = p[2]
    yrev = p[3]
    left = p[0] if not xrev else p[0] - w
    top = p[1] if not yrev else p[1] - h
    x = left
    y = top
  win.move(x, y)


def gtk_get_icon_theme_name():
  gtk.settings_get_default().get_property("gtk-icon-theme-name")


def gtk_get_icon_path(name):
  if "/" in name and os.path.exists(name):
    return name
  if gtk:
    try:
      if not icon_theme_name:
        icon_theme = gtk.icon_theme_get_default()
      else:
        icon_theme = gtk.IconTheme()
        icon_theme.set_custom_theme(icon_theme_name)
      icon = icon_theme.lookup_icon(name, icon_size, 0)
      if icon and icon.get_filename():
        return icon.get_filename()
      icon = icon_theme.lookup_icon("application-x-executable", icon_size, 0)
      if icon and icon.get_filename():
        return icon.get_filename()
    except:
      pass
  return name


def sort_categories(menu):
  return sorted(menu, key=lambda x: (x is "", x))


def xml_escape(s):
  return s.replace('&', "&amp;").replace('"', "&quot;").replace("'", "&apos;").replace("<", "&lt;").replace(">", "&gt;")


def jgmenu_create_menu(arg_append_file, arg_prepend_file, wm, no_icons):
  print("jgmenu,^tag(pmenu)")
  cat_file(arg_prepend_file)
  tree, categories = load_applications(wm)
  icon = ""
  for c in sort_categories(tree):
    if c:
      category = categories[c]
      if not no_icons:
        icon = category["Icon"] if "Icon" in category else "folder"
      print(category["Name"] + ",^checkout(" + category["Name"] + ")," + icon)
    else:
      for app in tree[c]:
        if not app:
          print("^sep()")
          continue
        if not no_icons:
          icon = app["Icon"] if "Icon" in app else "application-x-executable"
        print(app["Name"] + "," + app["cmd"] + "," + icon)
  cat_file(arg_append_file)
  for c in sort_categories(tree):
    if not c:
      continue
    category = categories[c]
    print("")
    print("#", category["_path"])
    print("submenu,^tag(" + category["Name"] + ")")
    print(strings["Back"] + ",^back(),go-previous")
    for app in tree[c]:
      if not app:
        print("^sep()")
        continue
      if not no_icons:
        icon = app["Icon"] if "Icon" in app else "application-x-executable"
      print("#", app["_path"])
      print(app["Name"] + "," + app["cmd"] + "," + icon)


def gtk_create_menu(x, y, wm, no_icons):
  tree, categories = load_applications(wm)
  menu = gtk.Menu()
  menu.connect("deactivate", gtk_destroy)
  for c in sort_categories(tree):
    if c:
      category = categories[c]
      group = gtk.ImageMenuItem()
      group.set_label(category["Name"])
      if not no_icons:
        image = gtk_load_image(category["Icon"] if "Icon" in category else "folder")
        group.set_image(image)
        group.set_always_show_image(not no_icons)
      else:
        group.set_always_show_image(False)
      submenu = gtk.Menu()
    else:
      submenu = menu
    for app in tree[c]:
      if not app:
        menu.append(gtk.SeparatorMenuItem())
        continue
      item = gtk.ImageMenuItem()
      item.set_label(app["Name"])
      tooltip = app["Comment"] if "Comment" in app else app["GenericName"] if "GenericName" in app else app["Name"]
      tooltip += "\n\n"
      if app["_path"]:
        tooltip += "(" + app["_path"] + ")" + "\n"
      tooltip += app["cmd"] if "cmd" in app else ""
      if "Path" in app and app["Path"]:
        tooltip += "\n" + " Path: " + app["Path"]
      item.set_tooltip_text(tooltip)
      if not no_icons:
        image = gtk_load_image(app["Icon"] if "Icon" in app else "application-x-executable")
        item.set_image(image)
        item.set_always_show_image(True)
      else:
        item.set_always_show_image(False)
      item.connect("activate", gtk_activate, app)
      submenu.append(item)
    if c:
      group.set_submenu(submenu)
      menu.append(group)
  menu.show_all()
  menu.popup(None, None, None, 0, 0)
  gtk_position_menu(menu, x, y)
  gtk.main()


def openbox_create_menu(wm, static, no_icons):
  if not static:
    print("<openbox_pipe_menu>")
  else:
    print("<openbox_menu>")
    print('<menu id="root-menu" label="Openbox 3">')
  tree, categories = load_applications(wm, static)
  for c in sort_categories(tree):
    if c:
      category = categories[c]
      if not no_icons:
        icon = gtk_get_icon_path(category["Icon"] if "Icon" in category else "folder")
        print('<menu id="{0}" label="{0}" icon="{1}">'.format(xml_escape(category["Name"]), xml_escape(icon)))
      else:
        print('<menu id="{0}" label="{0}">'.format(xml_escape(category["Name"])))
    for app in tree[c]:
      if not app:
        print('''<separator />''')
        continue
      if not no_icons:
        icon = gtk_get_icon_path(app["Icon"] if "Icon" in app else "application-x-executable")
        print('''<item label="{0}" icon="{1}">
                    <action name="Execute">
                       <command>
                          {2}
                       </command>
                    </action>
                 </item>'''.format(xml_escape(app["Name"]), xml_escape(icon), xml_escape(app["cmd"])))
      else:
        print('''<item label="{0}">
                    <action name="Execute">
                       <command>
                          {1}
                       </command>
                    </action>
                 </item>'''.format(xml_escape(app["Name"]), xml_escape(app["cmd"])))
    if c:
      print('</menu>')
  if not static:
    print("</openbox_pipe_menu>")
  else:
    print("</menu>")
    print("</openbox_menu>")


def setup_gettext():
  global _
  tr = gettext.NullTranslations()
  try:
    tr.add_fallback(gettext.translation("gnome-menus-3.0", languages=get_current_locale_names()))
  except:
    try:
      tr.add_fallback(gettext.translation("gnome-menus", languages=get_current_locale_names()))
    except:
      pass
  try:
    tr.add_fallback(gettext.translation("openbox", languages=get_current_locale_names()))
  except:
    pass
  try:
    tr.add_fallback(gettext.translation("xfce4-panel", languages=get_current_locale_names()))
  except:
    pass
  def _(s):
    try:
      return tr.ugettext(s)
    except:
      pass
    return s


def main():
  global gtk
  global strings
  global icon_size
  global icon_theme_name

  parser = argparse.ArgumentParser()
  parser.add_argument("--mode", help="The method used to display the menu. One of: gtk, openbox, obenbox-static, jgmenu. Default: gtk.", default="gtk")
  parser.add_argument("--wm", help="Display a custom menu for this window manager. One of: openbox, xfce.")
  parser.add_argument("--x", help="The x coordinate where to show the menu.", type=int)
  parser.add_argument("--y", help="The y coordinate where to show the menu.", type=int)
  parser.add_argument("--no-icons", help="Disable icons.", action="store_true")
  parser.add_argument("--append-file", help="Path to menu file to append to the root menu. Only applies to jgmenu.", metavar="FILE")
  parser.add_argument("--prepend-file", help="Path to menu file to prepend to the root menu. Only applies to jgmenu.", metavar="FILE")
  parser.add_argument("--locale", help="Use a custom locale (e.g. 'en_US.UTF-8'; available locales can be shown " +
                                       "by running 'locale -a')", default="")
  parser.add_argument("--icon-theme", help="Use a custom icon theme", default="")
  args = parser.parse_args()
  try:
    locale.setlocale(locale.LC_ALL, args.locale)
  except:
    sys.stderr.write("Warning: setting locale failed! Use an available locale as listed by 'locale -a'.")
  setup_gettext()
  strings = internationalized(strings)
  icon_theme_name = args.icon_theme
  if args.mode == "jgmenu":
    append_file = args.append_file if args.append_file else os.getenv("HOME") + "/.config/jgmenu/append.csv"
    prepend_file = args.prepend_file if args.prepend_file else os.getenv("HOME") + "/.config/jgmenu/prepend.csv"
    jgmenu_create_menu(append_file, prepend_file, args.wm, args.no_icons)
  elif args.mode == "gtk":
    import gtk
    if args.x == None and args.y == None:
      try:
        args.x = int(os.environ["TINT2_BUTTON_ALIGNED_X"])
        args.y = int(os.environ["TINT2_BUTTON_ALIGNED_Y"])
      except:
        pass
    gtk_create_menu(args.x, args.y, args.wm, args.no_icons)
  elif args.mode == "openbox" or args.mode == "openbox-static":
    try:
      import gtk
    except:
      pass
    icon_size = 24
    openbox_create_menu(args.wm, args.mode == "openbox-static", args.no_icons)


if __name__ == '__main__':
  main()
