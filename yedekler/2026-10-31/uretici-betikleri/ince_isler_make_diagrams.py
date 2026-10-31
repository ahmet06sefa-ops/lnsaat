from pathlib import Path
P=Path('/home/user/ince-isler-web/public/assets');P.mkdir(exist_ok=True)
head='''<svg xmlns="http://www.w3.org/2000/svg" width="1376" height="768" viewBox="0 0 1376 768" role="img">
<defs>
 <pattern id="paper" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="3" cy="4" r=".8" fill="#b4ad9d" opacity=".15"/><circle cx="19" cy="15" r=".7" fill="#b4ad9d" opacity=".1"/></pattern>
 <pattern id="brick" width="82" height="46" patternUnits="userSpaceOnUse"><rect width="82" height="46" fill="#c99171"/><path d="M0 0h82M0 23h82M0 46h82M41 0v23M0 23v23M82 23v23" fill="none" stroke="#7d6d5a" stroke-width="2" opacity=".65"/></pattern>
 <pattern id="mesh" width="22" height="22" patternUnits="userSpaceOnUse"><rect width="22" height="22" fill="#b6c8b5"/><path d="M0 0L22 22M22 0L0 22" stroke="#778f7d" stroke-width="1" opacity=".75"/></pattern>
 <pattern id="grain" width="55" height="38" patternUnits="userSpaceOnUse"><path d="M0 7q16-7 29 0t26 0M0 25q15-6 26 0t29 0" fill="none" stroke="#d0b08b" stroke-width="1.5" opacity=".5"/></pattern>
 <filter id="shadow"><feGaussianBlur stdDeviation="9"/></filter>
</defs>
<rect width="1376" height="768" fill="#f6f3e8"/><rect width="1376" height="768" fill="url(#paper)"/>
'''
end='</svg>'
art={}
art['olcum']='''
<!-- An unfinished wall, reference laser, straightedge, plumb and record book -->
<ellipse cx="685" cy="682" rx="560" ry="28" fill="#657b65" opacity=".1" filter="url(#shadow)"/>
<path d="M177 110 L1130 110 L1130 605 L177 605 Z" fill="#ebe8d9" stroke="#817c6d" stroke-width="4"/>
<path d="M177 605H1130L1270 700H85Z" fill="#dedacb" stroke="#817c6d" stroke-width="4"/>
<path d="M177 355H1130" fill="none" stroke="#c46748" stroke-width="4" stroke-dasharray="17 10" opacity=".85"/>
<path d="M930 120V605" fill="none" stroke="#c46748" stroke-width="4" stroke-dasharray="15 9"/>
<circle cx="930" cy="155" r="11" fill="#f5efe0" stroke="#c46748" stroke-width="4"/>
<path d="M920 605h20l-10 16z" fill="#b96b4a"/>
<g transform="translate(475 276)"><rect width="390" height="35" rx="3" fill="#b7c6b3" stroke="#526755" stroke-width="4"/><path d="M28 0v14m30-14v9m30-9v14m30-14v9m30-9v14m30-14v9m30-9v14m30-14v9m30-9v14m30-14v9m30-9v14m30-14v9" stroke="#526755" stroke-width="2"/><rect x="174" y="9" width="42" height="17" rx="8" fill="#eef1db" stroke="#526755" stroke-width="2"/><circle cx="194" cy="17" r="5" fill="#d9b379"/></g>
<g transform="translate(250 474)"><path d="M70 64L14 188M70 64l59 124M70 64v124" stroke="#657866" stroke-width="7"/><rect x="38" y="5" width="64" height="62" rx="8" fill="#c96c4c" stroke="#624f40" stroke-width="4"/><circle cx="70" cy="34" r="16" fill="#dce9dc" stroke="#526755" stroke-width="4"/></g>
<g transform="translate(1012 615) rotate(-6)"><rect width="150" height="72" rx="4" fill="#faf8ee" stroke="#7b8171" stroke-width="4"/><path d="M22 22h99M22 36h85M22 50h96" stroke="#a7b7a3" stroke-width="4"/><path d="M132 -8l28 3-35 86-18-7z" fill="#c77955" stroke="#6d6958" stroke-width="3"/></g>
<g transform="translate(937 591)"><rect width="64" height="56" rx="10" fill="#c36a4d" stroke="#6d5949" stroke-width="4"/><rect x="12" y="10" width="36" height="24" rx="3" fill="#e9eadc" stroke="#6d5949" stroke-width="3"/><path d="M61 27h93" stroke="#bdad79" stroke-width="7"/></g>
'''
art['malzeme']='''
<!-- Organised building-material delivery on a dry pallet -->
<ellipse cx="688" cy="681" rx="510" ry="25" fill="#657b65" opacity=".1" filter="url(#shadow)"/>
<path d="M280 627h820l35 43H245z" fill="#b58a66" stroke="#796b58" stroke-width="4"/><path d="M307 665v32m160-32v32m420-32v32m165-32v32" stroke="#796b58" stroke-width="10"/>
<g stroke="#867968" stroke-width="4"><path d="M312 238h292v178H312z" fill="#d8c19e"/><path d="M312 238l33-32h260l-1 32z" fill="#e9d4b0"/><path d="M604 238l36-24v177l-36 25z" fill="#c7aa86"/><path d="M330 428h292v177H330z" fill="#d8c19e"/><path d="M330 428l33-32h260l-1 32z" fill="#e9d4b0"/><path d="M622 428l35-24v176l-35 25z" fill="#c7aa86"/></g>
<g fill="#f8f4e8" stroke="#9d9b88" stroke-width="3"><rect x="370" y="280" width="166" height="100" rx="4"/><rect x="388" y="470" width="166" height="100" rx="4"/></g>
<g stroke="#7c927d" stroke-width="5"><path d="M392 302h114m-114 19h75m-75 19h103m-103 18h68"/><path d="M410 492h112m-112 19h72m-72 19h101m-101 18h68"/></g>
<g transform="translate(700 266)"><path d="M0 52Q0 28 28 28h150q27 0 27 24v244q0 24-27 24H28Q0 320 0 296z" fill="#e9e4d2" stroke="#7b8070" stroke-width="5"/><ellipse cx="102" cy="29" rx="102" ry="25" fill="#a9bca7" stroke="#7b8070" stroke-width="5"/><path d="M26 95h154v145H26z" fill="#faf8ec" stroke="#a6a995" stroke-width="3"/><path d="M47 121h112M47 143h84M47 165h100M47 188h75M47 209h96" stroke="#a5b4a0" stroke-width="5"/></g>
<g transform="translate(935 354)"><path d="M0 44Q0 22 23 22h107q23 0 23 22v194q0 22-23 22H23Q0 260 0 238z" fill="#c8d3bf" stroke="#7b8070" stroke-width="4"/><ellipse cx="76" cy="22" rx="76" ry="20" fill="#e7eee0" stroke="#7b8070" stroke-width="4"/><rect x="25" y="79" width="100" height="83" rx="3" fill="#f9f7eb" stroke="#b4b9a7" stroke-width="3"/><path d="M38 100h74M38 118h53M38 137h64" stroke="#9cac9a" stroke-width="4"/></g>
<path d="M255 176Q688 83 1115 176" fill="none" stroke="#a8bca9" stroke-width="5" stroke-dasharray="16 12"/>
'''
art['dolap']='''
<!-- One kitchen wall with upper and lower cabinets, worktop and services -->
<path d="M180 100h1015v525H180z" fill="#ece9db" stroke="#8b8878" stroke-width="4"/><path d="M180 625h1015l95 75H91z" fill="#ded9c9" stroke="#8b8878" stroke-width="4"/>
<path d="M205 170h95v355h-95M1145 170h-95v355h95" fill="none" stroke="#c17a56" stroke-width="4" stroke-dasharray="13 10"/>
<g stroke="#776c59" stroke-width="4"><rect x="328" y="147" width="670" height="220" fill="#ddc5a4"/><path d="M344 164h200v187H344zM560 164h203v187H560zM780 164h201v187H780z" fill="#e8d5ba"/><path d="M533 223v54m238-54v54m193-54v54" stroke="#758777" stroke-width="6"/></g>
<g fill="#627b69" stroke="#f2eee0" stroke-width="3"><circle cx="348" cy="157" r="12"/><circle cx="977" cy="157" r="12"/></g>
<path d="M290 430h750l26 35H268z" fill="#f8f4e8" stroke="#817e6e" stroke-width="4"/><rect x="292" y="465" width="750" height="180" fill="#d8bea0" stroke="#817260" stroke-width="4"/>
<path d="M310 481h200v145H310zM525 481h212v145H525zM752 481h272v145H752z" fill="#e8d2b5" stroke="#817260" stroke-width="3"/><path d="M492 528v44m227-44v44m287-44v44" stroke="#758777" stroke-width="6"/>
<ellipse cx="830" cy="438" rx="103" ry="19" fill="#b8cbc1" stroke="#718578" stroke-width="4"/><path d="M865 427v-48q0-36-31-36t-31 36" fill="none" stroke="#6a7e70" stroke-width="8"/><circle cx="803" cy="380" r="6" fill="#c96e4e"/>
<path d="M804 474v65q0 20 20 20h37v49" fill="none" stroke="#9bb9bc" stroke-width="6" stroke-dasharray="10 7"/><path d="M722 429h240" stroke="#b88b67" stroke-width="3"/>
'''
art['cephe']='''
<!-- A generic outside wall insulation system as a side cross-section; layers not to scale -->
<ellipse cx="687" cy="672" rx="500" ry="28" fill="#657b65" opacity=".10" filter="url(#shadow)"/>
<path d="M195 145l80-43h168l-80 43z" fill="#d1a183" stroke="#796c5c" stroke-width="4"/><path d="M195 145h168v474H195z" fill="url(#brick)" stroke="#796c5c" stroke-width="4"/><path d="M363 145l80-43v474l-80 43z" fill="#b8785d" stroke="#796c5c" stroke-width="4"/>
<path d="M443 145l56-29h45l-56 29z" fill="#cac9b4" stroke="#796c5c" stroke-width="4"/><rect x="443" y="145" width="45" height="474" fill="#c7c5ad" stroke="#796c5c" stroke-width="4"/>
<path d="M488 145l61-31h165l-61 31z" fill="#dce3cf" stroke="#796c5c" stroke-width="4"/><rect x="488" y="145" width="165" height="474" fill="#d8e1ca" stroke="#796c5c" stroke-width="4"/><path d="M488 302h165M488 461h165" stroke="#a3b69f" stroke-width="3"/>
<path d="M653 145l50-26h72l-50 26z" fill="#bed0b9" stroke="#796c5c" stroke-width="4"/><rect x="653" y="145" width="72" height="474" fill="url(#mesh)" stroke="#796c5c" stroke-width="4"/>
<path d="M725 145l48-24h78l-48 24z" fill="#dedbcc" stroke="#796c5c" stroke-width="4"/><rect x="725" y="145" width="78" height="474" fill="#e4e0d2" stroke="#796c5c" stroke-width="4"/>
<path d="M803 145l46-22h107l-46 22z" fill="#f8f4e9" stroke="#796c5c" stroke-width="4"/><rect x="803" y="145" width="107" height="474" fill="#f8f4e9" stroke="#796c5c" stroke-width="4"/>
<g fill="#8b9587" stroke="#5a6959" stroke-width="3"><path d="M382 365h251v13H382z"/><circle cx="633" cy="371" r="23" fill="#d4dfca"/><circle cx="633" cy="371" r="8" fill="#a3b5a0"/></g>
<path d="M950 183v405" stroke="#c57855" stroke-width="4" stroke-dasharray="11 11"/>
'''
art['kusur']='''
<!-- One damaged wall under inspection -->
<path d="M205 107h967v515H205z" fill="#ebe7d9" stroke="#8c8979" stroke-width="4"/><path d="M205 622h967l105 77H98z" fill="#dedacb" stroke="#8c8979" stroke-width="4"/>
<path d="M342 388c-43-68-22-161 25-180 24-10 49 12 69 31 35 35 94 42 94 105 0 73-31 124-107 130-39 2-64-32-81-86z" fill="#a9c4bd" opacity=".55"/><path d="M382 265c17 5 28 20 30 42M449 329c25 10 29 34 24 52" fill="none" stroke="#8aac9f" stroke-width="4"/>
<path d="M775 128l-29 82 38 42-31 71 39 49-27 77 27 46-12 86" fill="none" stroke="#a4634a" stroke-width="7" stroke-linecap="round"/><path d="M783 252l41 25 30-16M751 323l-45 21-15 36M792 452l39-12 26 26" fill="none" stroke="#a4634a" stroke-width="4"/>
<path d="M574 426c-32 5-53 34-48 70 5 37 38 48 65 43 19-4 33-12 39-31 25 6 56-13 57-37 2-27-28-45-54-37-11-17-35-20-59-8z" fill="#d1b6a0" stroke="#ae8e78" stroke-width="3"/>
<g transform="translate(900 495)"><rect x="0" y="0" width="105" height="156" rx="13" fill="#d0dbca" stroke="#708373" stroke-width="5"/><rect x="17" y="18" width="71" height="53" rx="5" fill="#f4f2e5" stroke="#708373" stroke-width="4"/><path d="M29 42h47" stroke="#9cab9d" stroke-width="5"/><circle cx="53" cy="112" r="17" fill="#bd7354" stroke="#708373" stroke-width="4"/></g>
<g transform="translate(1020 602) rotate(7)"><rect width="135" height="67" rx="8" fill="#c3cdbb" stroke="#708373" stroke-width="4"/><circle cx="69" cy="33" r="23" fill="#eef0e4" stroke="#708373" stroke-width="4"/><circle cx="69" cy="33" r="12" fill="#7f9684"/></g>
'''
art['teslim']='''
<!-- Quality-control clipboard with image, ruler and pen -->
<ellipse cx="691" cy="670" rx="490" ry="30" fill="#657b65" opacity=".12" filter="url(#shadow)"/>
<g transform="translate(432 97) rotate(-3 220 270)"><rect x="0" y="0" width="420" height="535" rx="12" fill="#b9c8b4" stroke="#687c6b" stroke-width="5"/><rect x="23" y="30" width="374" height="478" rx="4" fill="#fffcf2" stroke="#98a997" stroke-width="3"/><path d="M150 30V8q0-25 60-25t60 25v22" fill="#d8e4d6" stroke="#687c6b" stroke-width="5"/><path d="M62 112h28v28H62zM62 195h28v28H62zM62 278h28v28H62zM62 361h28v28H62z" fill="none" stroke="#92a894" stroke-width="4"/><path d="M68 123l7 8 13-16M68 206l7 8 13-16" fill="none" stroke="#5e8768" stroke-width="5"/><path d="M117 119h204m-204 18h158m-158 65h204m-204 18h144m-144 65h204m-204 18h159m-159 65h204m-204 18h158" stroke="#c6d1bf" stroke-width="7"/></g>
<g transform="translate(166 382) rotate(-8 135 95)"><rect width="271" height="198" rx="3" fill="#faf8ef" stroke="#98a997" stroke-width="4"/><rect x="14" y="14" width="243" height="145" fill="#d5e0d1"/><path d="M15 126l63-55 48 39 48-48 83 63" fill="none" stroke="#8eaa93" stroke-width="7"/><circle cx="207" cy="46" r="16" fill="#d6a785"/><path d="M19 179h160" stroke="#bdcbbb" stroke-width="6"/></g>
<g transform="translate(923 184) rotate(12 70 210)"><rect x="45" width="45" height="390" rx="5" fill="#d5b78e" stroke="#866d55" stroke-width="4"/><path d="M45 38h20M45 73h13M45 108h20M45 143h13M45 178h20M45 213h13M45 248h20M45 283h13M45 318h20M45 353h13" stroke="#8a7058" stroke-width="3"/></g>
<path d="M926 616l194-135 23 33-197 134z" fill="#c46d4b" stroke="#775d4e" stroke-width="4"/><path d="M923 619l-20 30 43-2z" fill="#e1c6a7" stroke="#775d4e" stroke-width="4"/>
'''
art['tas']='''
<!-- One clad wall with one panel offset to reveal prepared backing -->
<path d="M180 114h1020v500H180z" fill="#d0c8b5" stroke="#817d70" stroke-width="4"/><path d="M180 614h1020l90 81H95z" fill="#ddd9ca" stroke="#817d70" stroke-width="4"/>
<rect x="215" y="150" width="250" height="210" fill="#c5c3b2" stroke="#929785" stroke-width="4"/><path d="M230 166v180m22-180v180m22-180v180m22-180v180m22-180v180m22-180v180m22-180v180m22-180v180m22-180v180m22-180v180" stroke="#a1ad9b" stroke-width="6"/>
<g stroke="#8a8d7e" stroke-width="4"><rect x="493" y="150" width="305" height="210" fill="#e5e4d7"/><rect x="814" y="150" width="345" height="210" fill="#d4dfd2"/><rect x="215" y="376" width="305" height="207" fill="#e9e5d9"/><rect x="536" y="376" width="305" height="207" fill="#d6e0d1"/><rect x="857" y="376" width="302" height="207" fill="#ede5d9"/></g>
<g fill="none" stroke="#b7c2b3" stroke-width="3" opacity=".8"><path d="M510 175q95 12 154 103t113 42M853 175q88 53 125 18t148 47M244 407q104 20 123 104t133 49M559 413q90-10 144 78t112 56M879 398q92 45 138 18t119 69"/></g>
<g transform="translate(235 135) rotate(-7 125 105)"><rect width="250" height="210" fill="#f4eee0" stroke="#a49985" stroke-width="4"/><path d="M21 42q77 9 103 67t103 51M44 12q64 33 80 73t90 54" fill="none" stroke="#bfc5b4" stroke-width="3"/></g>
<path d="M1175 163v406" stroke="#c57a58" stroke-width="5" stroke-dasharray="14 10"/>
'''
for name,body in art.items():
 out=P/f'detay-{name}.svg';out.write_text(head+body+end);print(out.name,len(head+body+end))
