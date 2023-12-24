###----------[ IMPORT LIBRARY ]---------- ###
import random,os,sys
from time import localtime as lt
from os import system
import time
from time import sleep
try:
	import pyfiglet
except ModuleNotFoundError:
	os.system('pip install pyfiglet')

text_logo =  ("""


\033[1;92m \x1b[38;5;46m       █████  ███████  ██████ ██ ██ 
\033[1;92m \x1b[38;5;47m      ██   ██ ██      ██      ██ ██ 
\033[1;92m \x1b[38;5;48m      ███████ ███████ ██      ██ ██ 
\033[1;92m \x1b[38;5;49m      ██   ██      ██ ██      ██ ██ 
\033[1;92m \x1b[38;5;50m      ██   ██ ███████  ██████ ██ ██  \033[1;32m[\x1b\033[38;5;196m\x1b[1;97m\x1b[1;41m LOGO \x1b[0m\033[1;32m]
   \033[33;1m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\t\033[1;31m[\x1b[38;5;208m+\033[1;31m] \033[33;1m AUTHOR      \x1b[1;97m➤ \033[1;32mU7P4L 1N  
\t\033[1;31m[\x1b[38;5;208m+\033[1;31m] \033[33;1m GITHUB      \x1b[1;97m➤ \033[1;32mU7P4L-IN  
\t\033[1;31m[\x1b[38;5;208m+\033[1;31m] \033[33;1m VERSION     \x1b[1;97m➤ \033[1;32m1.0.5
\t\033[1;31m[\x1b[38;5;208m+\033[1;31m] \033[33;1m TOOL'S NAME \x1b[1;97m➤ \033[1;32mASCII LOGO GENARETOR 
   \033[33;1m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")               

# --------------------[ LOADING ]-----------------#
def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r\t\tLoading... " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print()	
# --------------------[ ADMIN SOCIAL PLATFORM ]-----------------#

def admin():
	os.system('clear')
	loadinglisen()
	os.system('clear')
	print(text_logo)
	print('      \033[1;32m┏━━━\033[97;1m[\033[92;1m1\033[97;1m]\033[1;32m FOLLOW ME GITHUB')
	print('      \033[1;32m┣━━━\033[97;1m[\033[92;1m2\033[97;1m]\033[1;32m JOIN MY FB GROUP ')
	print('      \033[1;32m┣━━━\033[97;1m[\033[92;1m3\033[97;1m]\033[1;32m JOIN MY CHANNEL ')
	print('      \033[1;32m┗━━━\033[97;1m[\033[92;1m0\033[97;1m]\033[38;5;196m BACK TO MAIN MENU')
	print('   \033[33;1m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	shoha = input('  \033[97;1m[\033[34;1m+\033[97;1m]\033[1;32mCHOOSE OPTION>>> ')
	if shoha =='1':
		os.system('xdg-open https://github.com/U7P4L-IN');time.sleep(1)
		admin()
	if  shoha =='2':
		os.system('xdg-open https://www.facebook.com/utpalcyber');time.sleep(1)
		admin()
	if shoha =='3':
		os.system('xdg-open https://t.me/AN0NYM0U5_CY83R');time.sleep(1)
		admin()
	if shoha =='0':
		menu()

def menu():
	os.system('clear')
	loadinglisen()
	os.system('clear')
	#os.system('xdg-open https://github.com/U7P4L-IN')
	os.system('clear')
	print(text_logo)
	print('   \033[1;32m┏━━━\033[1;31m[\033[36;1m01\033[1;31m]\x1b[1;97mCONVERT TEXT TO MULTI-ASCII \033[1;33m[\033[38;5;196m290+FONTS\033[1;33m] ')
	print('   \033[1;32m┣━━━\033[1;31m[\033[36;1m02\033[1;31m]\x1b[1;97mCONVERT TEXT TO SINGLE-ASCII \033[1;33m[\033[38;5;196mRANDOM\033[1;33m] ')
	print('   \033[1;32m┣━━━\033[1;31m[\033[36;1m03\033[1;31m]\x1b[1;97mREPORT FOR BUG ')
	print('   \033[1;32m┗━━━\033[1;31m[\033[36;1m00\033[1;31m]\x1b\033[38;5;197mEXIT PROGRAMMING')
	print('   \033[33;1m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	umo=input(f'     \033[97;1m[\033[34;1m+\033[97;1m]\033[1;32mCHOOSE OPTION :\033[33;1m ')
	if umo in ["01","1"]:
		generator_multi()
	if umo in ["02","2"]:
		generator_single()
	if umo in ["03","3"]:
		admin()
	if umo in ["00","0"]:
		exit('\t\033[33;1mTHANKS FOR USING. HAVE A GOOD DAY ❤')
	else:
		print('\n\n\n      \033[38;5;196mCHOOSE VALID OPTION....!\033[0;97m');time.sleep(1)
		input('      \033[97;1m[\033[92;1m•\033[97;1m]\033[34;1m PRESS ENTER TO RUN AGAIN ');menu()

def generator_multi():
	os.system('clear')
	loadinglisen()
	os.system('clear')
	print(text_logo)
	extra = input("     \033[1;97m[\033[1;92m❯\033[1;97m]\033[36;1m ENTER LOGO NAME \033[0;97m:\033[38;5;196m ")
	if extra=='':
		print('      \033[97;1m[\033[92;1m•\033[97;1m]\033[34;1m REMAIN EMPTY');sleep(2)
		menu()
	_file=open('/sdcard/AC-Logo.txt','w')
	for i in range(292):
		umo = random.choice(['1943____', '3-d', '3x5', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', '6x9', 'a_zooloo', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alphabet', 'aquaplan', 'arrows', 'asc_____', 'ascii___', 'assalt_m', 'asslt__m', 'atc_____', 'atc_gran', 'avatar', 'b_m__200', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'battle_s', 'battlesh', 'baz__bil', 'beer_pub', 'bell', 'big', 'bigchief', 'binary', 'block', 'brite', 'briteb', 'britebi', 'britei', 'broadway', 'bubble', 'bubble__', 'bubble_b', 'bulbhead', 'c1______', 'c2______', 'c_ascii_', 'c_consen', 'calgphy2', 'caligraphy', 'catwalk', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'chartr', 'chartri', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'colossal', 'com_sen_', 'computer', 'contessa', 'contrast', 'convoy__', 'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'd_dragon', 'dcs_bfmo', 'decimal', 'deep_str', 'defleppard', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'double', 'drpepper', 'druid___', 'dwhistled', 'e__fist_', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'etcrvs__', 'f15_____', 'faces_of', 'fair_mea', 'fairligh', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'fender', 'finalass', 'fireing_', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funky_dr', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'ghost_bo', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'greek', 'green_be', 'hades___', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'heroboti', 'hex', 'high_noo', 'hills___', 'hollywood', 'home_pak', 'house_of', 'hypa_bal', 'hyper___', 'inc_raw_', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 'jazmine', 'jerusalem', 'joust___', 'katakana', 'kban', 'kgames_i', 'kik_star', 'krak_out', 'larry3d', 'lazy_jon', 'lcd', 'letterw3', 'lexible_', 'lockergnome', 'madrid', 'marquee', 'mayhem_d', 'mcg_____', 'mike', 'mini', 'mirror', 'mnemonic', 'modern__', 'morse', 'mshebrew210', 'nancyj-underlined', 'nancyj', 'new_asci', 'nfi1____', 'nipples', 'npn_____', 'nvscript', 'ogre', 'os2', 'p_s_h_m_', 'p_skateb', 'pacos_pe', 'pawn_ins', 'pawp', 'peaks', 'pebbles', 'pod_____', 'poison', 'rad_____', 'rally_sp', 'rampage_', 'rastan__', 'rci_____', 'rectangles', 'relief2', 'rev', 'road_rai', 'rockbox_', 'roman', 'roman___', 'rounded', 'rowancap', 'runyc', 'sans', 'sansbi', 'sansi', 'sbookb', 'sbooki', 'script__', 'serifcap', 'shimrod', 'short', 'skate_ro', 'skateord', 'sketch_s', 'slant', 'slide', 'slscript', 'small', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'space_op', 'stampatello', 'standard', 'star_war', 'starwars', 'stellar', 'stencil1', 'stencil2', 'stop', 'street_s', 'subteran', 'tanja', 'tav1____', 'taxi____', 'thin', 'threepoint', 'ticksslant', 'tiles', 'tombstone', 'trek', 'tsalagi', 'tsn_base', 'twin_cob', 'unarmed_', 'univers', 'usa_____', 'usaflag', 'utopia', 'utopiab', 'war_of_w', 'wavy', 'whimsy', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xcour', 'xcourb', 'xcouri', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbook', 'xsbookb', 'xsbookbi', 'xtimes', 'yie-ar__', 'z-pilot_', 'lean', 'letter_w', 'letters', 'linux', 'mad_nurs', 'magic_ma', 'master_o', 'maxfour', 'mig_ally', 'moscow', 'nancyj-fancy', 'notie_ca', 'ntgreek', 'o8', 'octal', 'odel_lak', 'ok_beer_', 'outrun__', 'panther_', 'pepper', 'phonix__', 'platoon2', 'platoon_', 'puffy', 'pyramid', 'r2-d2___', 'rad_phan', 'radical_', 'rainbow_', 'rally_s2', 'raw_recu', 'relief', 'ripper!_', 'rok_____', 'rot13', 'rozzo', 'runic', 'sansb', 'sblood', 'sbook', 'sbookbi', 'script', 'shadow', 'skateroc', 'sm______', 'smisome1', 'spc_demo', 'speed', 'stacey', 'stealth_', 'straight', 'super_te', 't__of_ap', 'tec1____', 'tec_7000', 'tecrvs__', 'tengwar', 'term', 'thick', 'ti_pan__', 'ticks', 'times', 'timesofl', 'tinker-toy', 'tomahawk', 'top_duck', 'trashman', 'triad_st', 'ts1_____', 'tsm_____', 'tty', 'ttyb', 'tubular', 'twopoint', 'type_set', 'ucf_fan_', 'ugalympi', 'usa_pq__', 'utopiabi', 'utopiai', 'vortron_', 'weird', 'xbrite', 'xchartri', 'xcourbi', 'xhelv', 'xsbooki', 'xtty', 'xttyb', 'yie_ar_k', 'zig_zag_', 'zone7___'])
		gen_qsr = pyfiglet.figlet_format(extra,font=umo)
		_file.write(f"\t\t\t U7P4L LOGO NO : {i} \n------------------------------------------------------------\n{gen_qsr}------------------------------------------------------------\n")
	print("     \033[1;97m[\033[1;92m❯\033[1;97m]\033[36;1m GENERATING FONTS ........");sleep(2.5)
	print(f"     \033[1;97m[\033[1;92m❯\033[1;97m]\033[36;1m COMPLETED FONTS SAVED\033[0m:\033[1;92m/sdcard/AC-Logo.txt")
	ope=input("       \033[97;1m[\033[92;1m•\033[97;1m]\033[34;1m YOU WANT TO OPEN FILE y/n ? ")
	if ope in ['n','N','no','No']:
		menu()
	if ope in ['y','Yes','Y','yes']:
		os.system('termux-open /sdcard/AC-Logo.txt')
		input("      \033[97;1m[\033[92;1m•\033[97;1m]\033[34;1m PRESS ENTER TO GO BACK ")
		menu()
	else:
		os.system('termux-open /sdcard/logo.txt')

def generator_single():
	os.system('clear')
	loadinglisen()
	os.system('clear')
	print(text_logo)
	extra = input("     \033[1;97m[\033[1;92m❯\033[1;97m]\033[36;1m ENTER LOGO NAME \033[0;97m:\033[38;5;196m ")
	umo = random.choice(['1943____', '3-d', '3x5', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', '6x9', 'a_zooloo', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alphabet', 'aquaplan', 'arrows', 'asc_____', 'ascii___', 'assalt_m', 'asslt__m', 'atc_____', 'atc_gran', 'avatar', 'b_m__200', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'battle_s', 'battlesh', 'baz__bil', 'beer_pub', 'bell', 'big', 'bigchief', 'binary', 'block', 'brite', 'briteb', 'britebi', 'britei', 'broadway', 'bubble', 'bubble__', 'bubble_b', 'bulbhead', 'c1______', 'c2______', 'c_ascii_', 'c_consen', 'calgphy2', 'caligraphy', 'catwalk', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'chartr', 'chartri', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'colossal', 'com_sen_', 'computer', 'contessa', 'contrast', 'convoy__', 'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'd_dragon', 'dcs_bfmo', 'decimal', 'deep_str', 'defleppard', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'double', 'drpepper', 'druid___', 'dwhistled', 'e__fist_', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'etcrvs__', 'f15_____', 'faces_of', 'fair_mea', 'fairligh', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'fender', 'finalass', 'fireing_', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funky_dr', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'ghost_bo', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'greek', 'green_be', 'hades___', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'heroboti', 'hex', 'high_noo', 'hills___', 'hollywood', 'home_pak', 'house_of', 'hypa_bal', 'hyper___', 'inc_raw_', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 'jazmine', 'jerusalem', 'joust___', 'katakana', 'kban', 'kgames_i', 'kik_star', 'krak_out', 'larry3d', 'lazy_jon', 'lcd', 'letterw3', 'lexible_', 'lockergnome', 'madrid', 'marquee', 'mayhem_d', 'mcg_____', 'mike', 'mini', 'mirror', 'mnemonic', 'modern__', 'morse', 'mshebrew210', 'nancyj-underlined', 'nancyj', 'new_asci', 'nfi1____', 'nipples', 'npn_____', 'nvscript', 'ogre', 'os2', 'p_s_h_m_', 'p_skateb', 'pacos_pe', 'pawn_ins', 'pawp', 'peaks', 'pebbles', 'pod_____', 'poison', 'rad_____', 'rally_sp', 'rampage_', 'rastan__', 'rci_____', 'rectangles', 'relief2', 'rev', 'road_rai', 'rockbox_', 'roman', 'roman___', 'rounded', 'rowancap', 'runyc', 'sans', 'sansbi', 'sansi', 'sbookb', 'sbooki', 'script__', 'serifcap', 'shimrod', 'short', 'skate_ro', 'skateord', 'sketch_s', 'slant', 'slide', 'slscript', 'small', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'space_op', 'stampatello', 'standard', 'star_war', 'starwars', 'stellar', 'stencil1', 'stencil2', 'stop', 'street_s', 'subteran', 'tanja', 'tav1____', 'taxi____', 'thin', 'threepoint', 'ticksslant', 'tiles', 'tombstone', 'trek', 'tsalagi', 'tsn_base', 'twin_cob', 'unarmed_', 'univers', 'usa_____', 'usaflag', 'utopia', 'utopiab', 'war_of_w', 'wavy', 'whimsy', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xcour', 'xcourb', 'xcouri', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbook', 'xsbookb', 'xsbookbi', 'xtimes', 'yie-ar__', 'z-pilot_', 'lean', 'letter_w', 'letters', 'linux', 'mad_nurs', 'magic_ma', 'master_o', 'maxfour', 'mig_ally', 'moscow', 'nancyj-fancy', 'notie_ca', 'ntgreek', 'o8', 'octal', 'odel_lak', 'ok_beer_', 'outrun__', 'panther_', 'pepper', 'phonix__', 'platoon2', 'platoon_', 'puffy', 'pyramid', 'r2-d2___', 'rad_phan', 'radical_', 'rainbow_', 'rally_s2', 'raw_recu', 'relief', 'ripper!_', 'rok_____', 'rot13', 'rozzo', 'runic', 'sansb', 'sblood', 'sbook', 'sbookbi', 'script', 'shadow', 'skateroc', 'sm______', 'smisome1', 'spc_demo', 'speed', 'stacey', 'stealth_', 'straight', 'super_te', 't__of_ap', 'tec1____', 'tec_7000', 'tecrvs__', 'tengwar', 'term', 'thick', 'ti_pan__', 'ticks', 'times', 'timesofl', 'tinker-toy', 'tomahawk', 'top_duck', 'trashman', 'triad_st', 'ts1_____', 'tsm_____', 'tty', 'ttyb', 'tubular', 'twopoint', 'type_set', 'ucf_fan_', 'ugalympi', 'usa_pq__', 'utopiabi', 'utopiai', 'vortron_', 'weird', 'xbrite', 'xchartri', 'xcourbi', 'xhelv', 'xsbooki', 'xtty', 'xttyb', 'yie_ar_k', 'zig_zag_', 'zone7___'])
	gen_qsr = pyfiglet.figlet_format(extra,font=umo)
	print(f"\n{gen_qsr}\n")
	input("      \033[97;1m[\033[92;1m•\033[97;1m]\033[34;1m PRESS ENTER TO GO BACK ")
	menu()

menu()
