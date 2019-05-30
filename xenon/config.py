from os import environ as env


token = env.get('NDc3NDk2MTcyNTkyODg5ODY2.XO7JHQ.9cZZA2GK9QGmDSWVnJJit0SN2Gs')
# shard_count and shard_ids can be overridden by Command Line Arguments
shard_count = None  # ~ guilds // 1000
shard_ids = None

prefix = "#!"

extensions = [
    "cogs.errors",
    "cogs.help",
    "cogs.admin",
    "cogs.backups",
    "cogs.templates",
    "cogs.users",
    "cogs.basics",
    "cogs.sharding",
    "cogs.botlist"
]

db_host = env.get('DB_HOST') or 'localhost'

support_guild = 410488579140354049
owner_id = 386861188891279362

template_approval_channel = 565845836529926144
template_list = env.get('TEMPLATE_LIST')
template_approval = env.get('TEMPLATE_APPROVAL')
template_featured = env.get('TEMPLATE_FEATURED')

dbl_token = env.get('DBL_TOKEN')
