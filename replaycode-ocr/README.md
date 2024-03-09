# replaycode-ocr bot

## Install
https://discord.com/oauth2/authorize?client_id=1214396853374812211&permissions=68672&scope=bot

- Click link to add the bot to your server
- Limit the channels the bot has access to
- You can DM it as well
- Bot will only process images it can template match


## What works
post picture in a channel the bot sees, it spits out replay code as text, but only if the template is matched

## ToDo:
- [x] message bot directly
- [x] accept images only
- [x] create message then edit it (let user know bot is calculating)
- [x] template match for high pixel density
- [x] variable high density sizes for crop
- [x] logging for testing
- [x] reactions to output
- [ ] how to configure bot
- [ ] refactor respond_to_message()
- [ ] fixing ocr performance
- [ ] monitor specific channel in a guild (user perms?)
