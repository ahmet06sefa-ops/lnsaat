from pathlib import Path
from html import escape
p=Path('/home/user/ince-isler-web/public/assets')
head='''<svg xmlns="http://www.w3.org/2000/svg" width="1376" height="768" viewBox="0 0 1376 768"><defs><pattern id="paper" width="35" height="35" patternUnits="userSpaceOnUse"><circle cx="4" cy="5" r="1" fill="#b8ad98" opacity=".2"/><circle cx="22" cy="24" r=".8" fill="#afa994" opacity=".17"/></pattern><pattern id="mesh" width="17" height="17" patternUnits="userSpaceOnUse"><path d="M0 0H17M0 0V17" fill="none" stroke="#a1ab9b" stroke-width="2"/></pattern><pattern id="fiber" width="50" height="37" patternUnits="userSpaceOnUse"><path d="M-12 27Q10 1 26 21T66 14M-8 5Q12 28 31 9T61 18" fill="none" stroke="#b89760" stroke-width="4" opacity=".45"/></pattern><pattern id="wood" width="120" height="60" patternUnits="userSpaceOnUse"><path d="M0 10q35-10 64 0t56 0M0 35q24-10 65 0t55 0" fill="none" stroke="#a98761" stroke-width="2" opacity=".45"/></pattern><filter id="shadow"><feGaussianBlur stdDeviation="10"/></filter></defs><rect width="1376" height="768" fill="#f6f2e7"/><rect width="1376" height="768" fill="url(#paper)"/><ellipse cx="680" cy="645" rx="445" ry="45" fill="#5c6c57" opacity=".08" filter="url(#shadow)"/>'''
style='font-family="Arial, sans-serif"'
def txt(x,y,text,size=26,color='#52695b',weight=700,anchor='start',extra=''):
 return f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{escape(text)}</text>'
def save(name, inner, eyebrow, bottom):
 s=head+txt(65,75,eyebrow,19,'#be7151',700,extra='letter-spacing="3"')+inner+txt(65,712,bottom,19,'#8a988a',700,extra='letter-spacing="1.5"')+'</svg>'
 (p/f'mat-{name}.svg').write_text(s,encoding='utf8')
def bag(label, fill='#dbbc91', powder='#f4eee2'):
 return f'''<path d="M451 212Q461 192 486 198H743Q765 190 781 213L806 584Q808 611 780 616H440Q414 610 417 581Z" fill="{fill}" stroke="#887c68" stroke-width="5"/><path d="M451 212Q471 230 486 219Q511 230 530 217Q556 231 575 216Q599 230 620 216Q643 230 666 216Q687 229 710 216Q745 231 781 213" fill="{powder}" stroke="#887c68" stroke-width="5"/><path d="M463 300Q613 279 761 300L774 480Q620 499 452 480Z" fill="#f9f6eb" opacity=".88"/><path d="M464 502Q610 520 768 503" stroke="#9a907a" stroke-width="3" fill="none"/>{txt(613,380,label,29,'#617466',700,'middle')}{txt(613,420,'TOZ ÜRÜN',18,'#a68769',700,'middle',extra='letter-spacing="3"')}<path d="M845 550l150-60 17 35-147 62z" fill="#a8b9ac" stroke="#62756b" stroke-width="4"/><path d="M974 495l62-42 12 29-49 42z" fill="#936847" stroke="#6a584b" stroke-width="3"/>'''
save('saten',bag('SATEN ALÇI','#e0c6a6'),'YÜZEY DÜZELTME','PERDAH ALÇISI  /  TEMSİLİ ÜRÜN')
save('cimento',bag('ÇİMENTO SIVA','#c8b49b','#c9c5b9'),'SIVA GRUBU','ÇİMENTO ESASLI  /  TEMSİLİ ÜRÜN')
# Boards: front plane, core edge and paper face; unique color coding purely as example
for name,label,color in [('nemli-levha','NEME DAYANIMLI','#b2c8b1'),('yangin-levha','YANGIN PERFORMANSI','#d7b4aa')]:
 b=f'''<path d="M240 425L825 205 1131 329 544 551Z" fill="{color}" stroke="#74877b" stroke-width="5"/><path d="M544 551l587-222v37L544 589Z" fill="#eee8d9" stroke="#848d80" stroke-width="4"/><path d="M240 425l304 126v38L240 462Z" fill="#e7e3d5" stroke="#848d80" stroke-width="4"/><path d="M260 424L826 212 1104 329" fill="none" stroke="#dae6d6" stroke-width="3"/><circle cx="365" cy="393" r="7" fill="#7a9180"/><circle cx="405" cy="378" r="7" fill="#7a9180"/>{txt(685,407,label,27,'#466054',700,'middle')}'''
 save(name,b,'ALÇI LEVHA','ÖRNEK RENK  /  TEK BAŞINA ÜRÜN TANIMI DEĞİLDİR')
# profile cross sections, intentionally open channel
for name,title,lips in [('u-profil','U PROFİL',False),('c-profil','C PROFİL',True),('tavan-profil','TAVAN C PROFİLİ',True)]:
 channel='M 378 217 L 378 522 L 829 522 L 829 217' if not lips else 'M 448 277 L 448 217 L 378 217 L 378 522 L 829 522 L 829 217 L 759 217 L 759 277'
 b=f'''<rect x="250" y="150" width="700" height="460" rx="4" fill="#e8ece5" stroke="#d3ddd1" stroke-width="3"/><path d="{channel}" fill="none" stroke="#8b9993" stroke-width="31" stroke-linejoin="round" stroke-linecap="square"/><path d="{channel}" fill="none" stroke="#f8faf3" stroke-width="3" stroke-linejoin="round" opacity=".85"/>{txt(1035,324,'KESİT',26,'#587161',700,'middle')}{txt(1035,367,'AÇIK',22,'#92a39a',700,'middle')}{txt(1035,401,'KANAL',22,'#92a39a',700,'middle')}{txt(604,586,title,27,'#486152',700,'middle')}'''
 save(name,b,'METAL İSKELET','KESİT ŞEMASI  /  ÖLÇEKSİZ')
# corner bead with mesh
b='''<path d="M555 180L720 219V596L555 552Z" fill="#d5e0d2" stroke="#708777" stroke-width="5"/><path d="M720 219L835 169V547L720 596Z" fill="#bbcbbc" stroke="#708777" stroke-width="5"/><path d="M280 245L553 180V551L280 617Z" fill="url(#mesh)" stroke="#96a89a" stroke-width="4"/><path d="M835 169L1080 245V615L835 547Z" fill="url(#mesh)" stroke="#96a89a" stroke-width="4"/><path d="M718 223V589" stroke="#f6f5e8" stroke-width="9"/>'''
save('kose',b,'KÖŞE GÜÇLENDİRME','FİLELİ KÖŞE PROFİLİ  /  TEMSİLİ')
# screw inclined, no dimension claim
b='''<g transform="translate(260 520) rotate(-18)"><path d="M25 38h540l120 20-120 20H25Q-18 58 25 38Z" fill="#7e9188" stroke="#566d62" stroke-width="5"/><path d="M30 34q-62 24 0 48" fill="#d2dad1" stroke="#566d62" stroke-width="5"/><path d="M30 57h-37m18-18v35" fill="none" stroke="#536b5d" stroke-width="6"/><g stroke="#d9e5dc" stroke-width="6">''' + ''.join(f'<path d="M{x} 41l-13 34"/>' for x in range(75,560,25))+'''</g></g>'''
save('vida',b,'BAĞLANTI ELEMANI','HAVŞA BAŞLI LEVHA VİDASI  /  TEMSİLİ')
# drywall joint compound
b=bag('DERZ ALÇISI','#dec7a4')+'''<path d="M230 505l160-56v82l-160 58zM895 442l161-55v82l-161 57z" fill="#e7ebe0" stroke="#9aa99b" stroke-width="4"/><path d="M870 448v80" stroke="#c96d4f" stroke-width="7" stroke-dasharray="12 10"/>'''
save('alci-derz',b,'ALÇI LEVHA BİRLEŞİMİ','KARO DERZİYLE KARIŞTIRMA  /  TEMSİLİ')
# paper and mesh tapes: single spool with visible paper ribbon
b='''<ellipse cx="536" cy="368" rx="161" ry="151" fill="#ddd6c6" stroke="#8e988b" stroke-width="5"/><path d="M536 217h110c89 0 161 68 161 151s-72 151-161 151H536c89 0 161-68 161-151s-72-151-161-151Z" fill="#ede7d9" stroke="#8e988b" stroke-width="5"/><ellipse cx="646" cy="368" rx="161" ry="151" fill="#f5f1e6" stroke="#8e988b" stroke-width="5"/><ellipse cx="646" cy="368" rx="57" ry="55" fill="#a8b5a6" stroke="#7d9081" stroke-width="4"/><path d="M760 485L1030 587l60-30-285-112" fill="#e5e0d0" stroke="#8e988b" stroke-width="5"/><path d="M866 510l138 51" stroke="#b5b5a4" stroke-width="3"/>'''
save('derz-bandi',b,'ALÇI LEVHA AKSESUARI','KÂĞIT VEYA FİLE BANT  /  TEMSİLİ RULO')
# mineral wool batt
b='''<path d="M294 329L777 188l302 120-483 141Z" fill="#dfd0a7" stroke="#a99976" stroke-width="5"/><path d="M596 449l483-141v138L596 588Z" fill="#c7b58a" stroke="#a99976" stroke-width="5"/><path d="M294 329l302 120v139L294 466Z" fill="#d4c396" stroke="#a99976" stroke-width="5"/><path d="M294 329L777 188l302 120-483 141ZM596 449l483-141v138L596 588ZM294 329l302 120v139L294 466Z" fill="url(#fiber)" opacity=".9"/>'''
save('mineral-yun',b,'ARA BÖLME DOLGUSU','MİNERAL YÜN LEVHA  /  TEMSİLİ')
# porcelain
b='''<path d="M256 373L710 209l424 160-455 164Z" fill="#d7ded5" stroke="#849388" stroke-width="5"/><path d="M679 533l455-164v54L679 587Z" fill="#bbc5bd" stroke="#849388" stroke-width="5"/><path d="M256 373l423 160v54L256 428Z" fill="#e9e9dd" stroke="#849388" stroke-width="5"/><path d="M342 369q125-18 212 30t237 44M617 265q30 56 128 73t208 69" fill="none" stroke="#aebcad" stroke-width="6" opacity=".7"/>'''
save('porselen',b,'YER VE DUVAR KAPLAMASI','PORS ELEN KARO  /  TEMSİLİ ÜRÜN'.replace('PORS ELEN','PORSELEN'))
# natural stone slab with recognizable veins
b='''<path d="M338 225L851 188 1005 272 492 313Z" fill="#f0ece0" stroke="#9ba69a" stroke-width="5"/><path d="M492 313l513-41v265L492 578Z" fill="#e8e7dc" stroke="#9ba69a" stroke-width="5"/><path d="M338 225l154 88v265l-154-91Z" fill="#d3d5c9" stroke="#9ba69a" stroke-width="5"/><path d="M515 358q70-43 125 21t125 18q70-31 193 55M550 510q55-68 119-33t159-42" fill="none" stroke="#abb6aa" stroke-width="7" opacity=".8"/>'''
save('tas',b,'DOĞAL TAŞ','DOĞAL DAMAR  /  ÖLÇÜ VE YÜZEY ÜRÜNE GÖRE')
# spacer
b='''<path d="M280 222h315v145H280zM752 222h315v145H752zM280 478h315v145H280zM752 478h315v145H752z" fill="#e5e8dd" stroke="#a6b3a4" stroke-width="4"/><path d="M635 283h83v95h95v83h-95v95h-83v-95h-95v-83h95z" fill="#c8704e" stroke="#9f593e" stroke-width="5"/><path d="M594 420H752M676 367V478" stroke="#faf7ec" stroke-width="3" stroke-dasharray="10 8"/>'''
save('derz-artisi',b,'KARO AKSESUARI','DERZ ARTISI  /  SEÇİLEN ARALIĞI KORUR')
# epoxy products
b='''<path d="M387 303h350l-22 270q-6 43-153 43T410 573Z" fill="#d9e4d9" stroke="#879b8c" stroke-width="5"/><ellipse cx="562" cy="303" rx="175" ry="48" fill="#eef1e6" stroke="#879b8c" stroke-width="5"/><path d="M454 269q-2-103 108-104t110 104" fill="none" stroke="#8fa090" stroke-width="5"/><rect x="453" y="360" width="218" height="114" fill="#faf7eb" stroke="#d4ddd2" stroke-width="3"/>'''+txt(562,405,'EPOKSİ',25,'#526c5b',700,'middle')+txt(562,442,'DERZ DOLGU',19,'#a07258',700,'middle')+'''<rect x="814" y="395" width="75" height="177" rx="5" fill="#c2d1bf" stroke="#8fa18e" stroke-width="4"/><rect x="908" y="395" width="75" height="177" rx="5" fill="#e0cbb2" stroke="#a69680" stroke-width="4"/>'''+txt(850,500,'A',28,'#587466',700,'middle')+txt(945,500,'B',28,'#8e6d58',700,'middle')
save('epoksi',b,'KİMYASAL DAYANIM','BİLEŞEN SAYISI ÜRÜNE GÖRE DEĞİŞİR  /  TEMSİLİ')
# waterproof corner tape
b='''<path d="M340 234h546v254H340z" fill="#dbe4dc" stroke="#9bada0" stroke-width="5"/><path d="M340 488h546l139 126H201z" fill="#e7e9dd" stroke="#9bada0" stroke-width="5"/><path d="M340 453h546v36H340z" fill="#7c9ca7" stroke="#627f8d" stroke-width="4"/><path d="M340 488h546l42 39H298z" fill="#a4c2c4" stroke="#627f8d" stroke-width="4"/><path d="M340 488h546" stroke="#f8f6eb" stroke-width="3"/>'''
save('pah-bandi',b,'SU YALITIMI AKSESUARI','DUVAR–ZEMİN KÖŞE BANDI  /  TEMSİLİ')
# membrane
b='''<path d="M337 346L798 241l288 116-465 106Z" fill="#8eb0b6" stroke="#678691" stroke-width="5"/><path d="M621 463l465-106v52L621 516Z" fill="#7398a1" stroke="#678691" stroke-width="4"/><ellipse cx="467" cy="318" rx="145" ry="100" fill="#c9dddd" stroke="#688892" stroke-width="5"/><path d="M467 218h175c80 0 145 45 145 100s-65 100-145 100H467c80 0 145-45 145-100s-65-100-145-100Z" fill="#9ebfc1" stroke="#688892" stroke-width="5"/><ellipse cx="642" cy="318" rx="145" ry="100" fill="#b3cfcf" stroke="#688892" stroke-width="5"/><ellipse cx="642" cy="318" rx="52" ry="37" fill="#f1eee1" stroke="#688892" stroke-width="4"/>'''
save('membran',b,'SU YALITIMI','RULO MEMBRAN  /  BİNDİRME ÜRÜN SİSTEMİNE GÖRE')
# primer bucket and roller
b='''<path d="M385 295h350l-20 283q-5 38-155 38t-155-38z" fill="#e1e7d9" stroke="#94a496" stroke-width="5"/><ellipse cx="560" cy="295" rx="175" ry="45" fill="#f8f7eb" stroke="#94a496" stroke-width="5"/><rect x="448" y="364" width="223" height="103" fill="#f9f7ed" stroke="#cfd8cd" stroke-width="3"/>'''+txt(560,425,'ASTAR',29,'#557160',700,'middle')+'''<rect x="857" y="243" width="140" height="185" rx="24" fill="#c8d5c6" stroke="#8b9b8d" stroke-width="5"/><path d="M925 430v64q0 22-35 22h-48v72" fill="none" stroke="#8b9b8d" stroke-width="10"/><path d="M841 571v71" stroke="#bb7956" stroke-width="22" stroke-linecap="round"/>'''
save('astar',b,'YÜZEY HAZIRLIĞI','ASTAR  /  UYGUNLUK YÜZEYE VE BOYAYA GÖRE')
# putty
b='''<path d="M400 306h350l-20 273q-4 42-155 42t-155-42z" fill="#e8e3d7" stroke="#9a9d8f" stroke-width="5"/><ellipse cx="575" cy="306" rx="175" ry="45" fill="#f8f5e9" stroke="#9a9d8f" stroke-width="5"/><rect x="465" y="375" width="220" height="100" fill="#faf8ef" stroke="#d9d9cd" stroke-width="3"/>'''+txt(575,433,'MACUN',28,'#577160',700,'middle')+'''<path d="M825 502l201-59-10 66-181 55z" fill="#bbc8be" stroke="#7e9185" stroke-width="5"/><path d="M929 459l26-73 28 8-18 57" fill="#b98762" stroke="#8f725d" stroke-width="5"/>'''
save('macun',b,'BOYA ÖNCESİ DÜZELTME','HAZIR YÜZEY MACUNU  /  TEMSİLİ')
# underlay roll, plank above
b='''<path d="M260 487L782 360l285 110-522 127Z" fill="#c5d6c9" stroke="#91aa98" stroke-width="5"/><path d="M340 396L762 290l229 85-423 107Z" fill="#d0b18a" stroke="#9b8064" stroke-width="5"/><path d="M340 396L762 290l229 85-423 107Z" fill="url(#wood)"/><path d="M568 482l423-107v35L568 518Z" fill="#aa8d6f" stroke="#927b62" stroke-width="4"/><ellipse cx="370" cy="494" rx="106" ry="74" fill="#dbe5d8" stroke="#91aa98" stroke-width="5"/><ellipse cx="370" cy="494" rx="35" ry="25" fill="#f4f2e7" stroke="#91aa98" stroke-width="4"/>'''
save('silte',b,'ZEMİN ALTLIĞI','ŞİLTE + KAPLAMA  /  MALZEME UYUMU KONTROL EDİLİR')
# skirting
b='''<path d="M260 170h750v365H260z" fill="#e5e8dd" stroke="#a3b0a1" stroke-width="4"/><path d="M260 535h750l150 100H122z" fill="#d6c4a9" stroke="#a3a796" stroke-width="4"/><path d="M260 464h750v71H260z" fill="#f6f1e5" stroke="#9ca99b" stroke-width="5"/><path d="M260 464h750" stroke="#bdc9bb" stroke-width="4"/>'''
save('supurgelik',b,'ZEMİN BİTİŞİ','SÜPÜRGELİK  /  KAPLAMA HAREKETİNİ KİLİTLEMEZ')
# door
b='''<path d="M410 135h487v500H410z" fill="#d3c5ac" stroke="#8e8b77" stroke-width="5"/><path d="M448 161h411v474H448z" fill="#f0e8da" stroke="#8e8b77" stroke-width="5"/><path d="M476 188h360v443H476z" fill="#dcc7aa" stroke="#9b8a71" stroke-width="5"/><path d="M476 188h360v443H476z" fill="url(#wood)"/><path d="M783 405h-38" stroke="#607468" stroke-width="10" stroke-linecap="round"/><circle cx="790" cy="405" r="10" fill="#607468"/><path d="M410 135h487v500h-38V171H448v464h-38z" fill="#c4b69e" stroke="#8e8b77" stroke-width="4"/>'''
save('kapi',b,'KAPI SİSTEMİ','KANAT + KASA  /  DUVAR BOŞLUĞU AYRI ÖLÇÜLÜR')
# foam can
b='''<path d="M510 245h223l-11 331q0 40-101 40t-100-40z" fill="#dfc5a5" stroke="#9a8d79" stroke-width="5"/><ellipse cx="621" cy="244" rx="111" ry="35" fill="#f1e6d5" stroke="#9a8d79" stroke-width="5"/><path d="M594 212v-43h55v43" fill="#9baaa0" stroke="#7b8d82" stroke-width="4"/><path d="M645 176l157-67" stroke="#6c8174" stroke-width="12" stroke-linecap="round"/><rect x="543" y="337" width="157" height="113" fill="#f8f3e6" stroke="#e2d8c6" stroke-width="3"/>'''+txt(621,382,'MONTAJ',21,'#647969',700,'middle')+txt(621,418,'KÖPÜĞÜ',21,'#647969',700,'middle')
save('kopuk',b,'KASA MONTAJI','POLİÜRETAN KÖPÜK  /  TEK BAŞINA SABİTLEME DEĞİLDİR')
print('created',len(list(p.glob('mat-*.svg'))),'vector illustrations')
# Distinct material packages: one-component powder vs two-component powder + liquid.
b1=bag('1K YALITIM','#cdbfa4','#c6c9bd')+'''<path d="M848 452h175l-12 126q-3 23-77 23t-75-23z" fill="#b4cfd1" stroke="#74949a" stroke-width="4"/><ellipse cx="935" cy="452" rx="87" ry="24" fill="#d8e7e1" stroke="#74949a" stroke-width="4"/>'''
save('yalitim-1k',b1,'TEK BİLEŞENLİ YALITIM','TOZ ÜRÜN + SU  /  ÜRÜN TALİMATINA GÖRE')
b2='''<path d="M323 244q8-25 36-25h253q28 0 35 25l20 332q3 34-27 38H334q-32-3-29-38z" fill="#d4bf9e" stroke="#8d836f" stroke-width="5"/><path d="M323 244q160 18 324 0" fill="none" stroke="#a99b85" stroke-width="5"/><rect x="362" y="330" width="245" height="123" fill="#f9f6ea"/>'''+txt(485,384,'TOZ BİLEŞEN',26,'#627565',700,'middle')+txt(485,425,'ÇİMENTO ESASLI',17,'#a07b60',700,'middle')+'''<path d="M782 226h75v-50h69v50h35l42 52v302q0 30-30 30H752q-30 0-30-30V279q0-26 20-42z" fill="#c4d4ca" stroke="#83998a" stroke-width="5"/><rect x="787" y="287" width="124" height="80" rx="17" fill="#f5f4e8" stroke="#83998a" stroke-width="5"/><rect x="764" y="415" width="194" height="93" fill="#f8f6ea"/>'''+txt(861,470,'SIVI BİLEŞEN',23,'#577061',700,'middle')
save('yalitim-2k',b2,'İKİ BİLEŞENLİ YALITIM','TOZ + SIVI  /  ORAN ÜRÜN FÖYÜNDEN')
