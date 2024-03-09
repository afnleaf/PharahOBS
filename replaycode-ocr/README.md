# replaycode-ocr bot

## Install
https://discord.com/oauth2/authorize?client_id=1214396853374812211&permissions=68672&scope=bot

- Click link to add the bot to your server
- Limit the channels the bot has access to
- DM the bot if you want to
- Bot will only process images it can template match


## What works
- Post picture in a channel the bot sees, it spits out replay codes as text, but only if the template is matched.
- React to the message if it was right or wrong to help out with improving the character recognition.

## ToDo:
- [x] message bot directly
- [x] accept images only
- [x] create message then edit it (let user know bot is calculating)
- [x] template match for high pixel density
- [x] variable high density sizes for crop
- [x] logging for testing
- [x] reactions to output
- [ ] refactor respond_to_message()
- [ ] how to configure bot
- [ ] log scraper at end of day
- [ ] fixing ocr performance
- [ ] monitor specific channel in a guild (user perms?)
