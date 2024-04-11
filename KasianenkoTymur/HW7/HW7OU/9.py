def are_you_playing_banjo(name):
    if name[0]=='r' or name[0]=='R':
        return name + " plays banjo" 
    else:
         return name  + " does not play banjo" 
    

print(are_you_playing_banjo("martin"))
print(are_you_playing_banjo("Rikke"))
print(are_you_playing_banjo("bravo"))
print(are_you_playing_banjo("rolf"))