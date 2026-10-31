from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from xml.sax.saxutils import escape
from pathlib import Path
import pymupdf, os, math, json

ROOT=Path('/home/user')
AS=ROOT/'ince_isler_assets'/'jpg'
SOURCE=ROOT/'uploads'/'Ince_Isler_Rehberi.pdf'
FRONT=ROOT/'ince_isler_on_bolum.pdf'
OUTPUT=ROOT/'Ince_Isler_Resimli_Kullanim_Rehberi.pdf'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONTB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DVS',FONT))
pdfmetrics.registerFont(TTFont('DVSB',FONTB))
W,H=A4
L,R=44,W-44
NAVY=colors.HexColor('#1c3042')
MID=colors.HexColor('#405669')
MUTE=colors.HexColor('#6a7b87')
TEAL=colors.HexColor('#176f74')
ORANGE=colors.HexColor('#cb6429')
AMBER=colors.HexColor('#e5a257')
PALE=colors.HexColor('#f5f4ef')
BLUEPALE=colors.HexColor('#eaf2f2')
ORANGEPALE=colors.HexColor('#fbf1e7')
LINE=colors.HexColor('#d6e0e0')
WHITE=colors.white
FRONT_PAGES=25
links=[]
overflow=[]

# Record links in PDF-space coordinates. Targets are physical PDF page numbers.
def link_rect(c,x,y,w,h,target,kind='link'):
    links.append({'source':c.getPageNumber()-1,'rect':[x,H-(y+h),x+w,H-y],
                  'target':target-1,'kind':kind})

def paragraph(c,text,x,top,width,size=10,leading=None,color=NAVY,bold=False,align=0):
    if leading is None: leading=size*1.38
    sty=ParagraphStyle('x',fontName='DVSB' if bold else 'DVS',fontSize=size,leading=leading,
                       textColor=color,alignment=align,allowWidows=0,allowOrphans=0,
                       wordWrap=None,splitLongWords=1)
    pg=Paragraph(escape(text).replace('\n','<br/>'),sty)
    _,height=pg.wrap(width,1000)
    pg.drawOn(c,x,top-height)
    return height

def font(c,name,size,col):
    c.setFont(name,size);c.setFillColor(col)

def frame(c,x,y,w,h,fill=WHITE,stroke=LINE,r=7):
    c.setFillColor(fill);c.setStrokeColor(stroke)
    c.roundRect(x,y,w,h,r,stroke=1,fill=1)

def page_header(c,tag='SAHA REHBERİ'):
    font(c,'DVSB',8.1,TEAL);c.drawString(L,H-32,'İNCE İŞLER')
    font(c,'DVS',8.1,MUTE);c.drawString(L+73,H-32,'/  '+tag)
    c.setStrokeColor(LINE);c.setLineWidth(.7);c.line(L,H-40,R,H-40)

def page_footer(c):
    n=c.getPageNumber()
    c.setStrokeColor(LINE);c.setLineWidth(.6);c.line(L,42,R,42)
    font(c,'DVS',7.3,MUTE);c.drawString(L,27,'RESİMLİ SAHA ÖZETİ  •  Proje ve üretici talimatları esastır')
    font(c,'DVSB',8.5,NAVY);c.drawRightString(R,27,f'{n:02d} / {FRONT_PAGES:02d}')

def title(c,t,sub=None):
    font(c,'DVSB',21.5,NAVY);c.drawString(L,H-78,t)
    if sub:
        paragraph(c,sub,L,H-87,R-L,9.6,13.2,MID)

def image_box(c,name,x,y,w,h):
    frame(c,x,y,w,h,colors.HexColor('#f8f5ed'),LINE,7)
    c.saveState()
    # clip the photo within the softly rounded figure box
    path=c.beginPath();path.roundRect(x+1,y+1,w-2,h-2,6)
    c.clipPath(path,stroke=0,fill=0)
    c.drawImage(ImageReader(str(AS/(name+'.jpg'))),x+1,y+1,width=w-2,height=h-2,
                preserveAspectRatio=True,anchor='c',mask='auto')
    c.restoreState()

# Vector diagrams are intentionally schematic rather than application details.
def visual(c,kind,x,y,w,h):
    c.saveState()
    s=min(w/250,h/164)
    c.translate(x+(w-250*s)/2,y+(h-164*s)/2)
    c.scale(s,s)
    c.setFillColor(colors.HexColor('#f3f5f0'));c.setStrokeColor(LINE)
    c.roundRect(0,0,250,164,7,stroke=1,fill=1)
    def txt(x,y,t,size=8,color=MID,bold=False):
        font(c,'DVSB' if bold else 'DVS',size,color);c.drawString(x,y,t)
    def arr(x1,y1,x2,y2,col=TEAL):
        c.setStrokeColor(col);c.setFillColor(col);c.setLineWidth(1.3)
        c.line(x1,y1,x2,y2)
        ang=math.atan2(y2-y1,x2-x1);a=4.5
        p=c.beginPath();p.moveTo(x2,y2);p.lineTo(x2-a*math.cos(ang-.45),y2-a*math.sin(ang-.45));p.lineTo(x2-a*math.cos(ang+.45),y2-a*math.sin(ang+.45));p.close()
        c.drawPath(p,stroke=0,fill=1)
    if kind=='material':
        c.setFillColor(colors.HexColor('#e4bd91'));c.setStrokeColor(MID)
        for xx,yy in [(24,33),(82,33),(24,71),(82,71)]:
            c.roundRect(xx,yy,52,33,3,stroke=1,fill=1)
            c.setStrokeColor(colors.HexColor('#a07e5b'));c.line(xx+6,yy+19,xx+46,yy+19)
        c.setFillColor(colors.HexColor('#c9945a'));c.rect(18,24,122,7,stroke=0,fill=1)
        c.setFillColor(WHITE);c.setStrokeColor(TEAL);c.roundRect(151,39,78,86,5,stroke=1,fill=1)
        for j,label in enumerate(['ÜRÜN','PARTİ','TARİH']):
            txt(160,105-j*23,label,8,TEAL,True)
            c.setStrokeColor(LINE);c.line(160,100-j*23,219,100-j*23)
        txt(25,131,'KURU VE DÜZENLİ DEPO',8,ORANGE,True)
    elif kind=='joints':
        c.setStrokeColor(MID);c.setLineWidth(1)
        for xx in [16,77]:
            c.setFillColor(colors.HexColor('#dce9e8'));c.roundRect(xx,88,54,47,2,stroke=1,fill=1)
        c.setFillColor(ORANGE);c.rect(71,88,5,47,stroke=0,fill=1)
        txt(145,117,'DERZ',8.5,TEAL,True);arr(142,112,77,112)
        txt(145,104,'karo arası',7.5,MID)
        c.setFillColor(colors.HexColor('#dce9e8'));c.rect(18,23,19,43,stroke=1,fill=1);c.rect(38,23,67,16,stroke=1,fill=1)
        c.setFillColor(ORANGE);c.circle(39,40,5,stroke=0,fill=1)
        txt(137,50,'ELASTİK',8.5,TEAL,True);txt(137,38,'köşe birleşimi',7.5,MID)
        arr(135,46,45,41)
    elif kind=='kitchen':
        c.setStrokeColor(MID);c.setLineWidth(1)
        c.setFillColor(colors.HexColor('#d7e4df'));c.rect(20,48,147,56,stroke=1,fill=1)
        c.line(68,48,68,104);c.line(118,48,118,104)
        c.setFillColor(colors.HexColor('#d8c2a6'));c.rect(16,104,155,7,stroke=1,fill=1)
        c.setFillColor(colors.HexColor('#e6efeb'));c.rect(20,123,64,20,stroke=1,fill=1);c.rect(90,123,77,20,stroke=1,fill=1)
        c.setDash(3,2);c.setStrokeColor(ORANGE);c.line(13,116,218,116);c.setDash()
        c.setStrokeColor(TEAL);c.setLineWidth(3);c.line(93,48,93,65);c.line(93,65,103,65)
        txt(176,127,'KOT',8,ORANGE,True);txt(176,84,'MONTAJ',8,TEAL,True);txt(176,70,'NOKTASI',7,TEAL,True)
        arr(174,80,150,77);txt(176,45,'TESİSAT',8,TEAL,True);arr(173,43,105,64)
    elif kind=='facade':
        xs=[19,80,123,164];ws=[58,39,37,41];fs=['#ded8ca','#d6e4de','#efd0ae','#e8e8e4']
        for xx,ww,fc in zip(xs,ws,fs):
            c.setFillColor(colors.HexColor(fc));c.setStrokeColor(MID);c.rect(xx,44,ww,81,stroke=1,fill=1)
        txt(20,24,'ALT YÜZEY',7.8,MID,True);txt(86,137,'SİSTEM',8,TEAL,True)
        txt(166,24,'BİTİŞ',7.8,ORANGE,True)
        c.setStrokeColor(TEAL);c.setLineWidth(1);c.line(80,132,162,132)
        txt(17,8,'Katmanlar projeye göre değişir.',7,MUTE)
    elif kind=='ceiling':
        c.setFillColor(colors.HexColor('#ddd9ce'));c.setStrokeColor(MID);c.rect(18,122,180,14,stroke=1,fill=1)
        c.setStrokeColor(MID);c.setLineWidth(2)
        for xx in [45,91,137]: c.line(xx,122,xx,91)
        c.setFillColor(colors.HexColor('#eaf2f2'));c.rect(15,79,145,12,stroke=1,fill=1)
        c.rect(15,50,18,29,stroke=1,fill=1)
        c.setStrokeColor(AMBER);c.setLineWidth(4);c.line(37,81,80,81)
        txt(166,118,'TAŞIYICI',7.5,TEAL,True);txt(166,88,'LEVHA',7.5,TEAL,True)
        txt(20,26,'IŞIK TESTİ + ERİŞİM',8.2,ORANGE,True)
    elif kind=='defect':
        c.setFillColor(WHITE);c.setStrokeColor(MID);c.roundRect(18,51,72,84,4,stroke=1,fill=1)
        c.setStrokeColor(ORANGE);c.setLineWidth(2)
        p=c.beginPath();p.moveTo(58,130);p.lineTo(50,112);p.lineTo(60,99);p.lineTo(48,81);p.lineTo(56,59);c.drawPath(p,stroke=1)
        c.setStrokeColor(TEAL);c.circle(68,93,19,stroke=1,fill=0);c.line(80,80,95,64)
        for yy,label in [(122,'BELİRTİ'),(96,'NEDEN'),(70,'ONARIM'),(44,'YENİDEN KONTROL')]:
            c.setFillColor(BLUEPALE);c.setStrokeColor(LINE);c.roundRect(114,yy-4,116,19,4,stroke=1,fill=1)
            txt(122,yy+2,label,7.8,TEAL,True)
        txt(20,23,'ÖNCE NEDENİ ARA',8,ORANGE,True)
    elif kind=='quality':
        c.setFillColor(WHITE);c.setStrokeColor(MID);c.roundRect(37,32,91,108,4,stroke=1,fill=1)
        c.setFillColor(colors.HexColor('#d5e4e0'));c.roundRect(63,134,39,10,3,stroke=1,fill=1)
        for yy in [112,91,70,49]:
            c.setStrokeColor(TEAL);c.rect(49,yy,9,9,stroke=1,fill=0)
            c.line(52,yy+4,54,yy+2);c.line(54,yy+2,58,yy+8)
            c.setStrokeColor(LINE);c.line(66,yy+4,111,yy+4)
        c.setStrokeColor(ORANGE);c.setLineWidth(3);c.circle(164,100,23,stroke=1,fill=0);c.line(180,84,202,62)
        txt(149,43,'KAYIT',8.5,TEAL,True);txt(149,30,'VE ONAY',8.5,TEAL,True)
    else: raise ValueError(kind)
    c.restoreState()

cards=[
 dict(title='Önce güvenlik',sub='İşe başlamadan alanı, ekipmanı ve çalışanı birlikte değerlendir.',image='guvenlik',
  purpose='İşi güvenle yapabilecek koşulları sağlamak; düşme, toz, kesik ve elektrik riskini azaltmak.',
  pre='İşe özgü risk değerlendirmesi ve saha kuralları görülmüş olmalı.',
  steps=['İşin ve alanın risklerini değerlendir; uygun kişisel koruyucuyu seç.',
         'Toz, kesme ve kimyasallara uygun göz, yüz ve solunum koruması kullan.',
         'Yüksekte çalışmada uygun platformu ve düşmeye karşı korumayı planla.',
         'Elektrik ve ekipmanı yetkili kişilere kontrol ettir; hasarlı aleti ayır.'],
  checks=['Maske ve filtre işe uygun; yüz uyumu kontrol edildi.','İskele veya merdiven uygun ve kontrol edilmiş.','Kablo, fiş ve koruyucular sağlam; alan güvenli.','Geçiş ve acil çıkış yolları açık.'],
  caution='Görseldeki donanım yalnızca örnektir. Gerekli KKD ve çalışma yöntemi işin riskine ve mevzuata göre belirlenir.',source=11,source_label='İş güvenliği ve KKD  •  kaynak s. 11–14'),
 dict(title='Ölç ve kaydet',sub='Düzlük, yatay, düşey ve açı kontrolü sonraki işlerin referansıdır.',image='olcum',
  purpose='Uygulamadan önce mevcut durumu görmek ve sonraki ekip için güvenilir referans oluşturmak.',
  pre='Aletlerin sağlamlığı ve doğruluğu kontrol edilmeli.',
  steps=['Projedeki referans kotunu ve ölçü alınacak noktaları belirle.',
         'Su terazisi veya lazerle yatay ve düşeyi farklı noktalarda kontrol et.',
         'Uzun mastarla yüzeyi yatay, düşey ve çapraz yönlerde incele.',
         'Sapmayı, ölçüm yerini ve kabul kriterini kayıt altına al.'],
  checks=['Aletler temiz, sağlam ve kontrol edilmiş.','Kapı açıklığı ve köşeler birden fazla noktada ölçüldü.','Yüzey sapması şartname ile karşılaştırıldı.','Zemin veya duvar nemi gerekiyorsa ölçüldü.'],
  caution='Yüzeyin elle kuru hissedilmesi nem ölçümünün yerine geçmez. Toleranslar işin şartnamesine ve ürüne göre değişir.',source=15,source_label='Ölçü ve kontrol araçları  •  kaynak s. 15–19'),
 dict(title='Malzeme kabulü',sub='Doğru ürün, doğru parti ve uygun depolama yeniden işi önler.',vector='material',
  purpose='Yanlış, hasarlı veya uygunsuz depolanmış ürünü uygulamaya girmeden ayırmak.',
  pre='Onaylı ürün listesi ve teknik föy hazır olmalı.',
  steps=['Ürün adı, tipi, miktarı ve kullanım yerini siparişle karşılaştır.',
         'Parti, tarih ve ambalaj durumunu kontrol edip fotoğraflandır.',
         'Uygun ürünleri üretici koşullarına göre kuru ve güvenli alanda sakla.',
         'Uygunsuz ürünü ayır; kararı ve tedarikçi bildirimini kaydet.'],
  checks=['Ürün onaylı uygulamaya uygun.','Parti ve renk/kalibre uyumu kontrol edildi.','Paket hasarsız ve son kullanım bilgisi uygun.','Depolama ve istif koşulları uygun.'],
  caution='Aynı renk kodu her partide tamamen aynı görünmeyebilir. Numune ve parti uyumunu uygulama öncesi doğrula.',source=20,source_label='Malzeme bilgisi  •  kaynak s. 20–23'),
 dict(title='Sıva ve alçı',sub='Yüzey hazırlığı → kılavuz → uygulama → kuruma ve kontrol.',image='siva',
  purpose='Düzgün, sağlam ve sonraki kaplamaya uygun bir yüzey elde etmek.',
  pre='Tesisat geçişleri ve yüzeyin uygunluğu kontrol edilmiş olmalı.',
  steps=['Gevşek, kirli ve uygunsuz yüzeyi temizle; uygun hazırlığı yap.',
         'Proje kotuna göre kılavuzları kur; yatay ve düşey doğruluğu ölç.',
         'Harç ve katları ürün föyüne göre hazırla; yüzeyi mastarla düzle.',
         'Yeterli kuruma sonrası yüzeyi ve köşeleri yeniden kontrol et.'],
  checks=['Alt yüzey sağlam ve hazırlanmış.','Kılavuz ve köşeler kontrol edilmiş.','Düzlük farklı yönlerde ölçülmüş.','Bir sonraki kat için kuruluk uygun.'],
  caution='Karışım suyu, kat kalınlığı ve bekleme süresi ürün ve saha koşuluna bağlıdır; üretici föyünü kullan.',source=24,source_label='Sıva ve alçı işleri  •  kaynak s. 24–30'),
 dict(title='Alçıpan ve tavan',sub='İskelet, levha ve derz; birlikte çalışan bir sistemdir.',image='alcipan',
  purpose='Projedeki yangın, akustik ve taşıma gereklerini karşılayan düzgün bir kaplama oluşturmak.',
  pre='Tesisat noktaları ve onaylı sistem detayı belirlenmiş olmalı.',
  steps=['Tavan ve duvar kotlarını, askı ve profil konumlarını projeye göre işaretle.',
         'Taşıyıcı sistemi uygun bağlantılarla kur; düzlem ve sağlamlığı kontrol et.',
         'Uygun levhayı sistemin vida ve birleşim kurallarına göre sabitle.',
         'Derz bandı ve dolguyu uygula; kuruma sonrası yüzeyi kontrol et.'],
  checks=['Levha tipi ve profil sistemi doğru.','Tesisat ve kapatılacak bölgeler kayıtlı.','Vidalar ve birleşimler üreticiye uygun.','Derz, köşe ve tavan düzlemi kontrol edildi.'],
  caution='Vida ve askı aralıkları ile yangın/akustik detayları sistem onayına göre belirlenir; tek bir genel ölçü kullanılmaz.',source=31,source_label='Alçıpan ve tavan işleri  •  kaynak s. 31–36'),
 dict(title='Boya işleri',sub='Görünen sonucun büyük kısmı boyadan önceki hazırlıktır.',image='boya',
  purpose='Temiz, homojen ve yüzeye uygun boya sistemiyle iyi bir bitiş elde etmek.',
  pre='Nem kaynağı giderilmiş; yüzey ürün koşullarına uygun olmalı.',
  steps=['Kusurları onar; yüzeyi zımparala ve tozdan arındır.',
         'Uygun astarı uygula; üreticinin bekleme süresine uy.',
         'Boyayı öngörülen kat sayısı ve uygulama koşullarında sür.',
         'Tam kuruma sonrası yandan ışıkla yüzeyi ve kenarları kontrol et.'],
  checks=['Yüzey ve ortam koşulları uygun.','Doğru astar, renk ve parti kullanıldı.','Kat aralıklarına uyuldu.','Akma, iz, örtücülük ve kenarlar kontrol edildi.'],
  caution='Yaş boyaya bakarak nihai renk veya kuruluk kararı verme; ürün föyündeki süre ve ortam koşullarını esas al.',source=37,source_label='Boya işleri  •  kaynak s. 37–41'),
 dict(title='Seramik ve fayans',sub='Önce yüzey ve dizilim; sonra yapıştırma, düzlem ve derz.',image='seramik',
  purpose='Düzgün derzli, sağlam ve projedeki hareket detaylarına uygun kaplama yapmak.',
  pre='Islak alanda su yalıtımı kaplama öncesinde kabul edilmiş olmalı.',
  steps=['Yüzeyi kontrol et; eksen, kesim ve kuru dizilim planını oluştur.',
         'Ürün sistemine uygun yapıştırıcıyı ve tarağı seç; föye göre hazırla.',
         'Karoları yerleştir; gerekli temas kontrolünü ve seviye ayarını yap.',
         'Belirlenen bekleme süresi sonrası derzi ve birleşimleri tamamla.'],
  checks=['Renk, parti, ölçü ve dizilim kontrol edildi.','Derz aralıkları ve düzlem proje ile uyumlu.','Hareket derzleri kapatılmadı.','Yapışma ve köşe detayları kontrol edildi.'],
  caution='Seramik ve derz, su yalıtım sisteminin yerine geçmez. Yapıştırıcı seçimi yüzeye, karoya ve kullanım yerine bağlıdır.',source=42,source_label='Seramik ve fayans  •  kaynak s. 42–49'),
 dict(title='Derz ve elastik birleşim',sub='Karo arası ile hareketli köşe birleşimi aynı detay değildir.',vector='joints',
  purpose='Yüzey aralıklarını doğru malzemeyle tamamlamak ve hareket detaylarını korumak.',
  pre='Yapıştırıcının derzlemeye hazır olduğu doğrulanmış olmalı.',
  steps=['Derz boşluklarını temizle; uygun derz ürününü ve rengi seç.',
         'Dolguyu ürün talimatına göre uygula; yüzeyi doğru zamanda temizle.',
         'Köşe ve birleşimlerde proje detayına uygun elastik mastik kullan.',
         'Sürekliliği, görünümü ve ürünün kürlenme süresini kontrol et.'],
  checks=['Derz rengi ve aralıkları tutarlı.','Hareket derzleri detayına uygun.','Mastik yüzeye ve ortam şartlarına uygun.','Yüzey kürlenme boyunca korunuyor.'],
  caution='Derz veya silikon tek başına su yalıtımı değildir. Esnek birleşim detayında proje ve ürün sistemini izle.',source=50,source_label='Derz ve silikon  •  kaynak s. 50–53'),
 dict(title='Parke ve laminat',sub='Kuru ve düzgün zemin, doğru altlık ve hareket payı esastır.',image='laminat',
  purpose='Döşemenin nemden etkilenmesini, kalkmasını ve hareketinin engellenmesini önlemek.',
  pre='Zemin nemi ve düzlüğü, seçilen sistemin sınırlarında olmalı.',
  steps=['Zemin durumunu ölç; nem ve düzlük kayıtlarını değerlendir.',
         'Paketleri ürün talimatına göre ortama alıştır; uygun altlığı yerleştir.',
         'Sıraları ve birleşimleri üretici detayına göre şaşırtarak döşe.',
         'Kenar ve eşik hareket paylarını koru; son kontrolü yap.'],
  checks=['Nem ölçümü ve yüzey kabulü tamam.','Altlık ve gerekiyorsa nem bariyeri uygun.','Duvar ve geçişlerde üretici payı korundu.','Kilit, eşik ve süpürgelik kontrol edildi.'],
  caution='Genleşme payı ve altlık ihtiyacı ürüne, oda ölçüsüne ve zemine göre değişir; tek bir genel değer yeterli değildir.',source=54,source_label='Parke ve laminat  •  kaynak s. 54–59'),
 dict(title='Kapı ve pencere',sub='Açıklığı ölç; kasayı hizala; kanadın çalışmasını doğrula.',image='kapi',
  purpose='Kasanın doğru konumda, kanadın sürtmeden ve güvenli şekilde çalışmasını sağlamak.',
  pre='Bitmiş döşeme kotu, duvar açıklığı ve ürün detayı bilinmeli.',
  steps=['Açıklığı birkaç noktadan ve bitmiş döşeme kotuna göre ölç.',
         'Kasayı takozla konumlandır; yatay, düşey ve köşegenleri kontrol et.',
         'Projeye ve üreticiye uygun mekanik bağlantıları uygula.',
         'Kanadı tak; boşlukları, açılma ve kapanmayı kontrol et.'],
  checks=['Açıklık ve kasa ölçüsü uygun.','Kasa düşey, yatay ve sağlam.','Kanat sürtmüyor; boşluklar uygun.','Pencere çevresi hava/su detayı kontrol edildi.'],
  caution='Montaj köpüğü tek başına gerekli mekanik sabitlemenin yerine geçmez. Yangın kapılarında sertifikalı detayı uygula.',source=60,source_label='Kapı ve pencere montajı  •  kaynak s. 60–64'),
 dict(title='Mutfak ve dolap',sub='Kot, bağlantı ve tesisat çıkışları montajdan önce birlikte kontrol edilir.',vector='kitchen',
  purpose='Dolap, tezgâh ve tesisatın birbirini engellemeden güvenli biçimde yerleşmesi.',
  pre='Onaylı yerleşim, ölçüler ve duvarın taşıma/bağlantı detayı hazır olmalı.',
  steps=['Saha ölçüsünü ve elektrik/tesisat çıkışlarını yerleşimle karşılaştır.',
         'Kotları işaretle; duvara uygun ankraj ve bağlantı detayını belirle.',
         'Dolapları sırayla yerleştir; yatay, düşey ve sabitlemeyi doğrula.',
         'Tezgâh ve evye bağlantılarını kontrol et; son ayarı ve temizliği yap.'],
  checks=['Delme noktalarında gizli hat riski kontrol edildi.','Dolap ve tezgâh kotları uyumlu.','Kapak/çekmece rahat çalışıyor.','Su bağlantısı ve çevresi kontrol edildi.'],
  caution='Duvar tipi ve yük için uygun sabitleme kullanılmalı; elektrik ve tesisat bağlantıları yetkili kişilerce yapılmalı.',source=65,source_label='Dolap ve mutfak montajı  •  kaynak s. 65–68'),
 dict(title='Islak hacim yalıtımı',sub='Yalıtımın sürekliliğini kaplama yapılmadan önce kontrol et.',image='islak',
  purpose='Su geçişini önleyen sistemin köşe, gider ve geçişlerde kesintisiz kalmasını sağlamak.',
  pre='Eğim, gider ve tesisat çıkışları onaylı detayla uyumlu olmalı.',
  steps=['Yüzeyi, eğimi ve gider/boru geçişlerini kontrol et ve hazırla.',
         'Köşe, geçiş ve detayları uyumlu sistem bileşenleriyle güçlendir.',
         'Yalıtımı proje ve ürün sistemine göre uygula; kat aralıklarına uy.',
         'Kaplamadan önce gerekli test ve kabulü yetkili kişiyle kaydet.'],
  checks=['Yüzey ve gider detayı uygun.','Köşe ve boru geçişleri süreklilik gösteriyor.','Sistem ve bekleme koşulları doğrulandı.','Gerekli test ve fotoğraflı kabul yapıldı.'],
  caution='Su testi yöntemi, süresi ve güvenliği; proje, şartname ve yetkili kişinin onayına göre belirlenir. Görsel ölçeksizdir.',source=69,source_label='Banyo ve ıslak hacim  •  kaynak s. 69–73'),
 dict(title='Dış cephe',sub='Onaylı sistem, hava koşulu ve güvenli çalışma birlikte yönetilir.',vector='facade',
  purpose='Dış etkilere uygun kaplama sisteminin kesintisiz ve güvenli uygulanması.',
  pre='Proje detayı, ürün sistemi ve yüksekte çalışma planı hazır olmalı.',
  steps=['Alt yüzeyi ve hava koşullarını sistem gerekliliklerine göre kontrol et.',
         'Katmanları ve mekanik bağlantıları onaylı detaya göre uygula.',
         'Pencere, köşe, damlalık ve hareket birleşimlerini ayrıca incele.',
         'Düzlem, yüzey ve katman kabullerini kayıtla tamamla.'],
  checks=['İskele ve çalışma yöntemi uygun şekilde kontrol edildi.','Ürünler aynı onaylı sistemle uyumlu.','Hava ve yüzey koşulları uygun.','Köşe ve açıklık detayları belgelendi.'],
  caution='Şema katmanların ölçekli bir detayı değildir. İskele ve yüksekte çalışma yetkin kişilerce, ilgili kurallara göre yürütülür.',source=88,source_label='Dış cephe ince işleri  •  kaynak s. 88–92'),
 dict(title='Tavan ve kaplamalar',sub='Gizli aydınlatma, kaplama deseni ve erişim detaylarını önceden çöz.',vector='ceiling',
  purpose='Tavan, aydınlatma ve duvar kaplamalarının birbirine uyumunu ve son görünümünü kontrol etmek.',
  pre='Tesisat, taşıyıcı ve bitiş detayları proje üzerinde koordine edilmeli.',
  steps=['Işık oluğu, erişim ve tesisat konumlarını kapatmadan önce kontrol et.',
         'Tavan ve duvar kaplamalarında referans çizgilerini belirle.',
         'Desen, damar ve birleşim düzenini uygulama öncesi planla.',
         'Yüzeyi ve ışığı kuruma sonrası farklı açılardan incele.'],
  checks=['Elektrik işleri yetkili kişiyle koordine edildi.','Tesisata gerekli erişim korundu.','Desen ve birleşim planı onaylandı.','Yüzey ve ışıkta son kontrol yapıldı.'],
  caution='Elektrik bağlantıları ve yangınla ilgili detaylar yetkili kişilerce, onaylı projeye ve üretici sistemine göre yapılır.',source=93,source_label='Tavan ve duvar kaplamaları  •  kaynak s. 93–101'),
 dict(title='Kusuru yönet',sub='Belirtiyi kaydet; sebebi araştır; onar ve yeniden doğrula.',vector='defect',
  purpose='Görünen kusuru kapatmak yerine tekrarını önleyecek nedeni bulmak.',
  pre='Yer, tarih, kapsam ve fotoğrafla ilk kayıt oluşturulmalı.',
  steps=['Çatlak, kabarma veya lekeyi konumuyla ve fotoğrafla kaydet.',
         'Olası nem, hareket veya yapışma nedenini yetkin kişiyle araştır.',
         'Nedeni gider; uygun onarım yöntemini ve sorumluyu belirle.',
         'Onarım sonrası tekrar kontrol et ve kaydı sonuçlandır.'],
  checks=['Kusur yeri ve fotoğraf numarası yazıldı.','Neden araştırması ve karar kaydedildi.','Sorumlu ve hedef tarih belirlendi.','Son kontrol ve kapanış onaylandı.'],
  caution='Büyüyen çatlak, yapısal hareket veya elektrikle temas riski olan nemde işi durdur; ilgili uzmanı çağır.',source=74,source_label='Sık görülen kusurlar  •  kaynak s. 74–77'),
 dict(title='Kontrol ve teslim',sub='Her işi bir sonraki ekibe kayıtlı ve korunmuş olarak devret.',vector='quality',
  purpose='Eksikleri görünür kılmak, kapanış sorumluluğunu belirlemek ve teslimi belgelemek.',
  pre='Onaylı kalite kriterleri, test sonuçları ve iş kalemi listesi hazır olmalı.',
  steps=['Ara kontrolü, üstü kapanacak işler kapatılmadan önce yap.',
         'Eksikleri yer, fotoğraf, sorumlu ve hedef tarihle kaydet.',
         'Düzeltmeleri doğrula; temizlik ve yüzey korumasını tamamla.',
         'Kabul durumunu, kalan işleri ve taraf imzalarını tutanağa geçir.'],
  checks=['Ölçü ve test sonuçları kayıtlı.','Kusurlar ve kapanış tarihleri izleniyor.','Ürün/bakım belgeleri hazır.','Kabul durumu ve imzalar açık.'],
  caution='Fotoğraflar ve imza, teknik testin yerine geçmez; test ve kabul kriterleri proje ve sözleşmeye göre belirlenir.',source=78,source_label='Kalite kontrol ve teslim  •  kaynak s. 78–80'),
]

source_chapters=[
('İnce İşe Giriş',9),('İş Güvenliği ve Kişisel Koruyucu Donanım',11),('Ölçü ve Kontrol Araçları',15),('Malzeme Bilgisi',20),
('Sıva ve Alçı İşleri',24),('Alçıpan ve Tavan İşleri',31),('Boya İşleri',37),('Seramik ve Fayans',42),('Derz ve Silikon',50),
('Parke ve Laminat',54),('Kapı ve Pencere Montajı',60),('Dolap ve Mutfak Montajı',65),('Banyo, Islak Hacim ve Tesisat Çıkışları',69),
('Sık Görülen Kusurlar ve Çözümleri',74),('Kalite Kontrol ve Teslim',78),('Ekip Yönetimi ve Şeflik Kurnazlıkları',81),
('Hızlı Başvuru: Kuruma Süreleri ve Ölçü Tabloları',83),('Sözlük',84),('Uygulama Kontrol Listeleri',86),('Dış Cephe İnce İşleri',88),
('Tavan Süsleme ve Gizli Aydınlatma',93),('Duvar Kaplamaları ve Doğal Taş',97),('Teslim Sonrası Garanti ve Bakım',102),
('Malzeme Teknik Özellikleri',105),('Sıva ve Alçı Malzemeleri',106),('Alçıpan ve Profil Malzemeleri',108),
('Seramik, Fayans ve Doğal Taş',110),('Yapıştırıcı, Derz ve Silikon',112),('Boya ve Astar Malzemeleri',114),
('Parke, Laminat ve Kapı Malzemeleri',116),('Su Yalıtım ve Yardımcı Malzemeler',118),('Ölçü Tolerans Tablosu',120),
('Malzeme Kodları ve Standart Referansları',121)]

c=canvas.Canvas(str(FRONT),pagesize=A4,pageCompression=1)
c.setTitle('İnce İşler | Resimli Kullanım ve Şantiye Rehberi')
c.setAuthor('Saha düzeni ve görsel anlatım')
c.setSubject('Resimli saha kartları, kontrol formları ve kaynak rehber')

# 01 Cover
c.setFillColor(colors.HexColor('#f7f5ef'));c.rect(0,0,W,H,stroke=0,fill=1)
c.setFillColor(TEAL);c.roundRect(L,H-58,118,20,4,stroke=0,fill=1)
font(c,'DVSB',8,WHITE);c.drawString(L+11,H-51,'ŞANTİYE  /  SAHA REHBERİ')
font(c,'DVSB',36,NAVY);c.drawString(L,H-112,'İNCE İŞLER')
font(c,'DVS',16.3,MID);c.drawString(L,H-138,'Resimli kullanım ve kontrol rehberi')
font(c,'DVS',10.5,MUTE);c.drawString(L,H-159,'Adım adım uygulama  •  kontrol listeleri  •  formlar')
image_box(c,'kapak',L,246,R-L,338)
font(c,'DVSB',10,TEAL);c.drawString(L,220,'SAHADA HIZLI BAKIŞ  +  TAM KAYNAK')
paragraph(c,'Ölçüden teslime, önemli kontrol noktalarını görsellerle öne çıkaran pratik bir çalışma. Orijinal rehberin tüm içeriği bu dosyada korunmuştur.',L,205,R-L,10.3,15.1,MID)
frame(c,L,90,R-L,57,WHITE,LINE,5)
font(c,'DVSB',8.3,ORANGE);c.drawString(L+13,128,'ÖNEMLİ')
paragraph(c,'Çizimler kavramsaldır; proje, güncel mevzuat ve üretici talimatlarının yerine geçmez.',L+13,118,R-L-26,9,12.4,NAVY)
font(c,'DVS',7.7,MUTE);c.drawString(L,48,'SAHA KARTLARI   /   KONTROL FORMLARI   /   KAYNAK REHBER')
c.showPage()

# 02 Navigation / how to read
page_header(c,'İÇİNDEKİLER');title(c,'İhtiyacın olan sayfaya git','Başlıklara tıklayabilir; PDF yer imlerinden tüm kaynak bölümlerine geçebilirsin.')
frame(c,L,638,R-L,67,BLUEPALE,LINE,6)
font(c,'DVSB',9.2,TEAL);c.drawString(L+13,684,'BU DOSYADA NELER VAR?')
paragraph(c,'Önce 25 sayfalık resimli saha özeti ve yazdırılabilir formlar, ardından 121 sayfalık tam kaynak rehber yer alır.',L+13,674,R-L-26,9.4,13.1,NAVY)
font(c,'DVSB',10.5,NAVY);c.drawString(L,614,'SAHA KARTLARI')
entries=[('İş sırası ve kontrol kapıları',3)]+[(q['title'],i+4) for i,q in enumerate(cards)]
left=entries[:9];right=entries[9:]
for col,els in enumerate([left,right]):
    x=L+col*258; cw=242
    for i,(label,num) in enumerate(els):
        yy=590-i*27.6
        c.setStrokeColor(LINE);c.line(x,yy-8,x+cw,yy-8)
        font(c,'DVS',9.2,NAVY);c.drawString(x+2,yy,label)
        font(c,'DVSB',9.2,TEAL);c.drawRightString(x+cw-3,yy,f'{num:02d}')
        link_rect(c,x,yy-9,cw,22,num,'front-toc')
font(c,'DVSB',10.5,NAVY);c.drawString(L,322,'FORMLAR VE TAM KAYNAK')
for i,(lab,num) in enumerate([('Günlük kontrol formu',20),('Malzeme kabul formu',21),('Kusur takip formu',22),('Ara kontrol ve teslim formu',23)]):
    col=i//2;row=i%2;x=L+col*258;yy=297-row*26
    font(c,'DVS',9.2,NAVY);c.drawString(x,yy,lab)
    font(c,'DVSB',9.2,TEAL);c.drawRightString(x+239,yy,f'{num:02d}')
    link_rect(c,x,yy-6,242,21,num,'form-toc')
frame(c,L,156,R-L,76,ORANGEPALE,colors.HexColor('#f1d7ba'),6)
font(c,'DVSB',9,ORANGE);c.drawString(L+12,213,'KAYNAK SAYFALARI HAKKINDA')
paragraph(c,'Tam kaynak PDF sayfa 26’da başlar. Kaynağın kendi içindekilerindeki sayılar orijinal sayfa numaralarıdır. Yeni PDF karşılıkları için 24–25. sayfalardaki tıklanabilir dizini kullan.',L+12,202,R-L-24,9.1,12.8,NAVY)
font(c,'DVSB',9.5,TEAL);c.drawString(L,127,'Kaynağın tam dizini  →  24–25')
link_rect(c,L,118,220,24,24,'source-index')
font(c,'DVSB',9.5,TEAL);c.drawRightString(R,127,'Tam kaynak  →  26')
link_rect(c,R-160,118,160,24,26,'source-start')
paragraph(c,'Kaynak metin ayrıca teknik doğrulamadan geçirilmemiştir; ölçü, süre, güvenlik ve kabul için yetkili kişi, proje ve güncel üretici verileri esastır.',L,102,R-L,8.2,11.3,MUTE)
page_footer(c);c.showPage()

# 03 Workflow
page_header(c,'İŞ SIRASI');title(c,'İş sırası ve kontrol kapıları','Genel bağımlılık şemasıdır; kesin sıra onaylı proje ve iş programına göre değişir.')
workflow=[
 ('01','PROJE VE ÖLÇÜ','Detay, kot, yüzey durumu, malzeme ve riskleri doğrula.'),
 ('02','TESİSAT VE ALTYAPI','Kapatılacak hatları, çıkışları ve gerekli testleri kontrol et.'),
 ('03','YÜZEY VE TAŞIYICI SİSTEM','Sıva, alçıpan ve yüzey hazırlığını uygun sırayla tamamla.'),
 ('04','YALITIM VE KAPLAMA','Islak hacim yalıtımı kabul edilmeden seramiğe geçme.'),
 ('05','BİTİŞ, MONTAJ VE TESLİM','Boya, döşeme ve son montajı programla; koru ve kayda bağla.')]
y=690
for i,(n,h,b) in enumerate(workflow):
    frame(c,L,y-59,R-L,59,WHITE,LINE,6)
    c.setFillColor(BLUEPALE);c.circle(L+26,y-29,17,stroke=0,fill=1)
    font(c,'DVSB',10,TEAL);c.drawCentredString(L+26,y-33,n)
    font(c,'DVSB',9.5,NAVY);c.drawString(L+55,y-22,h)
    paragraph(c,b,L+55,y-29,R-L-70,9.1,12.3,MID)
    if i<len(workflow)-1:
        c.setStrokeColor(TEAL);c.setLineWidth(1);c.line(L+26,y-60,L+26,y-69)
    y-=72
frame(c,L,241,R-L,67,ORANGEPALE,colors.HexColor('#f0d1b1'),6)
font(c,'DVSB',9.2,ORANGE);c.drawString(L+13,288,'KONTROL KAPISI')
paragraph(c,'Bir işi kapatmadan veya diğer ekibe devretmeden önce ölçüm / test / fotoğraf kaydı al; eksik varsa sorumlu ve hedef tarihi belirle.',L+13,277,R-L-26,9.5,13.4,NAVY)
font(c,'DVSB',10,TEAL);c.drawString(L,208,'Günlük saha kontrolü ve formlar  →  sayfa 20')
link_rect(c,L,198,350,23,20,'workflow-forms')
paragraph(c,'Örnek: Islak hacim için yalıtım → gerekli test ve onay → seramik. Diğer işlerin sırası malzeme, kuruma ve saha programına göre planlanır.',L,178,R-L,9.1,13,MID)
page_footer(c);c.showPage()

# 04–19 practical illustrated cards
def card(c, data, number):
    page_header(c,f'SAHA KARTI  {number:02d}')
    title(c,data['title'],data['sub'])
    # purpose/precondition box
    frame(c,L,526,239,170,BLUEPALE,LINE,6)
    font(c,'DVSB',8.2,TEAL);c.drawString(L+13,676,'AMAÇ')
    h1=paragraph(c,data['purpose'],L+13,664,213,9.6,13.5,NAVY)
    y2=664-h1-15
    font(c,'DVSB',8.2,TEAL);c.drawString(L+13,y2,'ÖN KOŞUL')
    h2=paragraph(c,data['pre'],L+13,y2-11,213,9.2,13.1,MID)
    if y2-11-h2<535: overflow.append((c.getPageNumber(),'purpose',y2-11-h2))
    if data.get('image'):
        image_box(c,data['image'],304,526,247,170)
    else:
        visual(c,data['vector'],304,526,247,170)
    font(c,'DVS',7,MUTE);c.drawString(305,512,'Kavramsal görsel; ölçekli teknik detay değildir.')
    c.setStrokeColor(LINE);c.line(L,502,R,502)
    font(c,'DVSB',10.1,NAVY);c.drawString(L,482,'UYGULAMA SIRASI')
    font(c,'DVSB',10.1,NAVY);c.drawString(312,482,'KONTROL LİSTESİ')
    yy=462
    for i,step in enumerate(data['steps']):
        c.setFillColor(TEAL);c.circle(L+9,yy-5,8.4,stroke=0,fill=1)
        font(c,'DVSB',7.7,WHITE);c.drawCentredString(L+9,yy-7.8,str(i+1))
        h=paragraph(c,step,L+24,yy+1,226,9.2,12.9,NAVY)
        yy-=max(h,13)+12
    if yy<270: overflow.append((c.getPageNumber(),'steps',yy))
    yy2=462
    for item in data['checks']:
        c.setStrokeColor(TEAL);c.setLineWidth(.8);c.rect(313,yy2-9,9,9,stroke=1,fill=0)
        h=paragraph(c,item,330,yy2+1,218,9.0,12.8,NAVY)
        yy2-=max(h,13)+12
    if yy2<270: overflow.append((c.getPageNumber(),'checks',yy2))
    frame(c,L,182,R-L,79,ORANGEPALE,colors.HexColor('#eed5bb'),5)
    c.setFillColor(ORANGE);c.roundRect(L,182,4,79,2,stroke=0,fill=1)
    font(c,'DVSB',8.9,ORANGE);c.drawString(L+13,242,'KRİTİK NOKTA')
    hh=paragraph(c,data['caution'],L+13,231,R-L-26,9.3,13.4,NAVY)
    if 231-hh<190: overflow.append((c.getPageNumber(),'caution',231-hh))
    font(c,'DVSB',9.4,TEAL);c.drawString(L,152,'AYRINTILI KAYNAĞA GİT  →')
    font(c,'DVS',8.6,MID);c.drawString(L,136,data['source_label'])
    link_rect(c,L,130,R-L,36,FRONT_PAGES+data['source'],'source-ref')
    c.setStrokeColor(LINE);c.line(L,96,R,96)
    font(c,'DVS',8,MUTE);c.drawString(L,104,'Saha notu:')
    page_footer(c);c.showPage()

for i,d in enumerate(cards): card(c,d,i+1)

# Shared helpers for printable forms

def form_header(c,t,sub):
    page_header(c,'YAZDIRILABİLİR FORM');title(c,t,sub)
    font(c,'DVS',8.5,MUTE);c.drawRightString(R,H-108,'Formu her iş alanı için ayrı kullanın.')

def field(c,x,top,w,label):
    font(c,'DVSB',8.3,TEAL);c.drawString(x,top,label)
    c.setStrokeColor(colors.HexColor('#9caeb4'));c.setLineWidth(.6);c.line(x,top-18,x+w,top-18)

def check_item(c,x,top,text,width=235):
    c.setStrokeColor(TEAL);c.setLineWidth(.8);c.rect(x,top-9,9,9,stroke=1,fill=0)
    return paragraph(c,text,x+16,top+1,width-16,9.1,12.7,NAVY)

def section_label(c,x,y,label):
    font(c,'DVSB',9.1,NAVY);c.drawString(x,y,label)
    c.setStrokeColor(LINE);c.line(x,y-6,R,y-6)

def write_lines(c,x,top,w,n=2,gap=24):
    c.setStrokeColor(colors.HexColor('#aebdc0'));c.setLineWidth(.5)
    for j in range(n): c.line(x,top-j*gap,x+w,top-j*gap)

# 20 Daily checklist
form_header(c,'Günlük saha kontrolü','Başlangıçta ve iş bitiminde işaretle; eksiği sorumluya aktar.')
field(c,L,705,150,'TARİH');field(c,218,705,150,'PROJE / ŞANTİYE');field(c,392,705,159,'KAT / MAHAL')
section_label(c,L,663,'İŞE BAŞLAMADAN ÖNCE')
for i,txt in enumerate(['İş, yöntem ve bugün çalışacak ekip net.','Risk değerlendirmesi ve uygun KKD gözden geçirildi.',
                        'İskele, merdiven, el aletleri ve enerji durumu kontrol edildi.','Malzeme, parti ve iş alanı uygulamaya hazır.',
                        'Ölçü, referans kotu ve önceki işin kabulü kontrol edildi.']):
    check_item(c,L,642-i*28,txt,500)
section_label(c,L,492,'İŞ BİTİMİNDE / DEVİRDE')
for i,txt in enumerate(['Ölçü, test ve görsel kontrol yapıldı; sonuç kaydedildi.','Üstü kapanacak işler kapatılmadan fotoğraflandı.',
                        'Eksikler, sorumlu ve hedef tarihle kaydedildi.','Çevredeki bitmiş yüzeyler ve malzeme korundu.',
                        'Alan temizlendi; sonraki ekip için güvenli devredildi.']):
    check_item(c,L,471-i*28,txt,500)
section_label(c,L,321,'EKSİK / ALINACAK AKSİYON')
write_lines(c,L,290,R-L,3,25)
field(c,L,189,230,'SORUMLU / HEDEF TARİH');field(c,322,189,229,'KONTROL EDEN / İMZA')
paragraph(c,'Bu form, işe özgü risk değerlendirmesi veya zorunlu kontrol kayıtlarının yerine geçmez.',L,139,R-L,8.3,11.7,MUTE)
page_footer(c);c.showPage()

# 21 material form
form_header(c,'Malzeme kabul formu','Her ürün veya parti için ayrı bir kayıt açılması önerilir.')
field(c,L,706,150,'TARİH');field(c,215,706,153,'PROJE / MAHAL');field(c,389,706,162,'KABUL EDEN')
field(c,L,658,240,'ÜRÜN / TİP');field(c,310,658,241,'ÜRETİCİ / TEDARİKÇİ')
field(c,L,610,150,'MİKTAR / BİRİM');field(c,215,610,153,'PARTİ / LOT');field(c,389,610,162,'ÜRETİM / SON KULLANIM')
section_label(c,L,568,'KABUL KONTROLÜ')
for i,txt in enumerate(['Onaylı ürün ve kullanım alanı ile uyumlu.','Parti / renk / kalibre bilgisi kontrol edildi.',
                        'Ambalaj ve ürün gözle hasarsız.','Miktar ve sevk belgesi uyumlu.',
                        'Depolama koşulu üretici talimatına uygun.','Teknik föy / gereken belgeler mevcut.']):
    check_item(c,L,547-i*25,txt,500)
section_label(c,L,376,'SONUÇ')
check_item(c,L,356,'Kabul',100);check_item(c,160,356,'Şartlı kabul',150);check_item(c,319,356,'Ret / karantina',170)
font(c,'DVSB',8.3,TEAL);c.drawString(L,316,'AÇIKLAMA / FOTOĞRAF NO / YAPILACAK İŞLEM')
write_lines(c,L,294,R-L,3,23)
field(c,L,198,230,'TEDARİKÇİ / BİLDİRİM');field(c,322,198,229,'KABUL EDEN / İMZA')
paragraph(c,'Uygunsuz ürünleri belirgin şekilde ayırın; karar ve bildirimi proje prosedürüne göre kaydedin.',L,142,R-L,8.4,11.8,MUTE)
page_footer(c);c.showPage()

# 22 defects
form_header(c,'Kusur takip formu','Belirtiyi kaydet; nedeni doğrula; onarım ve kapanışı izle.')
field(c,L,706,150,'KAYIT NO');field(c,215,706,153,'TARİH');field(c,389,706,162,'PROJE / MAHAL')
field(c,L,658,240,'İŞ KALEMİ / KONUM');field(c,310,658,241,'SORUMLU EKİP / KİŞİ')
section_label(c,L,615,'KUSURUN TANIMI VE KAPSAMI')
write_lines(c,L,587,R-L,3,23)
field(c,L,505,240,'FOTOĞRAF / ÖLÇÜM REFERANSI');field(c,310,505,241,'HEDEF TARİH')
section_label(c,L,461,'ARAŞTIRILAN NEDEN / KARAR')
write_lines(c,L,432,R-L,3,23)
section_label(c,L,339,'DÜZELTİCİ İŞLEM VE YENİDEN KONTROL')
write_lines(c,L,310,R-L,3,23)
field(c,L,218,150,'UYGULAMA TARİHİ');field(c,215,218,153,'KONTROL TARİHİ');field(c,389,218,162,'KONTROL EDEN / İMZA')
check_item(c,L,155,'Açık',90);check_item(c,157,155,'Takipte',110);check_item(c,281,155,'Kapatıldı',130)
page_footer(c);c.showPage()

# 23 handover
form_header(c,'Ara kontrol ve teslim','Sonucu açıkça seç; varsa kalan işleri ve sorumlusunu belirt.')
field(c,L,706,150,'TARİH');field(c,215,706,153,'PROJE / MAHAL');field(c,389,706,162,'İŞ KALEMİ')
field(c,L,658,240,'UYGULAYAN / EKİP');field(c,310,658,241,'KONTROL EDEN')
section_label(c,L,615,'KONTROL VE BELGELER')
for i,txt in enumerate(['Ölçü / test sonucu ve kabul kriteri kayıtlı.','Kapanan işler için fotoğraf ve gerekli raporlar mevcut.',
                        'Yüzey koruması, temizlik ve işlev kontrolü tamam.','Malzeme ve bakım belgeleri teslim edildi / planlandı.']):
    check_item(c,L,594-i*27,txt,500)
section_label(c,L,465,'KABUL DURUMU')
check_item(c,L,445,'Kabul',100);check_item(c,160,445,'Şartlı kabul',150);check_item(c,319,445,'Ret',100)
section_label(c,L,406,'KALAN İŞ / SORUMLU / HEDEF TARİH')
# printable writing table
x=L;y=288;tw=R-L;th=98
c.setStrokeColor(LINE);c.setLineWidth(.7);c.rect(x,y,tw,th,stroke=1,fill=0)
c.setFillColor(BLUEPALE);c.rect(x,y+73,tw,25,stroke=0,fill=1)
c.setStrokeColor(LINE)
for xx in [x+238,x+379]: c.line(xx,y,xx,y+th)
for yy in [y+25,y+49,y+73]: c.line(x,yy,x+tw,yy)
font(c,'DVSB',8.2,NAVY);c.drawString(x+8,y+82,'EKSİK / AÇIKLAMA');c.drawString(x+246,y+82,'SORUMLU');c.drawString(x+387,y+82,'HEDEF TARİH')
field(c,L,233,230,'DEVREDEN / İMZA');field(c,322,233,229,'TESLİM ALAN / İMZA')
paragraph(c,'Şartlı kabul ve ret gerekçelerini, kalan işleri ve tarihleri sözleşme / proje prosedürüyle birlikte değerlendirin.',L,174,R-L,8.4,11.8,MUTE)
page_footer(c);c.showPage()

# 24–25 exhaustive source index, each row is a live destination.
def source_index(c,start,end):
    page_header(c,'TAM KAYNAK DİZİNİ')
    title(c,'Kaynağın tam dizini',f'Bölüm {start+1}–{end}  •  Tıklayarak orijinal bölümün yeni PDF içindeki sayfasına geç.')
    font(c,'DVSB',8,TEAL);c.drawString(L,711,'BÖLÜM')
    font(c,'DVSB',8,TEAL);c.drawRightString(R,711,'KAYNAK S.  /  PDF S.')
    for j,idx in enumerate(range(start,end)):
        name,src=source_chapters[idx];top=698-j*34
        if j%2==0:
            c.setFillColor(colors.HexColor('#f7f9f7'));c.roundRect(L-3,top-27,R-L+6,31,3,stroke=0,fill=1)
        font(c,'DVSB',8.8,ORANGE);c.drawString(L+5,top-13,f'{idx+1:02d}')
        # each title is intentionally short enough for a single 9 pt line
        h=paragraph(c,name,L+34,top-1,338,8.8,10.8,NAVY)
        if h>22: overflow.append((c.getPageNumber(),'index',name))
        font(c,'DVSB',8.8,TEAL);c.drawRightString(R-5,top-13,f'{src:03d}   /   {FRONT_PAGES+src:03d}')
        link_rect(c,L-2,top-27,R-L+4,31,FRONT_PAGES+src,'source-index-row')
    paragraph(c,'Soldaki sayı kaynağın kendi sayfası; sağdaki sayı bu dosyanın PDF sayfasıdır. Sayfa başlıkları tıklanabilir.',L,104,R-L,8.3,11.5,MUTE)
    page_footer(c);c.showPage()
source_index(c,0,17)
source_index(c,17,33)
assert c.getPageNumber()==26, c.getPageNumber()
c.save()
print('Front links recorded:',len(links),'Overflow warnings:',overflow)

# Build transparent vector overlays for otherwise mostly empty source chapter openers.
overlay_file=ROOT/'ince_isler_vektor_katmani.pdf'
src_vectors=[
 (20,'material',475,175,'Malzeme kabulü ve depolama'),
 (50,'joints',340,175,'Derz ile elastik birleşim'),
 (65,'kitchen',220,190,'Dolap, kot ve tesisat koordinasyonu'),
 (74,'defect',460,180,'Kusurdan kapanışa kontrol'),
 (78,'quality',410,180,'Kontrol, kayıt ve onay'),
 (88,'facade',385,185,'Cephe sistem katmanları'),
 (93,'ceiling',225,195,'Tavan ve aydınlatma ilişkisi'),
 (102,'quality',365,185,'Bakım ve kusur kayıtları')]
ov=canvas.Canvas(str(overlay_file),pagesize=A4,pageCompression=1)
for srcnum,kind,top,hh,caption in src_vectors:
    yy=H-top-hh
    visual(ov,kind,73,yy,449,hh)
    font(ov,'DVS',7.5,MUTE);ov.drawCentredString(W/2,yy-13,'Kavramsal şema  •  '+caption+'  •  ölçekli detay değildir')
    ov.showPage()
ov.save()

original=pymupdf.open(str(SOURCE))
doc=pymupdf.open(str(FRONT))
doc.insert_pdf(original,links=True,annots=True)
assert len(original)==121 and len(doc)==FRONT_PAGES+len(original)

# Add nine genuinely new generated illustrations to matching source section openers,
# strictly below original content. The text and original page count are retained.
src_images=[
 (11,'guvenlik',210),(15,'olcum',433),(24,'siva',390),(31,'alcipan',315),
 (37,'boya',410),(42,'seramik',292),(54,'laminat',275),(60,'kapi',210),(69,'islak',210)]
source_collision=[]
for source_page,name,top in src_images:
    p=doc[FRONT_PAGES+source_page-1]
    rect=pymupdf.Rect(76,top,519,top+295)
    origp=original[source_page-1]
    for b in origp.get_text('blocks'):
        if b[6]==0 and b[1]<770 and pymupdf.Rect(b[:4]).intersects(rect):
            source_collision.append((source_page,'image',b[4][:40]))
    p.insert_image(rect,filename=str(AS/(name+'.jpg')),keep_proportion=True,overlay=True)
    p.insert_font(fontname='dv',fontfile=FONT)
    p.insert_text((85,top+310),'Yeni görsel • Kavramsal anlatım; uygulama detayı projeye göre belirlenir.',
                  fontname='dv',fontsize=7.6,color=(0.38,0.45,0.48),overlay=True)

vdoc=pymupdf.open(str(overlay_file))
for j,(source_page,kind,top,hh,caption) in enumerate(src_vectors):
    p=doc[FRONT_PAGES+source_page-1]
    rect=pymupdf.Rect(73,top,522,top+hh+16)
    for b in original[source_page-1].get_text('blocks'):
        if b[6]==0 and b[1]<770 and pymupdf.Rect(b[:4]).intersects(rect):
            source_collision.append((source_page,'vector',b[4][:40]))
    p.show_pdf_page(p.rect,vdoc,j,overlay=True)

# Prominent contextual cautions next to several potentially misleading source passages.
# The source text itself remains intact; these notes do not claim a full technical audit.
notes=[
 (50,550,75,'TEKNİK NOT','Derz ve silikon tek başına su yalıtımı değildir. Islak hacimlerde proje ve ürün sistemine uygun, ayrı su yalıtımı gerekir.'),
 (70,600,82,'TEST VE UYGULAMA NOTU','Kat sayısı, dönüş yüksekliği ve test koşulları proje ve ürün sistemine göre belirlenir. Su testi yöntemini, süresini ve güvenliğini yetkili kişi onaylamalıdır.'),
 (83,670,75,'SÜRE VE ÖLÇÜ NOTU','Tablodaki sayılar kabul kriteri değildir. Ürün föyü ve projeyi esas alın; yüzeyin elle kuru hissedilmesi gerekli nem ölçümünün yerine geçmez.'),
 (112,700,79,'SINIFLANDIRMA NOTU','C2 işareti tek başına esneklik, hızlı priz veya kayma direnci anlamına gelmez. Bunlar ilgili S1/S2, F ve T işaretleriyle ayrıca tanımlanır; ürün föyünü doğrulayın.'),
 (113,510,76,'ÜRÜN SEÇİMİ NOTU','Yapıştırıcı sınıfı; karo, yüzey ve kullanım koşullarına göre belirlenir. C2 işareti tek başına S1/S2 esnekliğini ifade etmez.'),
 (119,510,76,'SU TESTİ NOTU','Test yapılıp yapılmayacağı, yöntemi, süresi ve güvenliği proje, şartname ve yetkili kişinin kararına bağlıdır.'),
 (120,415,75,'TOLERANS NOTU','Bu tabloda verilen rakamları evrensel kabul sınırı olarak kullanmayın. Proje, şartname, üretici bilgisi ve güncel ilgili standardı doğrulayın.')]
notes_file=ROOT/'ince_isler_teknik_notlar.pdf'
nc=canvas.Canvas(str(notes_file),pagesize=A4,pageCompression=1)
for sn,top,hh,label,text in notes:
    yy=H-top-hh
    frame(nc,63,yy,469,hh,ORANGEPALE,colors.HexColor('#eed5bb'),5)
    nc.setFillColor(ORANGE);nc.roundRect(63,yy,4,hh,2,stroke=0,fill=1)
    font(nc,'DVSB',8.2,ORANGE);nc.drawString(75,yy+hh-17,label)
    nh=paragraph(nc,text,75,yy+hh-25,445,8.8,12,NAVY)
    if yy+hh-25-nh<yy+7: overflow.append((sn,'source-note',nh))
    nc.showPage()
nc.save()
ndoc=pymupdf.open(str(notes_file))
for j,(sn,top,hh,label,text) in enumerate(notes):
    rect=pymupdf.Rect(63,top,532,top+hh)
    for b in original[sn-1].get_text('blocks'):
        if b[6]==0 and b[1]<780 and pymupdf.Rect(b[:4]).intersects(rect):
            source_collision.append((sn,'note',b[4][:40]))
    doc[FRONT_PAGES+sn-1].show_pdf_page(doc[FRONT_PAGES+sn-1].rect,ndoc,j,overlay=True)

# Complete the previously recorded links after the full document exists.
for li in links:
    p=doc[li['source']]
    p.insert_link({'kind':pymupdf.LINK_GOTO,'from':pymupdf.Rect(li['rect']),
                   'page':li['target'],'to':pymupdf.Point(0,0),'zoom':0})

# Link source contents headings to their original section locations.
old_toc_found=[];old_toc_missing=[]
for k,(name,src) in enumerate(source_chapters,1):
    # Search full heading, falling back to a distinctive prefix for multiline headings.
    candidates=[f'{k}. {name}', f'{k}. '+name[:min(len(name),18)].rstrip(), f'{k}. '+name[:min(len(name),12)].rstrip()]
    found=False
    for ori_toc_page in range(2,8):
        p=doc[FRONT_PAGES+ori_toc_page-1]
        for query in candidates:
            hits=p.search_for(query)
            if hits:
                rect=hits[0];rect.x1=min(R+4,max(rect.x1,rect.x0+180));rect.y0-=2;rect.y1+=3
                p.insert_link({'kind':pymupdf.LINK_GOTO,'from':rect,
                               'page':FRONT_PAGES+src-1,'to':pymupdf.Point(0,0),'zoom':0})
                found=True;old_toc_found.append((k,ori_toc_page,query));break
        if found:break
    if not found:old_toc_missing.append((k,name))

# Hierarchical PDF bookmarks.
toc=[[1,'Resimli saha özeti',1],
     [2,'Hızlı erişim',2],[2,'İş sırası ve kontrol kapıları',3]]
for i,d in enumerate(cards): toc.append([2,f"{i+1:02d}. {d['title']}",i+4])
toc.extend([[1,'Yazdırılabilir formlar',20],[2,'Günlük saha kontrolü',20],
            [2,'Malzeme kabul formu',21],[2,'Kusur takip formu',22],
            [2,'Ara kontrol ve teslim',23],
            [1,'Kaynağın tam dizini',24],[1,'Tam kaynak rehber (121 sayfa)',26]])
for i,(name,src) in enumerate(source_chapters,1):
    toc.append([2,f'{i:02d}. {name}',FRONT_PAGES+src])
doc.set_toc(toc)
doc.set_metadata({'title':'İnce İşler: Resimli Kullanım ve Şantiye Rehberi',
                  'subject':'Resimli saha kartları, kontrol formları ve tam kaynak rehber',
                  'author':'Saha rehberi', 'keywords':'ince işler, şantiye, görsel, kalite kontrol'})
doc.save(str(OUTPUT),garbage=4,deflate=True,clean=True)
doc.close();vdoc.close()
print('Source image/vector collisions:',source_collision)
print('Source contents links found:',len(old_toc_found),'missing:',old_toc_missing)
print('Output:',OUTPUT,'bytes',OUTPUT.stat().st_size)
print('Front pages',FRONT_PAGES,'+ original pages',len(original))
original.close()
