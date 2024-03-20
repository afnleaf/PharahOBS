# Replaycode-ocr Discord Bot

## Install
https://discord.com/oauth2/authorize?client_id=1214396853374812211&permissions=68672&scope=bot

- Click link to add the bot to your server
- Limit the channels the bot has access to
- DM the bot if you want to
- Bot will only process images it can template match

If you would like to run a self hosted version of the bot reach out to me -> @afnckingleaf on twitter or discord.

## What works
- Post picture in a channel the bot sees, it spits out replay codes as text, but only if the template is matched.
- React to the message if it was right or wrong to help out with improving the character recognition.

## Problems
- Pytesseract character recognition issues
    - 3, 5, 8, 9 vs S
    - 1 vs I
    - 0 vs O (Actually the same)
    - 8 vs E
    - D vs O
    - 9 vs O

## ToDo:
- [x] message bot directly
- [x] accept images only
- [x] create message then edit it (let user know bot is calculating)
- [x] template match for high pixel density
- [x] variable high density sizes for crop
- [x] logging for testing
- [x] reactions to output
- [x] refactor respond_to_message()
- [x] logs go to server
- [x] sort by order found in image
- [x] testing cases for accuracy increase/decrease with ocr performance testing
- [x] fixing ocr performance
- [ ] prod vs test env
- [ ] how to configure bot
- [ ] monitor specific channel in a guild (user perms?)
