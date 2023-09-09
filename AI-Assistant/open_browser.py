import webbrowser

e = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"

f = "C:/Program Files/Mozilla Firefox/firefox.exe %s"

webbrowser.get(f).open_new_tab("https://tryhackme.com")

webbrowser.get(e).open_new("https://hackerone.com")
