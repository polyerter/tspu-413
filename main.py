# integer
number_1 = 12

# float
number_2 = 15.15 # float

print(
    number_1,
    number_2,
)

string_1 = 'hello "world"'
string_2 = "hello 'world'"
string_3 = "hello \\ \"world\" \\" 
string_4 = "\n"

print(
    string_1, 
    string_4,
    string_2,
    string_4,
    string_3,
)

string_5 = string_1.title()
string_6 = "string string STRING string string".title()

string_7 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In lacus lacus, malesuada id tempor et, consequat vitae dui. Fusce quis placerat metus. Curabitur vel arcu mi. Cras euismod dolor urna, nec ultrices ex vulputate eu. Cras tincidunt nibh at dui porttitor gravida. Integer urna purus, efficitur ac metus in, convallis rutrum ante. Fusce eu elit facilisis risus tempor imperdiet sit amet sed tortor. Curabitur ut velit nec lorem consequat laoreet eu eget mi. Nam eleifend id nibh quis dapibus. Sed rutrum, tellus et porttitor suscipit, mauris ligula luctus augue, vel pharetra ligula felis at turpis. Vivamus faucibus viverra orci a dapibus. Proin eget magna in eros tempor ultricies sit amet sed turpis.'
string_8 = 'Sed magna libero, iaculis sit amet erat ornare, lacinia placerat ante. Vestibulum semper risus turpis, sed sodales arcu iaculis sit amet. Maecenas iaculis diam ut tortor efficitur condimentum. Curabitur vitae nisi ligula. Sed varius iaculis suscipit. Proin quis nulla quam. In sed sagittis neque. Nulla metus lorem, euismod quis tellus nec, facilisis venenatis erat. Duis condimentum, ex vestibulum malesuada cursus, mi lectus blandit sem, eu ullamcorper massa purus ac massa. Ut sed justo non mauris fringilla porttitor. Sed sit amet convallis sapien.'
string_9 = string_7 + string_8.upper()

string_10 = f'{string_1}, asdasd, asd, {string_6}'

print(
    string_5,
    string_6,
    string_4,
    string_6.lower(),
    string_4,
    string_6.upper(),
)

print(
    string_9,
    string_4,
    string_10,
)


