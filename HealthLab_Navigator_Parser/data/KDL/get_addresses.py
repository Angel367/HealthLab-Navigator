import requests
from bs4 import BeautifulSoup

from fake_useragent import UserAgent
import json
page = """<div class="address__list-wrap swiper-wrapper" style="transition: transform 0ms ease 0s; transform: translate3d(0px, -66.6663px, 0px);">
                    <div class="swiper-slide js-address-list swiper-slide-active" data-region-id="1"><div style="display: block" class="address__item" data-id="493" data-balloon-content="" data-shop="{&quot;lat&quot;:55.891941,&quot;lan&quot;:37.725900}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.891941,&quot;lan&quot;:37.725900}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Мытищи, ул.&nbsp;Семашко, д.&nbsp;35</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-15:30
<br>вс:7:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="500" data-balloon-content="" data-shop="{&quot;lat&quot;:56.011771,&quot;lan&quot;:37.481127}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:56.011771,&quot;lan&quot;:37.481127}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Лобня, ул.&nbsp;Ленина, д.&nbsp;15</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб: 07:30-15:30
<br>вс: 7:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="501" data-balloon-content="" data-shop="{&quot;lat&quot;:55.757870,&quot;lan&quot;:37.856884}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.757870,&quot;lan&quot;:37.856884}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Реутов, ул.&nbsp;Ленина, д.&nbsp;14</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт 07:00-17:00
<br>сб 07:30-15:30
<br>вс 07:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="502" data-balloon-content="" data-shop="{&quot;lat&quot;:55.895424,&quot;lan&quot;:37.452318}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.895424,&quot;lan&quot;:37.452318}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Химки, пр-т&nbsp;Ленинский, д.&nbsp;1к.&nbsp;1</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-15:30
<br>вс: 7:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="503" data-balloon-content="" data-shop="{&quot;lat&quot;:55.904922,&quot;lan&quot;:37.390442}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.904922,&quot;lan&quot;:37.390442}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Химки, ул.&nbsp;Молодежная, д.&nbsp;64</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-18:00
<br>сб: 07:30-15:30
<br>вс: 07:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="505" data-balloon-content="" data-shop="{&quot;lat&quot;:55.764460,&quot;lan&quot;:37.790543}" data-metro="м." Перово="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.764460,&quot;lan&quot;:37.790543}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/yellow.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Перово&nbsp;<br>
ул.&nbsp;Новогиреевская, д.&nbsp;4. корп.&nbsp;1</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-17:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="512" data-balloon-content="" data-shop="{&quot;lat&quot;:55.744774,&quot;lan&quot;:37.498635}" data-metro="м." Багратионовская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.744774,&quot;lan&quot;:37.498635}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/blue.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Багратионовская&nbsp;<br>
ул.&nbsp;Барклая, д.&nbsp;12</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="520" data-balloon-content="" data-shop="{&quot;lat&quot;:55.736934,&quot;lan&quot;:37.467874}" data-metro="м." Пионерская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.736934,&quot;lan&quot;:37.467874}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/blue.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Пионерская&nbsp;<br>
ул.&nbsp;Малая Филевская, д.&nbsp;18</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="521" data-balloon-content="" data-shop="{&quot;lat&quot;:55.826382,&quot;lan&quot;:37.436194}" data-metro="м." Тушинская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.826382,&quot;lan&quot;:37.436194}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/violet.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Тушинская&nbsp;<br>
проезд Стратонавтов, д.&nbsp;9</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="525" data-balloon-content="" data-shop="{&quot;lat&quot;:55.800934,&quot;lan&quot;:37.532795}" data-metro="м." Аэропорт="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.800934,&quot;lan&quot;:37.532795}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/green.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Аэропорт&nbsp;<br>
пр.&nbsp;Ленинградский, д.&nbsp;62.</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="534" data-balloon-content="" data-shop="{&quot;lat&quot;:55.778385,&quot;lan&quot;:37.516449}" data-metro="м.Полежаевская">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.778385,&quot;lan&quot;:37.516449}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/violet.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Полежаевская&nbsp;<br>
ул.&nbsp;Куусинена, д.&nbsp;1.</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-17:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="544" data-balloon-content="" data-shop="{&quot;lat&quot;:55.863621,&quot;lan&quot;:37.559388}" data-metro="м." Селигерская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.863621,&quot;lan&quot;:37.559388}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/lime.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Селигерская&nbsp;<br>
б-р.&nbsp;Бескудниковский, д.&nbsp;13</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="545" data-balloon-content="" data-shop="{&quot;lat&quot;:55.791445,&quot;lan&quot;:37.496345}" data-metro="м." Октябрьское="" поле="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.791445,&quot;lan&quot;:37.496345}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/red.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Октябрьское поле&nbsp;<br>
ул.&nbsp;Маршала Бирюзова, д.&nbsp;9.</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="546" data-balloon-content="" data-shop="{&quot;lat&quot;:55.860494,&quot;lan&quot;:37.602948}" data-metro="м." Отрадное="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.860494,&quot;lan&quot;:37.602948}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/gray.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Отрадное&nbsp;<br>
ул.&nbsp;Хачатуряна, д.&nbsp;16</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="549" data-balloon-content="" data-shop="{&quot;lat&quot;:55.939444,&quot;lan&quot;:37.515641}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.939444,&quot;lan&quot;:37.515641}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Долгопрудный, ул. Первомайская, д.&nbsp;33, пом.&nbsp;1</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-17:00
<br>сб: 07:30-15:30
<br>вс: 07:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="556" data-balloon-content="" data-shop="{&quot;lat&quot;:55.745544,&quot;lan&quot;:37.679641}" data-metro="м." Римская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.745544,&quot;lan&quot;:37.679641}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/green.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Римская&nbsp;<br>
пл.&nbsp;Рогожская Застава, д.&nbsp;2/1, стр. 1.</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-17:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="557" data-balloon-content="" data-shop="{&quot;lat&quot;:55.748240,&quot;lan&quot;:37.816405}" data-metro="м." Новогиреево="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.748240,&quot;lan&quot;:37.816405}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/yellow.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Новогиреево&nbsp;<br>
&nbsp;Свободный пр-кт д.&nbsp;37/18.</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-17:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="572" data-balloon-content="" data-shop="{&quot;lat&quot;:55.839026,&quot;lan&quot;:37.489491}" data-metro="м." Водный="" стадион="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.839026,&quot;lan&quot;:37.489491}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/green.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Водный стадион,<br>
шоссе&nbsp;Головинское, д.&nbsp;4</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="605" data-balloon-content="" data-shop="{&quot;lat&quot;:55.793915,&quot;lan&quot;:37.615479}" data-metro="м." Марьина="" Роща="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.793915,&quot;lan&quot;:37.615479}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Марьина Роща,<br>
ул.&nbsp;Шереметьевская, д.&nbsp;1, к.1</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="628" data-balloon-content="" data-shop="{&quot;lat&quot;:55.855851,&quot;lan&quot;:37.470383}" data-metro="м." Речной="" вокзал="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.855851,&quot;lan&quot;:37.470383}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/green.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Речной вокзал,<br>
&nbsp;Ленинградское шоссе, д.&nbsp;94, к. 1</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="658" data-balloon-content="" data-shop="{&quot;lat&quot;:55.734353,&quot;lan&quot;:37.670203}" data-metro="м." Пролетарская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.734353,&quot;lan&quot;:37.670203}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Пролетарская,<br>
&nbsp;Волгоградский проспект, д.&nbsp;1 стр 1А &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-17:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="663" data-balloon-content="" data-shop="{&quot;lat&quot;:55.852055,&quot;lan&quot;:37.438463}" data-metro="Сходненская">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.852055,&quot;lan&quot;:37.438463}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Сходненская,<br>
&nbsp; ул. Героев Панфиловцев, д.&nbsp;1/2 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-19:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="667" data-balloon-content="" data-shop="{&quot;lat&quot;:55.845957,&quot;lan&quot;:37.363608}" data-metro="м." Митино="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.845957,&quot;lan&quot;:37.363608}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Митино,<br>
&nbsp;Митинская ул., д.&nbsp;36 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-17:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="668" data-balloon-content="" data-shop="{&quot;lat&quot;:55.793032,&quot;lan&quot;:37.801295}" data-metro="м." Первомайская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.793032,&quot;lan&quot;:37.801295}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Первомайская,<br>
&nbsp;Первомайская, д.&nbsp;74 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-19:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="669" data-balloon-content="" data-shop="{&quot;lat&quot;:55.885080,&quot;lan&quot;:37.606044}" data-metro="м." Бибирево="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.885080,&quot;lan&quot;:37.606044}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Бибирево,<br>
&nbsp;ул. Плещеева, д.&nbsp;1 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="670" data-balloon-content="" data-shop="{&quot;lat&quot;:55.782833,&quot;lan&quot;:37.729796}" data-metro="м." Семеновская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.782833,&quot;lan&quot;:37.729796}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Семеновская,<br>
&nbsp;ул. Щербаковская, д.&nbsp;35 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-19:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="671" data-balloon-content="" data-shop="{&quot;lat&quot;:55.820069,&quot;lan&quot;:37.580409}" data-metro="м." Тимирязевская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.820069,&quot;lan&quot;:37.580409}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Тимирязевская,<br>ул. Яблочкова, д.21</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-17:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="672" data-balloon-content="" data-shop="{&quot;lat&quot;:55.773890,&quot;lan&quot;:37.580072}" data-metro="м." Белорусская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.773890,&quot;lan&quot;:37.580072}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Белорусская,<br>
&nbsp;Грузинский переулок, д.&nbsp;16 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-17:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="674" data-balloon-content="" data-shop="{&quot;lat&quot;:55.758392,&quot;lan&quot;:37.552743}" data-metro="м." Улица="" 1905="" года="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.758392,&quot;lan&quot;:37.552743}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Улица 1905 года,<br>
&nbsp;Шмитовский проезд, д.&nbsp;9/5 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-19:30
<br>сб: 07:30- 16:30
<br>вс: 07:30- 14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="676" data-balloon-content="" data-shop="{&quot;lat&quot;:55.865074,&quot;lan&quot;:37.476272}" data-metro="м." Беломорская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.865074,&quot;lan&quot;:37.476272}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Беломорская,<br>
&nbsp;ул. Беломорская, д.&nbsp;26 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="677" data-balloon-content="" data-shop="{&quot;lat&quot;:55.797946,&quot;lan&quot;:37.722241}" data-metro="м." Преображенская="" площадь="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.797946,&quot;lan&quot;:37.722241}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Преображенская площадь,<br>
&nbsp;Большая Черкизовская, д.&nbsp;9А &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-19:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="679" data-balloon-content="" data-shop="{&quot;lat&quot;:55.810209,&quot;lan&quot;:37.810952}" data-metro="м." Щелковская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.810209,&quot;lan&quot;:37.810952}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Щелковская,<br>
&nbsp; Щелковское шоссе, д.&nbsp;74 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="683" data-balloon-content="" data-shop="{&quot;lat&quot;:55.971004,&quot;lan&quot;:37.175083}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.971004,&quot;lan&quot;:37.175083}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">г.Зеленоград,<br>
&nbsp;корпус 2044 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-17:30
<br>сб: 07:30-15:30
<br>вс: 07:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="684" data-balloon-content="" data-shop="{&quot;lat&quot;:55.817402,&quot;lan&quot;:37.569311}" data-metro="м." Тимирязевская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.817402,&quot;lan&quot;:37.569311}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Тимирязевская,<br>
&nbsp; ул. Дубки, д.&nbsp;2А &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-17:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="685" data-balloon-content="" data-shop="{&quot;lat&quot;:55.752639,&quot;lan&quot;:37.532581}" data-metro="м." Международная="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.752639,&quot;lan&quot;:37.532581}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Международная,<br>
&nbsp;ул. Тестовская, д.&nbsp;10 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-19:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="686" data-balloon-content="" data-shop="{&quot;lat&quot;:55.807520,&quot;lan&quot;:37.518996}" data-metro="м." Сокол="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.807520,&quot;lan&quot;:37.518996}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Сокол,<br>
&nbsp;ул. Усиевича, д.&nbsp;д 29, к. 1 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="690" data-balloon-content="" data-shop="{&quot;lat&quot;:55.794744,&quot;lan&quot;:37.490531}" data-metro="м." Октябрьское="" Поле="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.794744,&quot;lan&quot;:37.490531}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Октябрьское Поле,<br>
&nbsp;ул. Маршала Бирюзова, д.&nbsp;21 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-17:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="692" data-balloon-content="" data-shop="{&quot;lat&quot;:55.808339,&quot;lan&quot;:37.635528}" data-metro="м." Алексеевская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.808339,&quot;lan&quot;:37.635528}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Алексеевская,<br>
&nbsp;проспект Мира, д.&nbsp;95 стр. 2 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-19:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="693" data-balloon-content="" data-shop="{&quot;lat&quot;:55.774954,&quot;lan&quot;:37.474439}" data-metro="м." Народное="" Ополчение="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.774954,&quot;lan&quot;:37.474439}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Народное Ополчение,<br>
&nbsp;проспект Маршала Жукова, д.&nbsp;35 к1 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-19:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="694" data-balloon-content="" data-shop="{&quot;lat&quot;:55.817198,&quot;lan&quot;:37.369779}" data-metro="м." Мякинино="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.817198,&quot;lan&quot;:37.369779}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Красногорск,<br>
м.&nbsp;Мякинино,<br>
&nbsp;Ильинский бульвар, д.&nbsp;8 &nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-17:30
<br>сб: 07:30-15:30
<br>вс: 07:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="695" data-balloon-content="" data-shop="{&quot;lat&quot;:55.868525,&quot;lan&quot;:37.669259}" data-metro="м." Бабушкинская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.868525,&quot;lan&quot;:37.669259}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Бабушкинская,<br>
&nbsp;ул. Менжинского, д.&nbsp;21&nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-18:00
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="703" data-balloon-content="" data-shop="{&quot;lat&quot;:55.895594,&quot;lan&quot;:37.713357}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.895594,&quot;lan&quot;:37.713357}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Московская область,<br>
г.&nbsp;Мытищи,<br>
&nbsp;ул. Веры Волошиной, д.&nbsp;46&nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-14:00
<br>сб: 07:30-13:30
<br>вс: выходной</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="708" data-balloon-content="" data-shop="{&quot;lat&quot;:55.751975,&quot;lan&quot;:37.873507}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.751975,&quot;lan&quot;:37.873507}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Московская область,<br>
г.&nbsp;Реутов,<br>
&nbsp; Юбилейный проспект, д.&nbsp;41&nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-17:30
<br>сб: 07:30-15:30
<br>вс: 07:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="709" data-balloon-content="" data-shop="{&quot;lat&quot;:55.886329,&quot;lan&quot;:37.420272}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.886329,&quot;lan&quot;:37.420272}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Московская область,<br>
г.&nbsp;Химки,<br>
&nbsp;Юбилейный проспект, д.&nbsp;5, стр.1&nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб: 07:30-15:30
<br>вс: 07:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="711" data-balloon-content="" data-shop="{&quot;lat&quot;:55.789761,&quot;lan&quot;:37.784516}" data-metro="м." Измайловская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.789761,&quot;lan&quot;:37.784516}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp; Измайловская,<br>
&nbsp;  ул. 3-я Парковая, д.&nbsp;6&nbsp;</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:30-17:30
<br>сб: 07:30-16:30
<br>вс: 07:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="412" data-balloon-content="" data-shop="{&quot;lat&quot;:55.741123,&quot;lan&quot;:37.539800}" data-metro="м.Кутузовская">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.741123,&quot;lan&quot;:37.539800}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/blue.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.Кутузовская,<br>
Кутузовский проспект, д.&nbsp;33</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-19:00
<br>сб. 07:00-16:00
<br>вс. 07:00 - 14:00</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="451" data-balloon-content="" data-shop="{&quot;lat&quot;:55.850110,&quot;lan&quot;:37.355399}" data-metro="м." Митино="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.850110,&quot;lan&quot;:37.355399}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/blue.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Митино,<br>
ул.&nbsp;Митинская, д.&nbsp;48, помещ.&nbsp;7</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="477" data-balloon-content="" data-shop="{&quot;lat&quot;:55.816642,&quot;lan&quot;:37.498617}" data-metro="м." Войковская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.816642,&quot;lan&quot;:37.498617}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Войковская,<br>
Ленинградское шоссе, д.&nbsp;9, корп.&nbsp;1</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="482" data-balloon-content="" data-shop="{&quot;lat&quot;:55.820789,&quot;lan&quot;:37.376842}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.820789,&quot;lan&quot;:37.376842}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Красногорск, Красногорский б-р, д.26.пом.4</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт 7:00-17:00
<br>сб. 07:30-15:30
<br>вс 7:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="225" data-balloon-content="" data-shop="{&quot;lat&quot;:55.870127,&quot;lan&quot;:37.634029}" data-metro="м." Бабушкинская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.870127,&quot;lan&quot;:37.634029}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/orange.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Бабушкинская,<br>
пр-д Дежнева, д.&nbsp;27корп.1</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="226" data-balloon-content="" data-shop="{&quot;lat&quot;:55.780116,&quot;lan&quot;:37.664809}" data-metro="м." Красносельская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.780116,&quot;lan&quot;:37.664809}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/red.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Красносельская,<br>
ул.&nbsp;В.&nbsp;Красносельская, д.&nbsp;34</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="228" data-balloon-content="" data-shop="{&quot;lat&quot;:55.783175,&quot;lan&quot;:37.600684}" data-metro="м." Менделеевская="" м.="" Новослободская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.783175,&quot;lan&quot;:37.600684}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/gray.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Менделеевская&nbsp;/&nbsp;м.&nbsp;Новослободская,<br>
ул.&nbsp;Сущевская, д.&nbsp;27, стр.&nbsp;2</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="230" data-balloon-content="" data-shop="{&quot;lat&quot;:55.743773,&quot;lan&quot;:37.401534}" data-metro="м." Молодежная="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.743773,&quot;lan&quot;:37.401534}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/blue.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Молодежная,<br>
ул.&nbsp;Оршанская, д.&nbsp;13</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-17:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="231" data-balloon-content="" data-shop="{&quot;lat&quot;:55.78979,&quot;lan&quot;:37.633221}" data-metro="м." Рижская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.78979,&quot;lan&quot;:37.633221}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/orange.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Рижская,<br>
ул.&nbsp;Гиляровского, д.&nbsp;65, п.&nbsp;8</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:00-17:00
<br>вс: 7:00-15:00</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="232" data-balloon-content="" data-shop="{&quot;lat&quot;:55.846743,&quot;lan&quot;:37.440398}" data-metro="м." Сходненская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.846743,&quot;lan&quot;:37.440398}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/violet.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Сходненская,<br>
ул.&nbsp;Сходненская, д.&nbsp;46/14</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн- пт: 7:00-19:00 
<br>сб: 7:30-16:30 
<br>вс: 7:30- 14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="233" data-balloon-content="" data-shop="{&quot;lat&quot;:55.744142,&quot;lan&quot;:37.656923}" data-metro="м." Таганская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.744142,&quot;lan&quot;:37.656923}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/violet.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Таганская,<br>
Б.&nbsp;Дровяной пер., д.&nbsp;8, стр.&nbsp;1</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:00-16:00
<br>вс: 7:00-15:00</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="234" data-balloon-content="" data-shop="{&quot;lat&quot;:55.803571,&quot;lan&quot;:37.813617}" data-metro="м." Щелковская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.803571,&quot;lan&quot;:37.813617}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/blue.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Щелковская,<br>
Сиреневый Бульвар, д.&nbsp;51</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="246" data-balloon-content="" data-shop="{&quot;lat&quot;:55.9478185,&quot;lan&quot;:37.5015898}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.9478185,&quot;lan&quot;:37.5015898}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Долгопрудный, пр-т Пацаева, д.&nbsp;7, к.&nbsp;5</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00, 
<br>сб: 7:30-15:30, 
<br>вс: 7:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="249" data-balloon-content="" data-shop="{&quot;lat&quot;:55.9245643,&quot;lan&quot;:37.8206791}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.9245643,&quot;lan&quot;:37.8206791}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Королев, Стрекалова, д.&nbsp;2</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-15:30
<br>вс: 7:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="256" data-balloon-content="" data-shop="{&quot;lat&quot;:55.888868,&quot;lan&quot;:37.414528}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.888868,&quot;lan&quot;:37.414528}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Химки, Юбилейный пр-т, д.&nbsp;60</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-15:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="236" data-balloon-content="" data-shop="{&quot;lat&quot;:55.876652,&quot;lan&quot;:37.665574}" data-metro="м." Бабушкинская="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.876652,&quot;lan&quot;:37.665574}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/orange.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Бабушкинская,<br>
ул.&nbsp;Енисейская, д.&nbsp;37, стр.&nbsp;1 (офис при лаборатории)</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 07:00-20:00
<br>сб: 07:30-19:30
<br>вс: 07:30-19:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="238" data-balloon-content="" data-shop="{&quot;lat&quot;:55.802391,&quot;lan&quot;:37.402525}" data-metro="м." Строгино="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.802391,&quot;lan&quot;:37.402525}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/blue.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Строгино,<br>
Строгинский б-р, д.&nbsp;26, корп.&nbsp;2</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="239" data-balloon-content="" data-shop="{&quot;lat&quot;:55.760413,&quot;lan&quot;:37.406522}" data-metro="м." Крылатское="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.760413,&quot;lan&quot;:37.406522}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--metro" style="background-image: url(templates/images/metro-icons/map/blue.svg)"></i>
                  <span class="address__item-title">Москва,<br>
м.&nbsp;Крылатское,<br>
Осенний бульвар, д.&nbsp;15</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн: 7:00-19:00
<br>вт:7:00-19:00
<br>ср:7:00-19:00
<br>чт:7:00-19:00
<br>пт: 7:00-19:00
<br>сб: 7:30-16:30
<br>вс: 7:30-14:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="258" data-balloon-content="" data-shop="{&quot;lat&quot;:55.909877,&quot;lan&quot;:37.723349}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.909877,&quot;lan&quot;:37.723349}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Мытищи, ул.&nbsp;Летная, д.&nbsp;21</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-15:30
<br>вс: 7:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="260" data-balloon-content="" data-shop="{&quot;lat&quot;:55.746988,&quot;lan&quot;:37.861573}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.746988,&quot;lan&quot;:37.861573}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Реутов, ул.Южная, д.&nbsp;10</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-17:00
<br>сб: 7:30-15:30
<br>вс: 7:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div><div style="display: block" class="address__item" data-id="259" data-balloon-content="" data-shop="{&quot;lat&quot;:55.795408,&quot;lan&quot;:37.934741}" data-metro="">
          <div class="js-adress-item" data-item-coords="{&quot;lat&quot;:55.795408,&quot;lan&quot;:37.934741}">
              <div class="address__item-header">
                  <i class="address__icon address__icon--map" style="background-image: url(templates/images/metro-icons/map/default.svg)"></i>
                  <span class="address__item-title">Балашиха, ул.&nbsp;Советская, д.&nbsp;2/9</span>
                  <i class="address__chevron-down"></i>
              </div>
              <div class="address__hiden-block">
                  <div class="address__address">
                      <div class="address__work-time">Сегодня уже закрыт</div>
                  </div>
                  <div class="address__time-and-phone">
                      <div class="address__time">
                          <div>пн-пт: 7:00-19:00
<br>сб: 7:30-15:30
<br>вс: 7:30-13:30</div>
                      </div>
                  </div>
                  
                      
              </div>
          </div>
      </div>
                        <div class="address__btn-wr">
                            <a href="javascript:void(0)" class="btn address__show-all" data-not-ajax="true">Показать еще</a>
                        </div>
                    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  </div>
                </div>"""
url = 'https://kdl.ru/analizy-i-tseny/obshiy-analiz-kala-koprogramma'
user_agent = UserAgent().random
headers = {"User-Agent": user_agent}
bs = BeautifulSoup(page, 'html.parser')
labs_a_elements = bs.findAll('span', class_='address__item-title')
result = []
print(len(labs_a_elements))
for item in labs_a_elements:
    if not "Москва" in item.text:
        continue
    split_item = item.text.split('\n')
    try:
        result.append(
            {
                "metro_station": split_item[1].strip().replace('\xa0', '').replace('м.', '').replace(',', '').strip(),
                "address": split_item[2].strip().replace('\xa0', '')
            }
        )
    except:
        pass

with open('kdl-branches.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)


