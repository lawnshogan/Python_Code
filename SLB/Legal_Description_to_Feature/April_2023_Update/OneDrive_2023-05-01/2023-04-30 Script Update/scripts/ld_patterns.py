PATTERNS = {
#Halves - 4
"E1/2":  ["NWNE","NENE","SWNE","SENE","NWSE","NESE","SWSE","SESE"],
"W1/2":  ["NWNW","NENW","SWNW","SENW","NWSW","NESW","SWSW","SESW"],
"S1/2":  ["NWSW","NESW","SWSW","SESW","NWSE","NESE","SWSE","SESE"],
"N1/2":  ["NWNW","NENW","SWNW","SENW","NWNE","NENE","SWNE","SENE"],

#Quarters - 4
"NW1/4":  ["NWNW","NENW","SWNW","SENW"],
"NE1/4":  ["NWNE","NENE","SWNE","SENE"],
"SW1/4":  ["NWSW","NESW","SWSW","SESW"],
"SE1/4":  ["NWSE","NESE","SWSE","SESE"],

#Half Quarters - 16
"W1/2NW1/4":  ["NWNW","SWNW"],
"E1/2NW1/4":  ["NENW","SENW"],
"N1/2NW1/4":  ["NWNW","NENW"],
"S1/2NW1/4":  ["SWNW","SENW"],
"W1/2NE1/4":  ["NWNE","SWNE"],
"E1/2NE1/4":  ["NENE","SENE"],
"N1/2NE1/4":  ["NWNE","NENE"],
"S1/2NE1/4":  ["SWNE","SENE"],
"W1/2SW1/4":  ["NWSW","SWSW"],
"E1/2SW1/4":  ["NESW","SESW"],
"N1/2SW1/4":  ["NWSW","NESW"],
"S1/2SW1/4":  ["SWSW","SESW"],
"W1/2SE1/4":  ["NWSE","SWSE"],
"E1/2SE1/4":  ["NESE","SESE"],
"N1/2SE1/4":  ["NWSE","NESE"],
"S1/2SE1/4":  ["SWSE","SESE"],

#Half Halves - 8
"W1/2W1/2":  ["NWNW","SWNW","NWSW","SWSW"],
"E1/2W1/2":  ["NENW","SENW","NESW","SESW"],
"W1/2E1/2":  ["NWNE","SWNE","NWSE","SWSE"],
"E1/2E1/2":  ["NENE","SENE","NESE","SESE"],
"N1/2N1/2":  ["NWNW","NENW","NWNE","NENE"],
"S1/2N1/2":  ["SWNW","SENW","SWNE","SENE"],
"N1/2S1/2":  ["NWSW","NESW","NWSE","NESE"],
"S1/2S1/2":  ["SWSW","SESW","SWSE","SESE"],

#Quarter Quarters - 16
"NW1/4NW1/4":  ["NWNW"],
"NE1/4NW1/4":  ["NENW"],
"SW1/4NW1/4":  ["SWNW"],
"SE1/4NW1/4":  ["SENW"],
"NW1/4NE1/4":  ["NWNE"],
"NE1/4NE1/4":  ["NENE"],
"SW1/4NE1/4":  ["SWNE"],
"SE1/4NE1/4":  ["SENE"],t
"NW1/4SW1/4":  ["NWSW"],
"NE1/4SW1/4":  ["NESW"],
"SW1/4SW1/4":  ["SWSW"],
"SE1/4SW1/4":  ["SESW"],
"NW1/4SE1/4":  ["NWSE"],
"NE1/4SE1/4":  ["NESE"],
"SW1/4SE1/4":  ["SWSE"],
"SE1/4SE1/4":  ["SESE"],

#<<<<<<<<<<<<<<<  FOLLOWING NEED VALUES ASSIGNED!   >>>>>>>>>>>>>>>
# '2E':  ["NWNE","NENE","SWNE","SENE","NWSE","NESE","SWSE","SESE"],
# '2N':  [NWNW","NENW","SWNW","SENW","NWNE","NENE","SWNE","SENE],
# '2NE':  ["NWNE","NENE","SWNE","SENE"],
# '2NW':  ["NWNW","NENW","SWNW","SENW"],
# '2S':  ["NWSW","NESW","SWSW","SESW","NWSE","NESE","SWSE","SESE"],
# '2SE':  ["NWSE","NESE","SWSE","SESE"],
# '2SESE':  [SESE],
# '2SW':  ["NWSW","NESW","SWSW","SESW"],
# '2SWSW':  ["SWSW"],
# '2W':  ["NWNW","NENW","SWNW","SENW","NWSW","NESW","SWSW","SESW"],
# '4NE':  ["NWNE","NENE","SWNE","SENE"],
# '4SE':  ["NWSE","NESE","SWSE","SESE"],
# '4SW':  ["NWSW","NESW","SWSW","SESW"],
# 'E':  ["NWNE","NENE","SWNE","SENE","NWSE","NESE","SWSE","SESE"],
# 'E/2':  ["NWNE","NENE","SWNE","SENE","NWSE","NESE","SWSE","SESE"],
# 'E/2SE':  ["NESE","SESE"],
# 'E2':  ["NWNE","NENE","SWNE","SENE","NWSE","NESE","SWSE","SESE"],
# 'E2E2':  ["NENE","SENE","NESE","SESE"],
# 'E2E2NE':  [],
# 'E2E2NENE':  [],
# 'E2E2NW':  [],
# 'E2E2SE':  [],
# 'E2E2SENWSE':  [],
# 'E2E2SW':  [],
# 'E2E2SWNE':  [],
# 'E2E2W2':  [],
# 'E2E2W2NE':  [],
# 'E2N2':  [],
# 'E2NE':  [],
# 'E2NE4':  [],
# 'E2NESE':  [],
# 'E2NESW':  [],
# 'E2NW':  [],
# 'E2NW4':  [],
# 'E2NWNE':  [],
# 'E2NWNW':  [],
# 'E2NWNWSE':  [],
# 'E2NWSE':  [],
# 'E2NWSW':  [],
# 'E2SE':  [],
# 'E2SE4':  [],
# 'E2SENE':  [],
# 'E2SENW':  [],
# 'E2SESE':  [],
# 'E2SESW':  [],
# 'E2SW':  [],
# 'E2SW4':  [],
# 'E2SW4SW4':  [],
# 'E2SWNW':  [],
# 'E2SWSE':  [],
# 'E2SWSW':  [],
# 'E2W':  [],
# 'E2W2':  [],
# 'E2W2NE':  [],
# 'E2W2SWSE':  [],
# 'E3SE':  [],
# 'N':  [],
# 'N2':  [],
# 'N2E2':  [],
# 'N2N2':  [],
# 'N2N2N2':  [],
# 'N2N2N2N2':  [],
# 'N2N2NE':  [],
# 'N2N2NW':  [],
# 'N2N2NWNW':  [],
# 'N2N2S2':  [],
# 'N2N2SE':  [],
# 'N2N2SW':  [],
# 'N2N3':  [],
# 'N2NE':  [],
# 'N2NE4':  [],
# 'N2NENE':  [],
# 'N2NENW':  [],
# 'N2NESE':  [],
# 'N2NESW':  [],
# 'N2NW':  [],
# 'N2NW4':  [],
# 'N2NWNE':  [],
# 'N2NWSW':  [],
# 'N2NWSWSE':  [],
# 'N2S2':  [],
# 'N2S2NE':  [],
# 'N2S2NENE':  [],
# 'N2S2NW':  [],
# 'N2S2SE':  [],
# 'N2S2SW':  [],
# 'N2SE':  [],
# 'N2SE4':  [],
# 'N2SE4SE4':  [],
# 'N2SENE':  [],
# 'N2SENESE':  [],
# 'N2SENW':  [],
# 'N2SESE':  [],
# 'N2SESW':  [],
# 'N2SESWNE':  [],
# 'N2SW':  [],
# 'N2SW4':  [],
# 'N2SWNE':  [],
# 'N2SWNW':  [],
# 'N2SWSE':  [],
# 'N2SWSW':  [],
# 'N2SWSWSE':  [],
# 'N2SWSWSW':  [],
# 'N2W2':  [],
# 'NE':  [],
# 'NE4':  [],
# 'NE4NE4':  [],
# 'NE4NW4':  [],
# 'NE4SE4':  [],
# 'NE4SW4':  [],
# 'NENE':  [],
# 'NENENE':  [],
# 'NENENENE':  [],
# 'NENESE':  [],
# 'NENW':  [],
# 'NENWNE':  [],
# 'NENWNW':  [],
# 'NENWSE':  [],
# 'NENWSW':  [],
# 'NESE':  [],
# 'NESW':  [],
# 'NESWNE':  [],
# 'NESWNW':  [],
# 'NESWSE':  [],
# 'NW':  [],
# 'NW4':  [],
# 'NW4NE4':  [],
# 'NW4NW4':  [],
# 'NW4SE4':  [],
# 'NW4SW4':  [],
# 'NWNE':  [],
# 'NWNENE':  [],
# 'NWNW':  [],
# 'NWNWNE':  [],
# 'NWNWNESE':  [],
# 'NWNWNW':  [],
# 'NWNWSE':  [],
# 'NWSE':  [],
# 'NWSENW':  [],
# 'NWSW':  [],
# 'NWSWNESE':  [],
# 'NWSWNESW':  [],
# 'NWSWNW':  [],
# 'NWSWSE':  [],
# 'NWSWSW':  [],
# 'S':  [],
# 'S2':  [],
# 'S25':  [],
# 'S2E2':  [],
# 'S2N2':  [],
# 'S2N2N2N2NE':  [],
# 'S2N2N2N2NENW':  [],
# 'S2N2N2NE':  [],
# 'S2N2N2NENW':  [],
# 'S2N2NE':  [],
# 'S2N2NENW':  [],
# 'S2N2NWSE':  [],
# 'S2N2S2':  [],
# 'S2N2SE':  [],
# 'S2N2SW':  [],
# 'S2NE':  [],
# 'S2NE4':  [],
# 'S2NENE':  [],
# 'S2NENENE':  [],
# 'S2NENW':  [],
# 'S2NESW':  [],
# 's2NW':  [],
# 'S2NW4':  [],
# 'S2NW4SW4SW4':  [],
# 'S2NWNW':  [],
# 'S2NWSE':  [],
# 'S2S2':  [],
# 'S2S2N2NE':  [],
# 'S2S2NW':  [],
# 'S2S2S2':  [],
# 'S2S2S2S2':  [],
# 'S2S2S2S2S2S2S2':  [],
# 'S2S2SE':  [],
# 'S2S2SW':  [],
# 'S2SE':  [],
# 'S2SE4':  [],
# 'S2SE4SE4':  [],
# 'S2SENE':  [],
# 'S2SENW':  [],
# 'S2SENWSE':  [],
# 'S2SESE':  [],
# 'S2SESENW':  [],
# 'S2SESW':  [],
# 'S2SW':  [],
# 'S2SW4':  [],
# 'S2SWNW':  [],
# 'S2SWSE':  [],
# 'S2SWSENW':  [],
# 'S2SWSWSW':  [],
# 'S2W2':  [],
# 'SE':  [],
# 'SE4':  [],
# 'SE4NE4':  [],
# 'SE4NW4':  [],
# 'SE4SE4':  [],
# 'SE4SW4':  [],
# 'SENE':  [],
# 'SENENWNE':  [],
# 'SENESE':  [],
# 'SENESW':  [],
# 'SENEW':  [],
# 'SENW':  [],
# 'SENWNW':  [],
# 'SENWSW':  [],
# 'SESE':  [],
# 'SESENW':  [],
# 'SESESWSW':  [],
# 'SESW':  [],
# 'SESWNE':  [],
# 'SESWSE':  [],
# 'SESWSW':  [],
# 'SESWSWSW':  [],
# 'SW':  [],
# 'Sw1':  [],
# 'SW4':  [],
# 'SW4NE4':  [],
# 'SW4NW4':  [],
# 'SW4SE4':  [],
# 'SW4SW4':  [],
# 'SWNE':  [],
# 'SWNENE':  [],
# 'SWNENW':  [],
# 'SWNESW':  [],
# 'SWNW':  [],
# 'SWNWNENE':  [],
# 'SWNWNW':  [],
# 'SWNWNWNW':  [],
# 'SWSE':  [],
# 'SWSENE':  [],
# 'SWSENW':  [],
# 'SWSW':  [],
# 'SWSWNE':  [],
# 'SWSWNW':  [],
# 'SWSWNWSE':  [],
# 'SWSWSE':  [],
# 'SWSWSESW':  [],
# 'SWSWSW':  [],
# 'W':  [],
# 'W2':  [],
# 'W2E2':  [],
# 'W2E2E2':  [],
# 'W2E2NESE':  [],
# 'W2E2NW':  [],
# 'W2E2SW':  [],
# 'W2E2W2NE':  [],
# 'W2N2N2NWSE':  [],
# 'W2NE':  [],
# 'W2NE4':  [],
# 'W2NENE':  [],
# 'W2NENW':  [],
# 'W2NESE':  [],
# 'W2NESW':  [],
# 'W2NW':  [],
# 'W2NW4':  [],
# 'W2NWNE':  [],
# 'W2NWNWSE':  [],
# 'W2NWSE':  [],
# 'W2NWSESE':  [],
# 'W2NWSW':  [],
# 'W2SE':  [],
# 'W2SE4':  [],
# 'W2SENE':  [],
# 'W2SENW':  [],
# 'W2SESE':  [],
# 'W2SW':  [],
# 'W2SW4':  [],
# 'W2SWNE':  [],
# 'W2SWNW':  [],
# 'W2W2':  [],
# 'W2W2E2NE':  [],
# 'W2W2E2SE':  [],
# 'W2W2NW':  [],
# 'W2W2SE':  [],
# 'W2W2SW':  [],
# 'W2W2W2':  [],
# 'W2W2W2W2W2W2':  [],
# 'W2W2NE':  []




    # All
    # "ALL": ["NWNE","NENE","SWNE","SENE","NWSE","NESE","SWSE","SESE","NWNW","NENW","SWNW","SENW","NWSW","NESW","SWSW","SESW","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36"]#
}
