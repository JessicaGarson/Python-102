handles = {"kaarthika": "kaarthika", "abby": "abbypear", "jasmin": "jf2987", "matt": "TweetsbyMatt"}

print(handles)
print(handles['jasmin'])

print(handles.keys())

for name in sorted(handles.keys()):
    print(name)

print(handles.values())

for value in handles.values():
    print('handle: {}'.format(value))

print(handles.items())

handles['jess'] = 'jessicagarson'
print(handles)

handles.update({'jess': 'newhandle'})
print(handles)

del handles['jess']
print(handles)

handles.clear()
print(handles)
