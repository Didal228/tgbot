import telebot
from telebot import types


bot = telebot.TeleBot('7092670853:AAFf8bOblJQ8cMZH7_3at64snwKfneCFowk')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('7.36')
    itembtn2 = types.KeyboardButton('7.35')
    itembtn3 = types.KeyboardButton('7.34')
    itembtn4 = types.KeyboardButton('7.33')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Здравстуй игрок. Я бот который вам подскажет 'мету' патчей героя. Выберите патч который вас интересует:", reply_markup=markup)

                        #1 патчик


@bot.message_handler(func=lambda message: message.text == '7.36')
def start(message1):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton('Керри', callback_data='button1')
    button2 = types.InlineKeyboardButton('Мидер', callback_data='button2')
    button3 = types.InlineKeyboardButton('Тройка', callback_data='button3')
    button4 = types.InlineKeyboardButton('Частичная поддержка', callback_data='button4')
    button5 = types.InlineKeyboardButton('Полная поддержка', callback_data='button5')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message1.chat.id, "Вы выбрали патч 7.36. Какая роль вас интересует?:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    button_text = call.data
    chat_id1 = call.message.chat.id

    if button_text == 'button1':
        bot.send_message(chat_id1, "Templar Assassin Что изменил патч? В патче 7.36 Valve изменила механику работы Refraction: теперь способность не даёт стаки, блокирующие урон;вместо это Refraction Refraction даёт несколько зарядов барьеров. Основная разница в том, что теперь Темпларка не так сильно боится случайных тычек от крипов и периодического урона. Благодаря этому усилению и ряду других изменений персонаж стал одним из сильнейших керри в игре, даже несмотря на ослабления в патче 7.36. (93% выбор, 58% винрейт)")
    elif button_text == 'button2':
        bot.send_message(chat_id1, "Zeus Что изменил патч? Концептуально герой не поменялся, лишь получил назад Static Field в качестве врождённой способности, а также мощный аспект, значительно повышающий его урон на дистанции. (72% выбор, 58% винрейт)")
    elif button_text == 'button3':
        bot.send_message(chat_id1, "Legion Commander Что изменил патч? Главная имба первых дней патча, которую потом немного ослабили. Всё дело в одном из аспектов, который даёт Легионке барьер за использование Overwhelming Odds, делая из неё неубиваемого оффлейнера. Кроме этого, Moment of Courage стал врождённой способностью. (99% выбор, 54% винрейт)")
    elif button_text == 'button4':
        bot.send_message(chat_id1, "Spirit Breaker Что изменил патч? Бара получил несколько важных усилений. Во-первых, это врождённая способность, увеличивающая получение опыта. Во-вторых, это возможность использовать Charge of Darkness на героя в Black King Bar без покупки Aghanim's Scepter. В-третьих, перечень небольших баффов, включая мощный аспект. (91% выбор, 56% винрейт)")
    elif button_text == 'button5':
        bot.send_message(chat_id1, "Venomancer Что изменил патч? На самом деле, в патче 7.36 Valve, скорее, пофиксила Venomancer, который и до этого пользовался популярностью. Однако, видимо, ослаблений не хватило, особенно после того, как Poison Sting стала врождённой способностью, поэтому Веномансер до сих пор остаётся очень популярным саппортом. (92% выбор, 55% винрейт)")

                       #2 патчик


@bot.message_handler(func=lambda message: message.text == '7.35')
def start(message2):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button6 = types.InlineKeyboardButton('Керри', callback_data='button6')
            button7 = types.InlineKeyboardButton('Мидер', callback_data='button7')
            button8 = types.InlineKeyboardButton('Тройка', callback_data='button8')
            button9 = types.InlineKeyboardButton('Частичная поддержка', callback_data='button9')
            button10 = types.InlineKeyboardButton('Полная поддержка', callback_data='button10')
            markup.add(button6, button7, button8, button9, button10)
            bot.send_message(message2.chat.id, "Вы выбрали патч 7.35 .Какая роль вас интересует?:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
            button_text = call.data
            chat_id2 = call.message.chat.id

            if button_text == 'button6':
                bot.send_message(chat_id2, "Faceless Void Что изменилось в 7.35:— прирост силы за уровень увеличен на 0,2— усилены таланты на 10 и 15 уровнеСам Войд почти не изменился, зато под него подстроилась мета — эффективность выросла почти на 5% и составляет 53,1%. Прямо сейчас это один из лучших керри.РекламаValve апнула все, что так любит собирать Faceless Void в начале игры. Maelstrom дает больше скорости атаки, Javelin стоит дешевле, бонус к урону от Mask of Madness также увеличен — и с таким недорогим набором чар уже выглядит имбой.")
            elif button_text == 'button7':
                bot.send_message(chat_id2, "Outworld Destroyer Что изменилось в 7.35:— радиус Sanity's Eclipse на первых уровнях увеличен— теперь талант 20 уровня дает бонус не к силе, а к вампиризму заклинаниямиИнтересный пример: если большинство персонажей из нашего списка моментально взлетали вверх в таблице винрейта, то OD набирал эффективность постепенно.Это легко объяснить, ведь на первый взгляд героя бафнули совсем слегка. Только на практике выяснилось, насколько силен новый талант и как круто Destroyer заходит.По итогу сейчас OD уже выигрывает 58,7% игр и винрейт продолжает расти. Это лучший герой для мид-линии, игра на котором может неплохо забустить ваш MMR.")
            elif button_text == 'button8':
                bot.send_message(chat_id2, "Timbersaw Что изменилось в 7.35:— базовая сила и ее прирост за уровень увеличены— число от атак и максимум эффектов от Reactive Armor увеличены— таланты 10 и 15 уровня изменены в сторону улучшенияВ новом патче Риззрак однозначно стал лучшим героем для игры на третьей позиции. Персонаж и до обновления был силен в умелых руках, а теперь же стал настоящей имбой — винрейт вырос 8,6% и достиг отметки 53,5% побед.")
            elif button_text == 'button9':
                bot.send_message(chat_id2, "Witch DoctorЧто изменилось в 7.35:— Voodoo Restoration больше не наносит урон— лечение от Voodoo Restoration немного увеличено— талант 25 уровня немного усиленНельзя сказать, что персонаж стал намного сильнее. Но он не стал слабее, что для Witch Doctor уже отлично — герой был имбой в 7.34 и остался ей в 7.35.Жарвакко входит в топ-5 по проценту побед в пабликах (55,1%) и является самым сильным персонажем поддержки. Саппорт на все случаи жизни, который хорош как на линии, так и в поздней стадии игры.")
            elif button_text == 'button10':
                bot.send_message(chat_id2, "Vengeful SpiritЧто изменилось в 7.35:— урон Nether Swap увеличен— Nether Swap больше не уменьшает урон, но теперь дает герою и союзникам барьер, здоровье которого равно урону способности— улучшены три таланта на 15, 20 и 25 уровняхВенга в 7.35 получила ряд баффов. Прежде всего, ультимейт стал намного сильнее, к тому же выросли бонусы от талантов. В итоге герой стал выигрывать на 3,4% чаще и замыкает десятку сильнейших с винрейтом 53,5%.Важно и то, что персонаж хорошо работает против героев с большим количеством брони: это и Wave of Terror, и ульт, и возможность купить Medallion of Courage. Если играете на саппорте — это без вопросов один из лучших вариантов на 4 или 5 позицию.")

                    #3 патчик


@bot.message_handler(func=lambda message: message.text == '7.34')
def start(message3):
                    markup = types.InlineKeyboardMarkup(row_width=2)
                    button11 = types.InlineKeyboardButton('Керри', callback_data='button11')
                    button12 = types.InlineKeyboardButton('Мидер', callback_data='button12')
                    button13 = types.InlineKeyboardButton('Тройка', callback_data='button13')
                    button14 = types.InlineKeyboardButton('Частичная поддержка', callback_data='button14')
                    button15 = types.InlineKeyboardButton('Полная поддержка', callback_data='button15')
                    markup.add(button11, button12, button13, button14, button15)
                    bot.send_message(message3.chat.id, "Вы выбрали патч 7.34. Какая роль вас интересует?:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
                    button_text = call.data
                    chat_id3 = call.message.chat.id
                    message_id = call.message.message_id

                    if button_text == 'button11':
                        bot.send_message(chat_id3, "1")
                    elif button_text == 'button12':
                        bot.send_message(chat_id3, " 2")
                    elif button_text == 'button13':
                        bot.send_message(chat_id3, " 3")
                    elif button_text == 'button14':
                        bot.send_message(chat_id3, "4")
                    elif button_text == 'button15':
                        bot.send_message(chat_id3, " 5")

                             #4 патчик


@bot.message_handler(func=lambda message: message.text == '7.33')
def start(message4):
                            markup = types.InlineKeyboardMarkup(row_width=2)
                            button16 = types.InlineKeyboardButton('Керри', callback_data='button16')
                            button17 = types.InlineKeyboardButton('Мидер', callback_data='button17')
                            button18 = types.InlineKeyboardButton('Тройка', callback_data='button18')
                            button19 = types.InlineKeyboardButton('Частичная поддержка', callback_data='button19')
                            button20 = types.InlineKeyboardButton('Полная поддержка', callback_data='button20')
                            markup.add(button16, button17, button18, button19, button20)
                            bot.send_message(message4.chat.id, "Вы выбрали патч 7.33. Какая роль вас интересует?:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
                            button_text = call.data
                            chat_id4 = call.message.chat.id
                            message_id = call.message.message_id

                            if button_text == 'button16':
                                bot.send_message(chat_id4, "1")
                            elif button_text == 'button17':
                                bot.send_message(chat_id4, "2")
                            elif button_text == 'button18':
                                bot.send_message(chat_id4, "3")
                            elif button_text == 'button19':
                                bot.send_message(chat_id4, "4")
                            elif button_text == 'button20':
                                bot.send_message(chat_id4, "5")


bot.polling(none_stop=True)


