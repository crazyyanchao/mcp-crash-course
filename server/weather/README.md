# TEST SERVER FROM CLAUDE DESKTOP

## INSTALL SERVER

```json
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "D:/workspace/mcp/mcp-crash-course/server/weather",
                "run",
                "sse.py"
            ]
        }
    }
}
```

## TEST QUERY

### 萨克拉门托的天气怎么样？

要查看萨克拉门托的天气，我需要使用其地理坐标。萨克拉门托位于加利福尼亚州，我将使用它的地理坐标来获取天气预报。

- View Result from get-forecast from weather (local)

```
{
  `latitude`: 38.5816,
  `longitude`: -121.4944
}
Forecast for 38.5816, -121.4944:
```

让我用中文为您详细解释萨克拉门托的天气预报：

明天（周三）的天气是：

- 温度：57华氏度（约14摄氏度）
- 风向：南风，风速很轻
- 天气状况：开始有轻微雾霾，之后以晴天为主

接下来几天的天气特点：

- 周四：温度56华氏度，可能会有小雨
- 周五：温度54华氏度，有小雨机会
- 周六：温度55华氏度，有小雨
- 周日：温度55华氏度，以晴天为主
- 周一：温度52华氏度，有小雨机会

总的来说，萨克拉门托本周天气以阴凉为主，温度在50-57华氏度之间，有几天会有小雨，也会有晴天间隔。建议准备一件外套和雨伞。

### 德克萨斯州有哪些有效天气警报？

我可以帮您查询德克萨斯州当前的天气警报。让我使用天气警报查询工具获取最新信息。

- View Result from get-alerts from weather (local)

```
{
  `state`: `TX`
}

Active alerts for TX:

Event: Rip Current Statement
Area: Kenedy Island; Willacy Island; Cameron Island
Severity: Moderate
Status: Actual
Headline: Rip Current Statement issued December 11 at 2:32AM CST until December 11 at 6:00PM CST by NWS Brownsville TX
---
Event: High Surf Advisory
Area: Kenedy Island; Willacy Island; Cameron Island
Severity: Minor
Status: Actual
Headline: High Surf Advisory issued December 11 at 2:32AM CST until December 11 at 6:00PM CST by NWS Brownsville TX
---
Event: Freeze Warning
Area: Terrell; Chisos Basin; Presidio Valley; Lower Brewster County
Severity: Moderate
Status: Actual
Headline: Freeze Warning issued December 11 at 1:59AM CST until December 11 at 9:00AM CST by NWS Midland/Odessa TX
---
Event: Flood Warning
Area: Nacogdoches, TX; Rusk, TX; San Augustine, TX; Shelby, TX
Severity: Severe
Status: Actual
Headline: Flood Warning issued December 10 at 11:07PM CST until December 12 at 1:30AM CST by NWS Shreveport LA
---
Event: Flood Warning
Area: Angelina, TX; Cherokee, TX; Nacogdoches, TX
Severity: Severe
Status: Actual
Headline: Flood Warning issued December 10 at 11:07PM CST until December 16 at 12:00PM CST by NWS Shreveport LA
---
Event: Freeze Watch
Area: La Salle; McMullen; Live Oak; Bee; Goliad; Victoria; Webb
Severity: Minor
Status: Actual
Headline: The Freeze Watch has been cancelled.
---
Event: Wind Advisory
Area: Aransas Islands; Kleberg Islands; Nueces Islands; Calhoun Islands
Severity: Minor
Status: Actual
Headline: The Wind Advisory has been cancelled.
---
Event: Freeze Warning
Area: Terrell; Chisos Basin; Presidio Valley; Lower Brewster County
Severity: Moderate
Status: Actual
Headline: Freeze Warning issued December 10 at 10:44PM CST until December 11 at 9:00AM CST by NWS Midland/Odessa TX
---
Event: Freeze Warning
Area: Houston; Trinity; Madison; Walker; San Jacinto; Polk; Burleson; Brazos; Washington; Grimes; Montgomery; Colorado; Austin; Waller
Severity: Moderate
Status: Actual
Headline: Freeze Warning issued December 10 at 9:42PM CST until December 11 at 8:00AM CST by NWS Houston/Galveston TX
---
Event: Wind Advisory
Area: Chambers; Coastal Jackson; Coastal Matagorda; Coastal Brazoria; Coastal Galveston; Matagorda Islands; Brazoria Islands; Galveston Island; Bolivar Peninsula
Severity: Moderate
Status: Actual
Headline: Wind Advisory issued December 10 at 9:42PM CST until December 11 at 12:00AM CST by NWS Houston/Galveston TX
---
Event: Freeze Warning
Area: Llano; Burnet; Williamson; Val Verde; Edwards; Real; Kerr; Bandera; Gillespie; Kendall; Blanco; Hays; Travis; Bastrop; Lee; Kinney; Uvalde; Medina; Bexar; Comal; Guadalupe; Caldwell; Fayette; Maverick; Zavala; Frio; Atascosa; Wilson; Karnes; Gonzales; De Witt; Lavaca; Dimmit
Severity: Moderate
Status: Actual
Headline: Freeze Warning issued December 10 at 7:48PM CST until December 11 at 8:00AM CST by NWS Austin/San Antonio TX
---
Event: High Surf Advisory
Area: Kenedy Island; Willacy Island; Cameron Island
Severity: Minor
Status: Actual
Headline: High Surf Advisory issued December 10 at 7:36PM CST until December 11 at 6:00PM CST by NWS Brownsville TX
---
Event: Rip Current Statement
Area: Kenedy Island; Willacy Island; Cameron Island
Severity: Moderate
Status: Actual
Headline: Rip Current Statement issued December 10 at 7:36PM CST until December 11 at 6:00PM CST by NWS Brownsville TX
---
Event: Wind Advisory
Area: Inland Kenedy; Inland Willacy; Inland Cameron; Coastal Kenedy; Coastal Willacy; Coastal Cameron; Kenedy Island; Willacy Island; Cameron Island
Severity: Minor
Status: Actual
Headline: The Wind Advisory has been cancelled.
---
Event: Freeze Watch
Area: La Salle; McMullen; Live Oak; Bee; Goliad; Victoria; Webb
Severity: Severe
Status: Actual
Headline: Freeze Watch issued December 10 at 2:58PM CST until December 11 at 8:00AM CST by NWS Corpus Christi TX
---
Event: Wind Advisory
Area: Aransas Islands; Kleberg Islands; Nueces Islands; Calhoun Islands
Severity: Moderate
Status: Actual
Headline: Wind Advisory issued December 10 at 2:58PM CST until December 11 at 12:00AM CST by NWS Corpus Christi TX
---
Event: Freeze Warning
Area: Houston; Trinity; Madison; Walker; San Jacinto; Burleson; Brazos; Washington; Grimes; Montgomery
Severity: Moderate
Status: Actual
Headline: Freeze Warning issued December 10 at 2:27PM CST until December 11 at 8:00AM CST by NWS Houston/Galveston TX
---
Event: Freeze Warning
Area: Polk; Colorado; Austin; Waller
Severity: Moderate
Status: Actual
Headline: Freeze Warning issued December 10 at 2:27PM CST until December 11 at 8:00AM CST by NWS Houston/Galveston TX
---
Event: Freeze Watch
Area: Houston; Trinity; Madison; Walker; San Jacinto; Burleson; Brazos; Washington; Grimes; Montgomery
Severity: Severe
Status: Actual
Headline: The Freeze Watch has been replaced. Please see the latest information from NWS Houston/Galveston TX on this developing situation.
---
Event: Wind Advisory
Area: Chambers; Coastal Jackson; Coastal Matagorda; Coastal Brazoria; Coastal Galveston; Matagorda Islands; Brazoria Islands; Galveston Island; Bolivar Peninsula
Severity: Moderate
Status: Actual
Headline: Wind Advisory issued December 10 at 2:27PM CST until December 11 at 12:00AM CST by NWS Houston/Galveston TX
---
```

根据最新的天气警报信息，德克萨斯州目前有以下有效的天气警报：

1. 低温警报（Freeze Warning）：
    - 地区包括特雷尔县、布雷斯特县、休斯顿、三一县、麦迪逊县等多个地区。
    - 大多数警报预计将持续到今天（12月11日）上午8:00或9:00。

2. 洪水警告（Flood Warning）：
    - 涉及地区：
        * 纳科多奇斯县
        * 拉斯克县
        * 圣奥古斯丁县
        * 谢尔比县
        * 安杰利娜县
        * 切罗基县
    - 这些洪水警告将持续到12月12日凌晨1:30或12月16日中午12:00。

3. 海浪和海岸警报：
    - 肯尼迪岛、威拉西岛和卡梅隆岛有：
        * 高浪警报（High Surf Advisory）
        * 湍流警报（Rip Current Statement）
    - 这些海岸警报将持续到今天（12月11日）下午6:00。

4. 风力警报：
    - 一些地区的风力警报已经取消。

请注意，这些警报可能会随时变化，建议您持续关注当地气象部门的最新通知，特别是如果您计划在这些地区出行或活动。


