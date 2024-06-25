# Teltonika-GPS-forwarding-via-HTTP-for-ROS2
ROS2 (Humble) Package that publishes GPS Data from a Teltonika router (tested with RUTX50) via HTTP forwarding


## How to run it

Install Python library for the NMEA 0183 protcol:
```bash
pip install pynmea2
```
### 1.) Build from source: 
Put the files inside a ros workspace, in the src folder: 
```bash
git clone https://github.com/TKL01/Teltonika-GPS-forwarding-via-HTTP-for-ROS2.git
```
then build outside of the src folder:
```bash
colcon build 
```
source it, for example if the files are located in the ros2_ws workspace folder (~/ros2_ws/install/setup.bash)
```bash
source ~/ros2_ws/install/setup.bash
```
### 2.) GPS configuration in the Teltonika Web Interface 
Enable GPS and NMEA:
![image](https://github.com/TKL01/Teltonika-GPS-forwarding-via-HTTP-for-ROS2/assets/120031026/664553bd-0a30-4548-8cb5-aa9c5486c52c)

Set HTTP Server Settings. Put in your machine's IP, the default port is :3000 and the forwarding Interval:
![Screenshot from 2024-06-24 15-30-19](https://github.com/TKL01/Teltonika-GPS-forwarding-via-HTTP-for-ROS2/assets/120031026/73be206e-e723-4fb7-9888-8d424efe23a8)

### 3.) Open 2 new terminals and run:
```bash
ros2 run gps_tools gps_server
```
```bash
ros2 run gps_tools gps_publisher
```
