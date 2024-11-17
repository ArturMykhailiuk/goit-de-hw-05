# goit-de-hw-05
## 1.Створення трьох топіків для відправки даних
![p1](https://github.com/user-attachments/assets/4f5172ff-bf66-48ed-a321-112a28de8951)  
Підтвердженням існування топіків є їх наявність в <b>admin_client.list_topics()</b>, що відображено у скріншоті. Перші три рядки підтверджують їх створення, а наступні три рядки підтверджують їх наявність і можливість використання

## 2.Генерація даних сенсорів та відправки даних в building_sensors
![p2](https://github.com/user-attachments/assets/42ef473b-5ddf-4b33-8d50-6c91aba7918f)
У скріншоті відображено виклик програми 5 разів, що підтверджується 5 рядками у терміналі. Дані успішно згенеровані. Всім ключам з об’єкту <b>data</b> присвоєно значення. Доказом успішної відправки даних в building_sensors є відсутність помилок.

## 3.Отримання даних та фільтрації саме тих даних, що будуть далі використані
![p3](https://github.com/user-attachments/assets/8a102edb-eb81-4c91-a5c7-8adb8fc51c3e)
У даному скріншоті відображено дані отримані з <b>building_sensors</b>. А також зазначено, яке саме повідомлення в подальшому буде відправлено або в <b>temperature_alerts</b> або в <b>humidity_alerts</b> в залежності від застосованої фільтрації.

## 4.Демонстрація того, що відфільтровані дані були послані у відповідні топіки
![p4](https://github.com/user-attachments/assets/619ae167-35dd-4ff7-8145-ceaac3ef63be)
Доказом відправки відфільтрованих даних по відповідним топікам є відсутність помилок при спробі відправки та повідомлення про успішну відправку з відповідного фільтру.

## 5.Результат запису відфільтрованих даних
![p5](https://github.com/user-attachments/assets/43285d0a-f478-41f0-a6ae-fc60ba528536)
Результатом запису відфільтрованих даних є їх знаходження у відповідному топіку. На вищевказаному скріншоті ми маємо можливість переконатись, що дані дійсно записані в топіках шляхом отримання повідомлень з цих топіків. Ключі підкреслені червоним кольором у скріншоті співпадають з попереднім скріншотом про відправку даних. Інші повідомлення прошу ігнорувати - результати попередніх тестувань.

