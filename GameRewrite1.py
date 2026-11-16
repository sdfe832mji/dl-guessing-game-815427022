import random
import time
import sys

##### DATA #####################################################

## Answers ##########

# Weapon

# 800
Close_Quarters = {'name':'Close Quarters','price':'800','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'15m'}
Extended_Magazine = {'name':'Extended Magazine','price':'800','category':'Weapon','ability':'has no active or passive attributes','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Headshot_Booster = {'name':'Headshot Booster','price':'800','category':'Weapon','ability':'comes with a passive','cooldown':'9s','duration':'not applicable','range':'not applicable'}
High_Velocity_Rounds = {'name':'High Velocity Rounds','price':'800','category':'Weapon','ability':'has no active or passive attributes','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Monster_Rounds = {'name':'Monster Rounds','price':'800','category':'Weapon','ability':'has no active or passive attributes.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Rapid_Rounds = {'name':'Rapid Rounds','price':'800','category':'Weapon','ability':'has no active or passive attributes.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Restorative_Shot = {'name':'Restorative Shot','price':'800','category':'Weapon','ability':'comes with a passive.','cooldown':'6s','duration':'not applicable','range':'not applicable'}
# 1600
ActiveReload = {'name':'Active Reload','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'12s','duration':'7s','range':'not applicable'}#c12s #d7s
Fleetfoot = {'name':'Fleetfoot','price':'1600','category':'Weapon','ability':'is an active item that comes with a passive','cooldown':'16s','duration':'5s','range':'not applicable'}#c16s #d5s
Intensifying_Magazine = {'name':'Intensifying Magazine','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'2.5s','range':'not applicable'}#d2.5s
Kinetic_Dash = {'name':'Kinetic Dash','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'7s','range':'not applicable'}#d7s
Long_Range = {'name':'Long Range','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'15m'}#r15m
Melee_Charge = {'name':'Melee Charge','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'5s','duration':'not applicable','range':'not applicable'}#c5s
Mystic_Shot = {'name':'Mystic Shot','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'8s','duration':'not applicable','range':'not applicable'}#c8s
Opening_Rounds = {'name':'Opening Rounds','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Recharging_Rush = {'name':'Recharging Rush','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'25s','duration':'3.5s','range':'not applicable'}#c25s #d3.5s
Slowing_Bullets = {'name':'Slowing Bullets','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'3.5s','range':'not applicable'}#d3.5s
Spirit_Shredder = {'name':'Spirit Shredder','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'8s','range':'not applicable'}#d8s
Split_Shot = {'name':'Split Shot','price':'1600','category':'Weapon','ability':'is an active item.','cooldown':'27s','duration':'5s and 12s','range':'not applicable'}#c27s #d5s and 12s
Stalker = {'name':'Stalker','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'6s','duration':'5s','range':'8m'}#c6s #d5s #r8m
Swift_Striker = {'name':'Swift Striker','price':'1600','category':'Weapon','ability':'has no active or passive attributes.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Titanic_Magazine = {'name':'Titanic Magazine','price':'1600','category':'Weapon','ability':'has no active or passive attributes.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Weakening_Headshot = {'name':'Weakening Headshot','price':'1600','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'12s','range':'not applicable'}#d12s
# 3200
Alchemical_Fire = {'name':'Alchemical Fire','price':'3200','category':'Weapon','ability':'is an active item.','cooldown':'30s','duration':'5s','range':'10m'}#c30s #d5s #r10m
Ballistic_Enchantment = {'name':'Ballistic Enchantment','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'20s','range':'not applicable'}#d20s
Berserker = {'name':'Berserker','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'10s','range':'not applicable'}#d10s
Blood_Tribute = {'name':'Blood Tribute','price':'3200','category':'Weapon','ability':'is an active item.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Burst_Fire = {'name':'Burst Fire','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'9s','duration':'4.5s','range':'not applicable'}#c9s #d4.5s
Cultist_Sacrifice = {'name':'Cultist Sacrifice','price':'3200','category':'Weapon','ability':'is an active item.','cooldown':'270s','duration':'160s','range':'not applicable'}#c270s #d160s
Escalating_Resilience = {'name':'Escalating Resilience','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'24s','range':'not applicable'}#d24s
Express_Shot = {'name':'Express Shot','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'8s','duration':'not applicable','range':'not applicable'}#c8s
Headhunter = {'name':'Headhunter','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'8s','duration':'3s','range':'not applicable'}#c8s #d3s
Heroic_Aura = {'name':'Heroic Aura','price':'3200','category':'Weapon','ability':'is an active item that comes with a passive','cooldown':'22s','duration':'7s','range':'35m'}#c22s #d7s #r35m
Hollow_Point = {'name':'Hollow Point','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'8s','range':'not applicable'}#d8s
Hunters_Aura = {'name':'Hunter\'s Aura','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'15m'}#r15m
Point_Blank = {'name':'Point Blank','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Shadow_Weave = {'name':'Shadow Weave','price':'3200','category':'Weapon','ability':'is an active item.','cooldown':'37s','duration':'13s, 5s, and 6s','range':'not applicable'} #c37s #d13s,5s,6s
Sharpshooter = {'name':'Sharpshooter','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'15m'} #r15m
Spirit_Rend = {'name':'Spirit Rend','price':'3200','category':'Weapon','ability':'comes with two passives','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Tesla_Bullets = {'name':'Tesla Bullets','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'0.2s','duration':'not applicable','range':'8m'} #c0.2s #r8m
Toxic_Bullets = {'name':'Toxic Bullets','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'4s','range':'not applicable'} #d4s
Weighted_Shots = {'name':'Weighted Shots','price':'3200','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'3.5s','range':'not applicable'} #d3.5s
# 6400
Armor_Piercer = {'name':'Armor Piercer','price':'6400','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Capacitor = {'name':'Capacitator','price':'6400','category':'Weapon','ability':'is an active item that comes with a passive','cooldown':'0.2s and 40s','duration':'3s','range':'10m'} #c0.2s and 40s #d3s #r10m
Crippling_Headshot = {'name':'Crippling Headshot','price':'6400','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'12s','range':'not applicable'} #d12s
Crushing_Fists = {'name':'Crushing Fists','price':'6400','category':'Weapon','ability':'comes with two passives','cooldown':'5s','duration':'0.75s and 8s','range':'not applicable'} #c5s #d0.75s and 8s
Frenzy = {'name':'Frenzy','price':'6400','category':'Weapon','ability':'comes with a passive','cooldown':'16s','duration':'10s','range':'not applicable'} #c16s #d10s
Glass_Canon = {'name':'Glass Canon','price':'6400','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Lucky_Shot = {'name':'Lucky Shot','price':'6400','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Ricochet = {'name':'Ricochet','price':'6400','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'13m'} #r13m
Silencer = {'name':'Silencer','price':'6400','category':'Weapon','ability':'comes with two passives','cooldown':'not applicable','duration':'6s and 10s','range':'not applicable'} #d6s and 10s
Spellslinger = {'name':'Spellslinger','price':'6400','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'18s','range':'not applicable'} #d18s
Spiritual_Overflow = {'name':'Spiritual Overflow','price':'6400','category':'Weapon','ability':'comes with a passive','cooldown':'not applicable','duration':'15s','range':'not applicable'} #d15s

# Spirit

# 800
Extra_Charge = {'name':'Extra Charge','price':'800','category':'Spirit','ability':'has no active or passive attributes.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Extra_Spirit = {'name':'Extra Spirit','price':'800','category':'Spirit','ability':'has no active or passive attributes.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Golden_Goose_Egg = {'name':'Golden Goose Egg','price':'800','category':'Spirit','ability':'is an active item.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Mystic_Burst = {'name':'Mystic Burst','price':'800','category':'Spirit','ability':'comes with a passive','cooldown':'14s','duration':'not applicable','range':'not applicable'} #c14s
Mystic_Expansion = {'name':'Mystic Expansion','price':'800','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Mystic_Regeneration = {'name':'Mystic Regeneration','price':'800','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'7s','range':'not applicable'} #d7s
Rusted_Barrel = {'name':'Rusted Barrel','price':'800','category':'Spirit','ability':'is an active item.','cooldown':'16s','duration':'5s','range':'32m'} #c16s #d5s #r32m
Spirit_Strike = {'name':'Spirit Strike','price':'800','category':'Spirit','ability':'comes with a passive','cooldown':'8s','duration':'6s','range':'not applicable'} #c8s #d6s
# 1600
Arcane_Surge = {'name':'Arcane Surge','price':'1600','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'7s','range':'not applicable'} #d7s
Bullet_Resist_Shredder = {'name':'Bullet Resist Shredder','price':'1600','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'8s','range':'not applicable'} #d8s
Cold_Front = {'name':'Cold Front','price':'1600','category':'Spirit','ability':'is an active item.','cooldown':'25s','duration':'4s','range':'10m'} #c25s #d4s #r10m
Compress_Cooldown = {'name':'Compress Cooldown','price':'1600','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Duration_Extender = {'name':'Duration Extender','price':'1600','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Improved_Spirit = {'name':'Improved Spirit','price':'1600','category':'Spirit','ability':'has no active or passive attributes.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Mystic_Slow = {'name':'Mystic Slow','price':'1600','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'2s','range':'not applicable'} #d2s
Mystic_Vulnerability = {'name':'Mystic Vulnerability','price':'1600','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'7s','range':'not applicable'} #d7s
Quicksilver_Reload = {'name':'Quicksilver Reload','price':'1600','category':'Spirit','ability':'comes with a passive','cooldown':'18s','duration':'not applicable','range':'not applicable'} #c18s
Slowing_Hex = {'name':'Slowing Hex','price':'1600','category':'Spirit','ability':'is an active item.','cooldown':'29s','duration':'3s','range':'25m'} #c29s #d3s #r25m
Spirit_Sap = {'name':'Spirit Sap','price':'1600','category':'Spirit','ability':'is an active item.','cooldown':'22s','duration':'12s','range':'35m'} #c22s #d12s #r35m
Suppressor = {'name':'Suppressor','price':'1600','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'stuf4.5sf','range':'not applicable'} #d4.5s
# 3200
Decay = {'name':'Decay','price':'3200','category':'Spirit','ability':'is an active item.','cooldown':'30s','duration':'12s','range':'20m'} #c30s #d12s #r20m
Disarming_Hex = {'name':'Disarming Hex','price':'3200','category':'Spirit','ability':'is an active item.','cooldown':'16s','duration':'4.25s','range':'32m'} #c16s #d4.25s #r32m
Greater_Expansion = {'name':'Greater Expansion','price':'3200','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Knockdown = {'name':'Knockdown','price':'3200','category':'Spirit','ability':'is an active item.','cooldown':'35s','duration':'not applicable','range':'45m'} #c35s #r45m
Radiant_Regeneration = {'name':'Radiant Regeneration','price':'3200','category':'Spirit','ability':'comes with two passives','cooldown':'6s','duration':'7s and 3s','range':'not applicable'} #c6s #d7s and 3s
Rapid_Recharge = {'name':'Rapid Recharge','price':'3200','category':'Spirit','ability':'has no active or passive attributes.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Silence_Wave = {'name':'Silence Wave','price':'3200','category':'Spirit','ability':'is an active item.','cooldown':'42s','duration':'not applicable','range':'25m'} #c42s #r25m
Spirit_Snatch = {'name':'Spirit Snatch','price':'3200','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'} #c6s #d10s
Superior_Cooldown = {'name':'Superior Cooldown','price':'3200','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Superior_Duration = {'name':'Superior Duration','price':'3200','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Surge_of_Power = {'name':'Surge of Power','price':'3200','category':'Spirit','ability':'comes with a passive','cooldown':'14s','duration':'8s','range':'not applicable'} #c14s #d8s
Tankbuster = {'name':'Tankbuster','price':'3200','category':'Spirit','ability':'comes with a passive','cooldown':'14s','duration':'not applicable','range':'not applicable'} #c14s
Torment_Pulse = {'name':'Torment Pulse','price':'3200','category':'Spirit','ability':'comes with a passive','cooldown':'1.4s','duration':'not applicable','range':'9m'} #c1.4s #r9m
# 6400
Arctic_Blast = {'name':'Arctic Blast','price':'6400','category':'Spirit','ability':'is an active item.','cooldown':'24s','duration':'1s','range':'16m'} #c24s #d1s #r16m
Boundless_Spirit = {'name':'Boundless Spirit','price':'6400','category':'Spirit','ability':'has no active or passive attributes.','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Cursed_Relic = {'name':'Cursed Relic','price':'6400','category':'Spirit','ability':'is an active item.','cooldown':'55s','duration':'2.5s','range':'20m'} #c55s #d2.5s #r20m
Echo_Shard = {'name':'Echo Shard','price':'6400','category':'Spirit','ability':'is an active item.','cooldown':'30s','duration':'not applicable','range':'not applicable'} #c30s
Escalating_Exposure ={'name':'Escalating Exposure','price':'6400','category':'Spirit','ability':'comes with a passive','cooldown':'0.7s','duration':'12s','range':'not applicable'} #c0.7s #d12s
Ethereal_Shift = {'name':'Ethereal Shift','price':'6400','category':'Spirit','ability':'is an active item.','cooldown':'37s','duration':'4s and 5s','range':'not applicable'} #c37s #d4s and 5s
Focus_Lens = {'name':'Focus Lens','price':'6400','category':'Spirit','ability':'is an active item.','cooldown':'40s','duration':'12s','range':'25m'} #c40s #d12s #r25m
Lightning_Scroll = {'name':'Lightning Scroll','price':'6400','category':'Spirit','ability':'comes with three passives','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Magic_Carpet = {'name':'Magic Carpet','price':'6400','category':'Spirit','ability':'is an active item.','cooldown':'32s','duration':'12s','range':'not applicable'} #c32s #d12s and 1.3s
Mercurial_Magnum = {'name':'Mercurial Magnum','price':'6400','category':'Spirit','ability':'comes with a passive','cooldown':'14s','duration':'not applicable','range':'not applicable'} #c14s
Mystic_Reverb = {'name':'Mystic Reverb','price':'6400','category':'Spirit','ability':'comes with a passive','cooldown':'6.25s','duration':'not applicable','range':'16m'} #c6.25s #r16m
Refresher = {'name':'Refresher','price':'6400','category':'Spirit','ability':'is an active item.','cooldown':'300s','duration':'not applicable','range':'not applicable'} #c300s
Scourge = {'name':'Scourge','price':'6400','category':'Spirit','ability':'is an active item.','cooldown':'35s','duration':'10s','range':'35m and 10m'} #c35s #d10s #r35m and 10m
Spirit_Burn = {'name':'Spirit Burn','price':'6400','category':'Spirit','ability':'comes with a passive','cooldown':'20s','duration':'8s','range':'not applicable'} #d20s and 8s
Transcendent_Cooldown = {'name':'Transcendent Cooldown','price':'6400','category':'Spirit','ability':'comes with a passive','cooldown':'not applicable','duration':'not applicable','range':'not applicable'}
Vortex_Web = {'name':'Vortex Web','price':'6400','category':'Spirit','ability':'is an active item.','cooldown':'42s','duration':'5s and 0.5s','range':'12m'} #c42s #d5s and 0.5s #r12m

########## Item catalog ########

catalog = {'close quarters':Close_Quarters,
           'extended magazine':Extended_Magazine,
           'headshot booster':Headshot_Booster,
           'high-velocity rounds':High_Velocity_Rounds,
           'monster rounds':Monster_Rounds,
           'rapid rounds':Rapid_Rounds,
           'restorative shot':Restorative_Shot,
           'active reload':ActiveReload,
           'fleetfoot':Fleetfoot,
           'intensifying magazine':Intensifying_Magazine,
           'kinetic dash':Kinetic_Dash,
           'long range':Long_Range,
           'melee charge':Melee_Charge,
           'mystic shot':Mystic_Shot,
           'opening rounds':Opening_Rounds,
           'recharging rush':Recharging_Rush,
           'slowing bullets':Slowing_Bullets,
           'spirit shredder':Spirit_Shredder,
           'split shot':Split_Shot,
           'stalker':Stalker,
           'swift striker':Swift_Striker,
           'titanic magazine':Titanic_Magazine,
           'weakening headshot':Weakening_Headshot,
           'alchemical fire':Alchemical_Fire,
           'ballistic enchantment':Ballistic_Enchantment,
           'berserker':Berserker,
           'blood tribute':Blood_Tribute,
           'burst fire':Burst_Fire,
           'cultist sacrifice':Cultist_Sacrifice,
           'escalating resilience':Escalating_Resilience,
           'express shot':Express_Shot,
           'headhunter':Headhunter,
           'heroic aura':Heroic_Aura,
           'hollow point':Hollow_Point,
           'hunter\'s aura':Hunters_Aura,
           'point blank':Point_Blank,
           'shadow weave':Shadow_Weave,
           'sharpshooter':Sharpshooter,
           'spirit rend':Spirit_Rend,
           'tesla bullets':Tesla_Bullets,
           'toxic bullets':Toxic_Bullets,
           'weighted shots':Weighted_Shots,
           'armor piercer':Armor_Piercer,
           'capacitor':Capacitor,
           'crippling headshot':Crippling_Headshot,
           'crushing fists':Crushing_Fists,
           'frenzy':Frenzy,
           'glass cannon':Glass_Canon,
           'lucky shot':Lucky_Shot,
           'ricochet':Ricochet,
           'silencer':Silencer,
           'spellslinger':Spellslinger,
           'spiritual overflow':Spiritual_Overflow,
           'extra charge':Extra_Charge,
           'extra spirit':Extra_Spirit,
           'golden goose egg':Golden_Goose_Egg,
           'mystic burst':Mystic_Burst,
           'mystic expansion':Mystic_Expansion,
           'mystic regeneration':Mystic_Regeneration,
           'rusted barrel':Rusted_Barrel,
           'spirit strike':Spirit_Strike,
           'arcane surge':Arcane_Surge,
           'bullet resist shredder':Bullet_Resist_Shredder,
           'cold front':Cold_Front,
           'compress cooldown':Compress_Cooldown,
           'duration extender':Duration_Extender,
           'improved spirit':Improved_Spirit,
           'mystic slow':Mystic_Slow,
           'mystic vulnerability':Mystic_Vulnerability,
           'quicksilver reload':Quicksilver_Reload,
           'slowing hex':Slowing_Hex,
           'spirit sap':Spirit_Sap,
           'suppressor':Suppressor,
           'decay':Decay,
           'disarming hex':Disarming_Hex,
           'greater expansion':Greater_Expansion,
           'knockdown':Knockdown,
           'radiant regeneration':Radiant_Regeneration,
           'rapid recharge':Rapid_Recharge,
           'silence wave':Silence_Wave,
           'spirit snatch':Spirit_Snatch,
           'superior cooldown':Superior_Cooldown,
           'superior duration':Superior_Duration,
           'surge of power':Surge_of_Power,
           'tankbuster':Tankbuster,
           'torment pulse':Torment_Pulse,
           'arctic blast':Arctic_Blast,
           'boundless spirit':Boundless_Spirit,
           'cursed relic':Cursed_Relic,
           'echo shard':Echo_Shard,
           'escalating exposure':Escalating_Exposure,
           'ethereal shift':Ethereal_Shift,
           'focus lens':Focus_Lens,
           'lightning scroll':Lightning_Scroll,
           'magic carpet':Magic_Carpet,
           'mercurial magnum':Mercurial_Magnum,
           'mystic reverb':Mystic_Reverb,
           'refresher':Refresher,
           'scourge':Scourge,
           'spirit burn':Spirit_Burn,
           'transcendent cooldown':Transcendent_Cooldown,
           'vortex web':Vortex_Web}

def show_catalog_pretty():
    print()
    print()
    print('   close quarters...extended magazine...headshot booster...high-velocity rounds...monster rounds')
    print('       rapid rounds...restorative shot...active reload...fleetfoot...intensifying magazine')
    print('    kinetic dash...long range...melee charge...mystic shot...opening rounds...recharging rush')
    print('   slowing bullets...spirit shredder...split shot...stalker...swift striker...titanic magazine')
    print('     weakening headshot...alchemical fire...ballistic enchantment...berserker...blood tribute')
    print('       burst fire...cultist sacrifice...escalating resilience...express shot...headhunter')
    print('     heroic aura...hollow point...hunter\'s aura...point blank...shadow weave...sharpshooter')
    print('    spirit rend...tesla bullets...toxic bullets...weighted shots...armor piercer...capacitor')
    print('      crippling headshot...crushing fists...frenzy...glass cannon...lucky shot...ricochet')
    print('                          silencer...spellslinger...spiritual overflow')
    print()
    print('          extra charge...extra spirit...golden goose egg...mystic burst...mystic expansion')
    print('    mystic regeneration...rusted barrel...spirit strike...arcane surge...bullet resist shredder')
    print('        cold front...compress cooldown...duration extender...improved spirit...mystic slow')
    print('    mystic vulnerability...quicksilver reload...slowing hex...spirit sap...suppressor...decay')
    print('       disarming hex...greater expansion...knockdown...radiant regeneration...rapid recharge')
    print('silence wave...spirit snatch...superior cooldown...superior duration...surge of power...tankbuster')
    print('torment pulse...arctic blast...boundless spirit...cursed relic...echo shard...escalating exposure')
    print(' ethereal shift...focus lens...lightning scroll...magic carpet...mercurial magnum...mystic reverb')
    print('              refresher...scourge...spirit burn...transcendent cooldown...vortex web')
    print()
    print()

## Common Builds ############

heroes = {'Abrams':['close quarters','monster rounds','restorative shot','melee charge','stalker','berserker','hunter\'s aura','point blank','crushing fists','spirit strike','bullet resist shredder','duration extender','spirit snatch','superior cooldown','superior duration','torment pulse'],
           'Apollo':['melee charge','extra spirit','mystic burst','mystic expansion','mystic regeneration','spirit strike','cold front','compress cooldown','improved spirit','mystic vulnerability','greater expansion','radiant regeneration','spirit snatch','superior cooldown','tankbuster','torment pulse','boundless spirit','escalating exposure','mystic reverb','spirit burn','transcendent cooldown'],
           'Baba':['opening rounds','swift striker','titanic magazine','spiritual overflow','arcane surge','compress cooldown','duration extender','improved spirit','mystic vulnerability','quicksilver reload','greater expansion','radiant regeneration','rapid recharge','spirit snatch','superior cooldown','superior duration','tankbuster','boundless spirit','escalating exposure','mercurial magnum','transcendent cooldown'],
           'Bebop':['headshot booster','headhunter','extra spirit','mystic burst','mystic expansion','spirit strike','arcane surge','compress cooldown','improved spirit','slowing hex','greater expansion','radiant regeneration','spirit snatch','superior cooldown','surge of power','tankbuster','boundless spirit','echo shard','mystic reverb','spirit burn','transcendent cooldown'],
           'Billy':['close quarters','monster rounds','melee charge','stalker','berserker','cultist sacrifice','escalating exposure','point blank','weighted shots','crushing fists','extra charge','mystic expansion','spirit strike','bullet resist shredder','slowing hex','greater expansion','rapid recharge','spirit snatch','scourge'],
           'Calico':['mystic shot','spirit shredder','stalker','hunter\'s aura','extra spirit','spirit strike','cold front','compress cooldown','improved spirit','mystic vulnerability','spirit snatch','superior cooldown','tankbuster','torment pulse','arctic blast','boundless spirit','escalating exposure','scourge','spirit burn','transcendent cooldown'],
           'Celeste':['high-velocity rounds','kinetic dash','opening rounds','swift striker','spellslinger','spiritual overflow','extra charge','extra spirit','mystic burst','mystic expansion','mystic regeneration','compress cooldown','improved spirit','mystic vulnerability','suppressor','greater expansion','radiant regeneration','rapid recharge','superior cooldown','tankbuster','torment pulse','boundless spirit','escalating exposure','refresher','transcendent cooldown'],
           'Deadman Danny':['high-velocity rounds','long range','opening rounds','express shot','sharpshooter','glass cannon','lucky shot','spiritual overflow','extra spirit','mystic burst','mystic expansion','bullet resist shredder','cold front','compress cooldown','improved spirit','greater expansion','superior cooldown','tankbuster','boundless spirit','spirit burn'],
           'The Doorman':['high-velocity rounds','opening rounds','recharging rush','extra charge','extra spirit','mystic burst','mystic expansion','compress cooldown','improved spirit','slowing hex','greater expansion','knockdown','rapid recharge','superior cooldown','tankbuster','boundless spirit','mystic reverb','spirit burn','transcendent cooldown','vortex web'],
           'Drifter':['close quarters','rapid rounds','kinetic dash','melee charge','stalker','swift striker','burst fire','hollow point','hunter\'s aura','point blank','shadow weave','toxic bullets','weighted shots','crippling headshot','lucky shot','silencer','extra spirit','mythic burst','spirit strike','cold front','spirit snatch','tankbuster','arctic blast','spirit burn','boundless spirit'],
           'Dynamo':['headshot booster','recharging rush','headhunter','extra charge','extra spirit','mystic burst','mystic expansion','arcane surge','compress cooldown','duration extender','improved spirit','greater expansion','rapid recharge','superior cooldown','superior duration','tankbuster','boundless spirit','mystic reverb','refresher','spirit burn','transcendent cooldown'],
           'Graves':['monster rounds','restorative shot','mystic shot','heroic aura','toxic bullets','ricochet','spiritual overflow','extra charge','extra spirit','arcane surge','compress cooldown','duration extender','improved spirit','mystic vulnerability','superior cooldown','superior duration','tankbuster','boundless spirit','echo shard','escalating exposure','refresher','spirit burn','transcendent cooldown'],
           'Grey Talon':['high-velocity rounds','rapid rounds','restorative shot','long range','mystic shot','opening rounds','recharging rush','sharpshooter','spiritual overflow','extra charge','extra spirit','mystic burst','compress cooldown','improved spirit','rapid recharge','superior cooldown','surge of power','tankbuster','boundless spirit','mystic reverb','spirit burn','transcendent cooldown'],
           'Haze':['extended magazine','rapid rounds','active reload','swift striker','titanic magazine','weakening headshot','burst fire','tesla bullets','toxic bullets','capacitator','crippling headshot','lucky shot','ricochet','silencer','extra spirit','bullet resist shredder','slowing hex','surge of power','mercurial magnum'],
           'Holliday':['extended magazine','headshot booster','high-velocity rounds','rapid rounds','long range','mystic shot','recharging rush','swift striker','titanic magazine','headhunter','sharpshooter','crippling headshot','glass cannon','lucky shot','extra charge','extra spirit','mystic burst','bullet resist shredder','compress cooldown','duration extender','improved spirit','mystic vulnerability','rapid recharge','superior cooldown','superior duration','surge of power','tankbuster','boundless spirit','escalating exposure','mercurial magnum','spirit burn','transcendent cooldown'],
           'Infernus':['extended magazine','rapid rounds','spirit shredder','swift striker','titanic magazine','burst fire','spirit rend','toxic bullets','ricochet','spiritual overflow','extra charge','extra spirit','duration extender','improved spirit','mystic vulnerability','quicksilver reload','rapid recharge','superior duration','boundless spirit','escalating exposure','mercurial magnum','spirit burn'],
           'Kelvin':['high-velocity rounds','opening rounds','extra charge','extra spirit','mystic burst','mystic expansion','mystic regeneration','arcane surge','compress cooldown','duration extender','improved spirit','mystic vulnerability','greater expansion','radiant regeneration','rapid recharge','superior cooldown','superior duration','tankbuster','torment pulse','boundless spirit','escalating exposure','mystic reverb','spirit burn','transcendent cooldown'],
           'Ivy':['extended magazine', 'monster rounds', 'active reload', 'fleetfoot', 'titanic magazine','headhunter','tesla bullets','capacitator','extra charge','extra spirit','mystic expansion','bullet resist shredder','compress cooldown','duration extender','improved spirit','mystic slow','mystic vulnerability','slowing hex','greater expansion','rapid recharge','superior cooldown','superior duration','boundless spirit','echo shard','escalating exposure','lightning scroll','transcendent cooldown','vortex web'],
           'Lady Geist':['monster rounds','kinetic dash','recharging rush','berserker','spellslinger','extra spirit','mystic burst','mystic expansion','mystic regeneration','compress cooldown','improved spirit','mystic vulnerability','greater expansion','radiant regeneration','rapid recharge','superior cooldown','tankbuster','boundless spirit','escalating exposure','mystic reverb','spirit burn','transcendent cooldown'],
           'Lash':['headshot booster','mystic shot','recharging rush','headhunter','extra charge','extra spirit','mystic burst','mystic expansion','cold front','compress cooldown','improved spirit','quicksilver reload','greater expansion','rapid recharge','superior cooldown','tankbuster','boundless spirit','mystic reverb','refresher','spirit burn','transcendent cooldown'],
           'Mina':['rapid rounds','mystic shot','spirit shredder','swift striker','spirit rend','toxic bullets','spiritual overflow','extra spirit','mystic burst','mystic expansion','compress cooldown','improved spirit','quicksilver reload','spirit sap','greater expansion','superior cooldown','tankbuster','boundless spirit','ethereal shift','mercurial magnum','spirit burn','transcendent cooldown'],
           'Mirage':['extended magazine','headshot booster','high-velocity rounds','monster rounds','kinetic dash','opening rounds','recharging rush','spirit shredder','titanic magazine','headhunter','spirit rend','toxic bullets','ricochet','silencer','spiritual overflow','extra spirit','mystic regeneration','compress cooldown','improved spirit','mystic vulnerability','quicksilver reload','suppressor','radiant regeneration','superior cooldown','boundless spirit','escalating exposure','mercurial magnum','transcendent cooldown'],
           'McGinnis': ['extended magazine', 'monster rounds', 'intensifying magazine', 'recharging rush', 'heroic aura', 'tesla bullets', 'extra charge', 'mystic expansion', 'arcane surge', 'compress cooldown', 'improved spirit', 'mystic slow', 'mystic vulnerability', 'quicksilver reload', 'suppressor', 'greater expansion', 'rapid recharge', 'superior cooldown', 'superior duration', 'boundless spirit', 'escalating exposure', 'lightning scroll', 'mercurial magnum', 'spirit burn', 'transcendent cooldown'],
           'Mo & Krill':['extra spirit','mystic burst','mystic expansion','mystic regeneration','cold front','compress cooldown','duration extender','improved spirit','mystic vulnerability','quicksilver reload','greater expansion','radiant regeneration','superior cooldown','superior duration','tankbuster','torment pulse','arctic blast','boundless spirit','escalating exposure','scourge','spirit burn','transcendent cooldown'],
           'Nurse Harrow': ['extended magazine', 'headshot booster', 'high velocity rounds', 'rapid rounds', 'fleetfoot', 'kinetic dash', 'opening rounds', 'swift striker', 'titanic magazine', 'toxic bullets', 'ricochet', 'spiritual overflow', 'extra spirit', 'mystic expansion', 'arcane surge', 'bullet resist shredder', 'compress cooldown', 'duration extender', 'improved spirit', 'mystic slow', 'greater expansion', 'superior cooldown' 'superior duration', 'boundless spirit'],
           'Paige':['high-velocity rounds','opening rounds','extra charge','extra spirit','mystic expansion','arcane surge','compress cooldown','duration extender','improved spirit','mystic vulnerability','slowing hex','greater expansion','knockdown','rapid recharge','superior cooldown','superior duration','tankbuster','boundless spirit','cursed relic','escalating exposure','refresher','spirit burn','transcendent cooldown','vortex web'],
           'Paradox':['headshot booster','high-velocity rounds','monster rounds','restorative shot','long range','mystic shot','opening rounds','express shot','headhunter','hollow point','sharpshooter','crippling headshot','glass cannon','mystic burst','mystic expansion','compress cooldown','duration extender','improved spirit','greater expansion','superior cooldown','superior duration','tankbuster','echo shard','mystic reverb','spirit burn','transcendent cooldown'],
           'Pocket':['monster rounds','rapid rounds','restorative shot','swift striker','cultist sacrifice','spiritual overflow','extra spirit','mystic burst','mystic expansion','cold front','compress cooldown','duration extender','improved spirit','mystic vulnerability','greater expansion','superior cooldown','superior duration','tankbuster','arctic blast','boundless spirit','escalating exposure','ethereal shift','spirit burn','transcendent cooldown'],
           'Rat King':['close quarters','extended magazine','high-velocity rounds','monster rounds','fleetfoot','opening rounds','swift striker','titanic magazine','ballistic enchantment','berserker','cultist sacrifice','heroic aura','mystic expansion','compress cooldown','superior cooldown','superior duration','transcendent cooldown'],
           'Rem':['close quarters','high-velocity rounds','monster rounds','opening rounds','extra charge','extra spirit','golden goose egg','mystic burst','mystic expansion','arcane surge','compress cooldown','duration extender','improved spirit','greater expansion','rapid recharge','superior cooldown','superior duration','surge of power','tankbuster','torment pulse','boundless spirit','cursed relic','echo shard','mystic reverb','spirit burn','transcendent cooldown'],
           'Seven':['high-velocity rounds', 'monster rounds','intensifying magazine', 'opening rounds', 'spirit shredder', 'ballistic enchantment','cultist sacrifice', 'toxic bullets', 'spiritual overflow','extra charge','extra spirit', 'mystic expansion','arcane surge','compress cooldown','duration extender','improved spirit','mystic vulnerability','greater expansion', 'rapid recharge','superior cooldown','superior duration','surge of power', 'boundless spirit','escalating exposure','lightning scroll','refresher', 'spirit burn','transcendent cooldown'],
           'Shiv':['close quarters','high-velocity rounds','restorative shot','berserker','express shot','hunter\'s aura','point blank','glass cannon','lucky shot','extra charge','mystic regeneration','bullet resist shredder','cold front','compress cooldown','mystic vulnerability','radiant regeneration','rapid recharge','superior cooldown','torment pulse','arctic blast','escalating exposure','mystic reverb','transcendent cooldown'],
           'Silver':['close quarters','restorative shot','slowing bullets','stalker','berserker','hunter\'s aura','point blank','weighted shots','frenzy', 'silencer','bullet resist shredder','duration extender','slowing hex','superior duration','tankbuster'],
           'Sinclair':['high-velocity rounds','monster rounds','opening rounds','alchemical fire','extra charge','extra spirit','mystic burst','mystic expansion','compress cooldown','duration extender','improved spirit','mystic slow','mystic vulnerability','slowing hex','greater expansion','rapid recharge','superior cooldown','superior duration','tankbuster','boundless spirit','escalating exposure','magic carpet','mystic reverb','spirit burn','transcendent cooldown','vortex web'],
           'Solomon':['high-velocity rounds','opening rounds','swift striker','titanic magazine','spiritual overflow','extra spirit','mystic burst','mystic expansion','arcane surge','compress cooldown','improved spirit','mystic slow','greater expansion','superior cooldown','tankbuster','boundless spirit','lightning scroll','spirit burn','transcendent cooldown','vortex web'],
           'Venator':['close quarters','extended magazine','high-velocity rounds','monster rounds','rapid rounds','restorative shot','fleetfoot','intensifyiing magazine','opening rounds','recharging rush','slowing bullets','swift striker','titanic magazine','weakening headshot','ballistic enchantment','berserker','cultist sacrifice','hollow point','point blank','weighted shots','crippling headshot','ricochet','silencer','extra charge','rapid recharge'],
           'Victor':['high-velocity rounds','opening rounds','extra charge','extra spirit','mystic expansion','mystic regeneration','compress cooldown','improved spirit','mystic vulnerability','greater expansion','radiant regeneration','rapid recharge','superior cooldown','torment pulse','boundless spirit','escalating exposure','ethereal shift','refresher','transcendent cooldown'],
           'Vindicta':['extended magazine','high-velocity rounds','rapid rounds','fleetfoot','long range','opening rounds','swift striker','titanic magazine','burst fire','sharpshooter','cripping headshot','glass cannon','ricochet','spellslinger','spiritual overflow','extra charge','extra spirit','mystic burst','improved spirit','quicksilver reload','rapid recharge','superior duration','boundless spirit','mercurial magnum'],
           'Violet':['high-velocity rounds','opening rounds','slowing bullets','toxic bullets','silencer','spiritual overflow','extra charge','extra spirit','mystic burst','mystic expansion','mystic regeneration','compress cooldown','improved spirit','greater expansion','radiant regeneration','rapid recharge','superior cooldown','tankbuster','surge of power','boundless spirit','escalating exposure','spirit burn'],
           'Viscous':['close quarters','high-velocity rounds','monster rounds','melee charge','mystic shot','ballistic enchantment','express shot','crushing fists','extra charge','extra spirit','mystic burst','mystic expansion','spirit strike','compress cooldown','duration extender','improved spirit','greater expansion','rapid recharge','spirit snatch','superior cooldown','superior duration','tankbuster','boundless spirit','mystic reverb','spirit burn','transcendent cooldown'],
           'Vyper':['close quarters','monster rounds','rapid rounds','fleetfoot','intensifying magazine','split shot','swift striker','burst fire','point blank','tesla bullets','capacitor','ricochet','silencer','spiritual overflow','extra spirit','bullet resist shredder','improved spirit','quicksilver reload','boundless spirit','mercurial magnum'],
           'Warden':['extended magazine','high-velocity rounds','monster rounds','rapid rounds','fleetfoot','intensifying magazine','kinetic dash','opening rounds','swift striker','titanic magazine','berserker','silencer','spellslinger','spiritual overflow','extra spirit','bullet resist shredder','improved spirit','quicksilver reload','surge of power','boundless spirit','mercurial magnum'],
           'Wraith':['extended magazine','high-velocity rounds','monster rounds','rapid rounds','opening rounds','recharging rush','spirit shredder','swift striker','burst fire','spirit rend','tesla bullets','capacitor','ricochet','silencer','spiritual overflow','extra spirit','improved spirit','quicksilver reload','surge of power','boundless spirit','mercurial magnum'],
           'Yamato':['close quarters','restorative shot','mystic shot','recharging rush','stalker','hunter\'s aura','crushing fists','extra spirit','mystic burst','mystic regeneration','spirit strike','bullet resist shredder','cold front','compress cooldown','improved spirit','radiant regeneration','spirit snatch','superior cooldown','tankbuster','torment pulse','boundless spirit','mystic reverb','refresher','spirit burn','transcendent cooldown']}


##################################################################

count = 0
winner = False

######### Round ################################################

def start_round():

    global winner
    winner = False

    def lost_game():
        print()
        print('You lost the game!')
        print()
        time.sleep(1)

    def win_game():
        print()
        global winner
        winner = True
        print('You won the game!')
        print()
        time.sleep(1)

    favorite_item = random.choice(list(catalog.keys()))
    item_data = catalog[favorite_item]

    matching_heroes = []
    for seller, items in heroes.items():
        if favorite_item in items:
            matching_heroes.append(seller)

    if matching_heroes:
        seller_list = ', '.join(matching_heroes)
    else:
        seller_list = 'nobody'

    ######## Possible Hints ###################################

    hints_item = [f'The item costs {item_data['price']} souls.',
                  f'The item is a {item_data['category']} item.',
                  f'The item {item_data['ability']}.',
                  f'The cooldown for this item is {item_data['cooldown']}.',
                  f'The duration of this item is {item_data['duration']}. This does not include delays.',
                  f'The item\'s range is {item_data['range']}. This does not include % ability range increases.',
                  f'The item is a popular buy for {seller_list}.']

    ###########################################################

    print('The possible answers are:')
    show_catalog_pretty()
    time.sleep(3)
    print('Please enter the items as they are written here.')
    time.sleep(3)
    print()
    print('A random item has been chosen!')
    print()
    time.sleep(1)

    selected_hint = random.choice(hints_item)

    while True:
        if len(hints_item) == 1:
            print('You are on your last hint!')
        else:
            print('You have', len(hints_item), 'hints left.')
        print()

        try:
            print('Here is your hint:')
            time.sleep(1)
            print()

            print('* * * * * * * * * * *')
            print(selected_hint)
            print('* * * * * * * * * * *')
            print()
            time.sleep(1)

            my_guess = input('Guess what item it is:').lower()

            if my_guess not in catalog:
                raise ValueError
            else:
                if my_guess == favorite_item:
                    print('You are correct!')
                    time.sleep(1)
                    print(f'It was {item_data['name']}!')
                    time.sleep(1)
                    win_game()
                    break
                else:
                    print('You guessed the wrong item!')
                    hints_item.remove(selected_hint)
                    print()
                    if len(hints_item) == 0:
                        print()
                        print('You ran out of hints!')
                        lost_game()
                        break
                    selected_hint = random.choice(hints_item)
                    continue
        except ValueError:
            print()
            print('That is not a valid item.')
            print('Try again!')
            print()
            continue

def loop_game():
    print('Would you like to replay?')
    while True:
        replay_consent = input('Please enter \"Yes\" or \"No\".').lower()
        if replay_consent == 'yes':
            print()
            print('The game is restarting.')
            print()
            time.sleep(1)
            break
        elif replay_consent == 'no':
            print('Thank you for playing!')
            sys.exit(0)
        else:
            print('You entered something other than \"Yes\" or \"No\".')
            time.sleep(1)
            print('Please try again.')
            continue

############### GAME HERE ##################### GAME HERE #####################

print('Welcome to my Deadlock item guessing game!')
time.sleep(1)
print('DISCLAIMER: The game only includes Weapon and Spirit items.\n ALL Vitality items are not included yet.')
time.sleep(1)
print()
print('Would you like to play?')

while True:
    game_consent = input('Please enter \"Yes\" or \"No\".').lower()
    if game_consent == 'yes':
        print()
        print('The game will start shortly.')
        print()
        time.sleep(1)
        break
    elif game_consent == 'no':
        print()
        print('Thank you for playing!')
        sys.exit(0)
    else:
        print()
        print('You entered something other than \"Yes\" or \"No\".')
        time.sleep(1)
        print('Please try again.')
        time.sleep(1)
        print()
        continue

while True:
    start_round()
    if winner:
        count = count + 1
        if count == 1:
            print('Your current highscore is:')
            print(count,'win.')
            print()
            time.sleep(1)
        else:
            print('Your current highscore is:')
            print(count,'wins.')
            print()
            time.sleep(1)
        loop_game()
    else:
        loop_game()