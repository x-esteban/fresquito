**Fresquito** is a weekend project aiming to display on a website the coldest and hottest town in Spain, in (almost) real time.
The service is self-hosted on a **Raspberry Pi 4B** running **Nginx**.

The script running on the pi performs the following:
   1. Scrapes the meteorological data for every town in Spain from ElTiempo.es
   2. Saves the data as a Dataframe and exports it as a .csv (*output.csv*).
   3. Filters the resulting data to find the coldest and hottest town(s). If there's a draw, one of the towns is chosen randomly.
   4. Creates an interactive map with **Folium**, placing a tooltip on both towns that displays the town name, province and temperature. 
   5. Exports the map as an .html file.

This script runs automatically every 20 minutes via a crontab. Another crontab sends the file to the required **Nginx** folder with the necessary permissions.
You can find the **Fresquito** website on the following link:

www.fresquito.es

For more information hit me up at info@xesteban.com 😉
