#!/usr/bin/env python
# coding: utf-8

# In[35]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[73]:


x=[1,2,3,4,5,6,7,8]
y=[1,4,9,16,25,36,49,64]
x2=[1,2,3,4,5,6,7,8,]
y2=[1,8,27,64,125,216,343,512]


# In[86]:


plt.plot(x,y,)
plt.plot(x2,y2)
plt.title('GRAFIGE BASLIK EKLEME')
plt.xlabel("x eksenine yazi ekleme")
plt.ylabel("y eksenine yazi ekleme")
plt.grid()


# In[81]:


plt.plot(x,y)
plt.plot(x2,y2)
plt.title('GRAFIGE BASLIK EKLEME')
plt.xlabel("x eksenine yazi ekleme")
plt.ylabel("y eksenine yazi ekleme")
plt.plot()


# In[ ]:





# # 1-)  SCATTER PLOT (Serpilme diyagrami)
# Serpilme diyagramı, bir tür kalite diyagramı. Serpilme diyagramı, iki farklı değişkenin arasındaki ilişkiyi belirlemek için kullanılır. Aralarındaki ilişkinin sebebi görülemese de, ilgili iki değişkenin arasında direkt olarak bir ilişki bulunup bulunmadığı ve bu ilişkinin ne derece güçlü olduğu görülebilir.
# 
# SERPİLME DİYAGRAMINI HANGİ DURUMLARDA KULLANMALIYIZ?
# 1-)Sayısal verileri eşleştirebildiğinizde
# 2-)Bağımlı değişkeniniz, bağımsız değişkeninizin her değeri için birden fazla değere sahipse
# 3-)İki değişkenin ilişkili olup olmadığını belirlemek için:
# 4-)Problemlerin potansiyel kök nedenlerini belirlemeye çalışırken 
# 5-)Beyin fırtınası yaptıktan sonra, balık kılçığı yaparken belirli bir neden ve etkinin ilişkili olup olmadığını objektif olarak belirlerken
# 6)İlişkili gibi görünen iki etkinin aynı sebeple olup olmadığını belirlerken
# Kontrol çizelgesi oluşturmadan önce otokorelasyon testi yapılırken
# 
# Serpilme diyagramını oluşturduktan sonra yorumlarken de aşağıdakileri gözden kaçırmamak gerekir:
# 
# Serpilme diyagramı bir ilişki gösteriyorsa, bir değişkenin diğerine neden olduğunu varsaymayın. Her ikisi de üçüncü bir değişkenden etkileniyor olabilir.
# Verileri grafiğe koyduğunuzda, diyagram düz bir çizgiye ne kadar çok benzerse, ilişki o kadar güçlü olur. Çizgi net değilse, ilişkinin varlığının makul bir kesinliği olup olmadığını istatistik belirler. İstatistiksel olarak bir ilişki yoksa veriler rastgele-tesadüfen oluşmuş olabilir.
# Bazen bir ilişki açık değildir, çünkü veriler yeterince geniş bir alanı kapsamaz. Bu durumda bütünü temsil edecek şekilde daha çok-daha iyi veri toplamak gerekir.
# Değişkenlerin ve değişkenlerin çıktılar üzerindeki etkisini-ilişkisini ne kadar doğru anlayıp yorumlayabilirsek problemin kök nedenini bulmaya o kadar yaklaşıyoruz. 

# In[18]:


x=20*np.random.randn(1000)+100
y= x + (10 * np.random.randn(1000)+50)


# In[19]:


plt.scatter(x,y)
plt.show()


# ## 2-) BAR CHAT (BAR GRAFIKLERI)
# çubuk grafik veya çubuk grafik, temsil ettikleri değerlerle orantılı yükseklik veya uzunluklara sahip dikdörtgen çubuklarla kategorik verileri sunan bir grafik veya grafiktir. Çubuklar dikey veya yatay olarak çizilebilir. Dikey çubuk grafiğe bazen sütun grafiği denir.
# 
# Ne zaman kullanılır?
# Sütunların gruplandırılması ve yığınlanması, gruplandırılmış verilerin görselleştirilmesini kolaylaştırır. Sütun grafik, satışların farklı yıllara yönelik tahminlerle karşılaştırılması gibi değerleri yan yana karşılaştırmak istediğinizde ve hesaplamalar (bu durumda satış ve tahmin) aynı birim kullanılarak hesaplandığında da yararlı olur.
# 
# Avantajlar: Sütun grafiğin okunması ve anlaşılması kolaydır. Sütun grafikleri kullanırken değerler için iyi bir genel bakış elde edersiniz.
# 
# Dezavantajlar: Sütun grafik, eksen uzunluğu sınırlaması nedeniyle birçok boyut değeriyle pek iyi performans göstermez. Boyutlar sığmıyorsa, kaydırma çubuğunu kullanarak kaydırma yapabilirsiniz, ancak tam resmi göremeyebilirsiniz.
# 

# In[32]:


x=["COVID-19","HEALTHY","SYMPTOMATIC"]
y=[1010,8562,1843]


# In[33]:


plt.bar(x,y)
plt.show()


# # Histogram grafigi
# Histogram, gruplar halinde sıralanmış istatistiksel verilerin dağılımını gösteren bir grafiktir. Tipik bir histogram bir x ekseni, bir y ekseni ve dikdörtgen çubuklardan oluşur. Değer grubu x ekseninde yer alırken y ekseni frekans sayısını gösterir. Bu yapı, topladığınız verilerden ne kadar farklı değerlerin birbiriyle karşılaştırıldığını kolayca görmenizi sağlar.
# 
# Histogramlar genellikle şirket sunumlarında ve iş toplantılarında kalite kontrol araçları olarak veya daha verimli hale gelmek için ayarlanması gerekebilecek işyeri görevlerini belirlemek için kullanılır.. 

# In[39]:


df=sns.load_dataset("penguins")


# In[40]:


df.head() 


# In[42]:


sns.histplot(data=df,x="flipper_length_mm")
plt.show()


# #  PİE CHART (DAIRESEL GRAFIK)
# Dairesel grafik, istatistik biliminde betimsel istatistik alanında kategorik verileri görsel bir şekilde betimleyip özetlemek için hazırlanan; içindeki kategori dilimlerini orantısal olarak gösteren bir daire şeklinde sunulan bir gösterim aracıdır.
# 
# Daire Grafiği Nerelerde Kullanılır?
# Daire grafiğinin kullanım alanı genellikle oransal değerler söz konusu olduğunda kullanılır. Bunlara örnek vermek gerekirse;
# 
# Seçimlerde oy oranlarının karşılaştırılması,
# Televizyon kanallarının reyting oranlarının gösterilmesi,
# Belli bir zaman içerisinde üretilen ürünlerin oranlarının gösterilmesi,
# Belli bir ürünün yıllara göre üretim miktarının gösterilmesi,
# Bir bölgede üretilen tarım ürünlerinin yüzde miktarının gösterilmesi vb.

# In[57]:


meyveler=["ELMA","MUZ","ARMUT","KIRAZ"]
sayilar=[25,25,30,15]


# In[58]:


plt.pie(sayilar, labels=meyveler)
plt.show()


# # HEATMAP( ISI HARITASI)
# Isı haritası, bir olgunun büyüklüğünü iki boyutta renk olarak gösteren bir veri görselleştirme tekniğidir. Renkteki varyasyon, ton veya yoğunluğa göre olabilir ve okuyucuya olgunun nasıl kümelendiği veya uzayda nasıl değiştiği hakkında açık görsel ipuçları verir
# 
# Heatmap ne işe yarıyor sorusunun cevabı olarak verilerin renkler eşliğinde analiz edilmesi verilebilir. Isı haritasında soğuk renkler az ilgi çeken veya tıklanan bölümleri, sıcak renkler ise sürekli dikkat çeken bölümleri simgelemektedir. Bu analiz bir webmaster’ın sitesinde hangi bölümlerin daha fazla veya daha az ilgi çektiğini görmesine olanak sağlamaktadır. Heatmap’te imleç hareketleri, kaydırma ve klavye hareketleri görülebilmektedir. Bu hareketlerin tam olarak görülmesi e-ticaret sitelerinde satışı az olan ürünlerle ilgili çalışma yapılmasına olanak sağlar.
# 
# 
# E-ticaret siteleri için de ısı haritası son derece önem arz etmektedir. Siteye giren ziyaretçinin az ilgisini çeken veya hızlı bir şekilde geçilen sayfaların tekrar düzenlenmesi ve sorunun saptanması için Heatmap son derece önemlidir.

# In[59]:


data=np.random.randn(10,12)


# In[61]:


sns.heatmap(data)
plt.show()


# # BOX PLOT(KUTU GRAFIGI)
# Bir kutu grafiği (Boxplot), veri çeyreklerini (veya yüzdelikleri) ve ortalamaları görüntüleyerek sayısal verilerin ve değişkenliğin görsel olarak dağılımını göstermek için kullanılır. Veri analizinde sıklıkla kullanılan bir grafik türüdür.
# 
# Kutu grafikleri, bir veri kümesinin beş özelliğini gösterir: minimum değer, ilk (%25) çeyrek, medyan, üçüncü (%75) çeyrek ve maksimum değer.
# 
# Her ne kadar kutu grafikleri Histogram ve yoğunluk çizgileri ile karşılaştırıldığında çok ilkel bile görünse daha az yer kaplama gibi bir avantajları vardır ve bu da birçok grup veya veri seti dağılımını karşılaştırırken oldukça kullanışlı bir özelliktir.
# 
# İşte, bir kutu-bıyık grafiğine bakarak elde edebileceğiniz gözlem türleri:
# 
# Önemli anahtar değerler neler? örneğin: ortalama, 25.yüzdelik? vb.
# 
# Eğer uç değerler varsa, bunların değerleri nedir?
# 
# Veri simetrik midir?
# 
# Verilerin gruplandırılması ne kadar sıkıdır?
# 
# Eğer veride kayma varsa, hangi yönedir?

# In[63]:


tips=sns.load_dataset("tips")


# In[64]:


tips.head()


# In[65]:


sns.boxplot(x=tips["total_bill"])
plt.show()


# # subplots

# In[104]:


fig=plt.figure(figsize=(18,5))
first_plot=fig.add_subplot(1,3,1)
first_plot.plot(x,y,color="blue")
first_plot.set_title("LINE PLOT")

second_plot=fig.add_subplot(1,3,2)
second_plot.scatter(x,y,color="red")
second_plot.set_title("SCATTER PLOT")

third_plot=fig.add_subplot(1,3,3)
third_plot.bar(x,y,color="orange")
third_plot.set_title("BAR PLOT")
plt.show()


# In[ ]:




