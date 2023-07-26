from pyrogram import Client, filters
from helper.database import db

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("😔**𝚂𝙾𝚁𝚁𝚈 ! 𝙽𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝙵𝙾𝚄𝙽𝙳...**😔") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈**✅️")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    LazyDev = await message.reply_text("Please Wait ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await LazyDev.edit("**𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝚂𝙰𝚅𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈**✅️")
	
