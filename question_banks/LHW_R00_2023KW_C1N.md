---
schema_version: will-ai-question-bank/v1
source_pdf: LHW_R00_2023KW_C1N.pdf
source_sha256: 9d4fe66046dd69a803ca21aca3f35a52d58fe566d10577d5e7a72b5a7a69e27f
source_pages: 52
question_bank_version: V1
product_scope: LHW
---

# LHW_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LHW_R00_2023KW_C1N.pdf`
- SHA-256: `9d4fe66046dd69a803ca21aca3f35a52d58fe566d10577d5e7a72b5a7a69e27f`
- 物理页数: 52
- Product: KOSMEK LHW 传感器内置式低压油压复动旋转式夹紧器
- 来源证据原则: PDF 页面及其表格、公式、曲线、状态图和文字为 Source Truth；文字识别只用于定位，型号、数值及视觉关系以页面证据为准。

## 2. Scope

### 2.1 产品与文档范围

本题库覆盖 LHW 的内置传感阀、E/H/J 动作确认、动作原理、空气传感回路、型号表示、
规格、夹紧力、容许动作时间、外形与安装、标准及快换 A 型压板和专项注意事项。
LZH 压板附件和 BZL 低压速度控制阀仅在 Target 明确绑定相应附件或 LHW 适配关系时收录。
油压系列通用排气、速度控制、安全和保养要求按 DOCUMENT_COMMON 绑定。BZX、JZG、BZS
及联系信息不构成 LHW 当前选型的唯一技术对象，不纳入题目。

### 2.2 LHW 型号语法

LHW 型号结构为 `LHW<主体尺寸><设计编号>-C<夹紧时旋转方向><传感阀符号>[-<选配件>]`。
主体尺寸 `040/048/055/065/075` 对应本体外径 `φD=40/48/55/65/75 mm`；设计编号为 `1`；
`C` 为板式配管型，配有 G 螺纹堵头，可安装用户另购的 BZL-B；`R/L` 分别为夹紧时
顺时针/逆时针旋转；`E/H/J` 分别为夹紧与释放确认、仅夹紧确认、仅释放确认；无选配件
为标准锥形夹紧压板型，`A` 为快换压板 A 型。

### 2.3 来源清单

| Coverage ID | 物理页 | 局部范围 | Evidence type | 可测试对象 / 范围决定 | Priority / Disposition |
|---|---:|---|---|---|---|
| LHW-SI-001 | 1-4 | 油压旋转式夹紧器总览 | TEXT + TABLE | 跨系列宣传与选型导航 | LOW：排除宣传比较；LHW 边界由本文件 Scope 固定 |
| LHW-SI-002 | 5-6 | LHW 特点与剖面 | TEXT + DRAWING | 内置动作确认、超薄夹具、零漏气与简单气路；覆盖 LHW-Q-0003 | HIGH：已映射 |
| LHW-SI-003 | 7-8 | 动作原理 | STATE_DIAGRAM + TEXT | 夹紧/释放顺序、确认阀与 ON/OFF；覆盖 LHW-Q-0004、0005 | HIGH：已映射 |
| LHW-SI-004 | 9-10 | 空气传感器与流程 | TABLE + CHART + DRAWING | 推荐元件、气压、常态供气、排气口、配管长度；覆盖 LHW-Q-0006、0007 | HIGH：已映射 |
| LHW-SI-005 | 11-12 | 型号表示与规格 | MODEL + TABLE + FORMULA | 型号字段、规格与五种公式；覆盖 LHW-Q-0001、0002、0008 至 0013 | HIGH：已映射 |
| LHW-SI-006 | 13-14 | 夹紧力曲线 | CHART + TABLE + FORMULA | P/L/F 关系及不可使用范围；覆盖 LHW-Q-0012 至 0014 | HIGH：已映射 |
| LHW-SI-007 | 15-16 | 容许动作时间 | CHART + FORMULA + TEXT | 惯性矩、旋转/全动作时间与过快风险；覆盖 LHW-Q-0015、0016 | HIGH：已映射 |
| LHW-SI-008 | 17-24 | E/H/J/A 外形与安装 | MODEL + TABLE + DRAWING | 供气口、安装接口、0401 凸出和 A 型；覆盖 LHW-Q-0017、0019 | MEDIUM：代表性覆盖，不做尺寸替换式扩增 |
| LHW-SI-009 | 25-26 | 压板设计与 LZH 附件 | TABLE + DRAWING + TEXT | 标准/A 型压板、毛坯压板、紧固套件；覆盖 LHW-Q-0020 至 0022 | HIGH：已映射 |
| LHW-SI-010 | 27-30 | 油压旋转式夹紧器注意事项 | PROCEDURE + CAUTION + TABLE | 回路、惯性、安装、压板、速度调整；覆盖 LHW-Q-0017 至 0020 | HIGH：已映射 |
| LHW-SI-011 | 31-34 | 油压系列通用事项 | PROCEDURE + CAUTION + CIRCUIT_DIAGRAM | 排气、回油节流、安全与保养；覆盖 LHW-Q-0025 至 0028 | HIGH：技术内容已映射；商业保修条款排除 |
| LHW-SI-012 | 35-42 | BZL 低压速度控制阀 | MODEL + TABLE + CHART + DRAWING | BZL-B 规格、LHW 对应和安装限制；覆盖 LHW-Q-0023、0024 | MEDIUM：已映射 |
| LHW-SI-013 | 43-50 | BZX/JZG/BZS 附件 | MODEL + TABLE + DRAWING | 其他控制阀、堵头和顺序阀 | EXCLUDED：未与 LHW 当前题目形成唯一适配需求，不扩增附件目录题 |
| LHW-SI-014 | 51-52 | 公司与销售网点 | TEXT | 联系方式 | EXCLUDED：非耐久产品技术知识 |

## 3. Question Statistics

- Total: 28
- Direct LHW: 20
- Accessory / Related Product: 4
- Document Common: 4
- MODEL: 2
- FACT: 1
- SPEC_LOOKUP: 3
- TABLE: 5
- CALCULATION: 2
- CHART: 2
- PROCEDURE: 6
- CAUTION: 7

## 4. Questions

## LHW-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHW
- Model / Scope: LHW0481-CRE-A

### Question

按资料字段顺序解析 `LHW0481-CRE-A`，说明主体尺寸及 φD、设计编号、配管方式、
夹紧时旋转方向、传感阀功能和选配件。

### Standard Answer

`048` 对应 `φD=48 mm`；`1` 为设计编号；`C` 为配有 G 螺纹堵头的板式配管型，
BZL-B 速度控制阀由用户另购；`R` 为夹紧时顺时针；`E` 为夹紧和释放动作确认型；
`A` 为快换压板 A 型。

### Scoring Standard

- P1 [15]: `048` 与 `φD=48 mm`。
- P2 [10]: 设计编号 `1`。
- P3 [20]: `C`、板式配管和 G 螺纹堵头。
- P4 [10]: BZL-B 由用户另购。
- P5 [15]: `R` 为夹紧时顺时针。
- P6 [20]: `E` 为夹紧和释放动作确认型。
- P7 [10]: `A` 为快换压板 A 型。

### Accepted Variants

- `板式配管型` 可写为 `板式连接型`。

### Forbidden Errors

- 不得把 `R` 解释为释放方向，或把 `E` 解释为选配件。

### Tolerance

- 型号代码和尺寸必须精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 11
- Printed page: 609
- Section: 型号表示
- Local scope path: LHW > 型号表示 > 字段 1-6
- Evidence type: MODEL + DRAWING + TEXT
- Evidence: 型号图按顺序定义 048、1、C、R、E 和 A，并给出各字段含义。

## LHW-Q-0002

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHW
- Model / Scope: LHW 型号语法

### Question

判断以下型号是否合法并说明理由：`LHW0401-CLE`、`LHW0551-CRH`、
`LHW0651-CLJ-A`、`LHW0601-CRE`、`LHW0480-CRE`、`LHW0751-CCE`。

### Standard Answer

前三个合法；`LHW0601-CRE` 非法，因为无 060 主体尺寸；`LHW0480-CRE` 非法，
因为设计编号应为 1；`LHW0751-CCE` 非法，因为夹紧旋转方向只有 R/L，没有 C。
`E/H/J` 分别代表双向确认、夹紧确认和释放确认，A 位于末尾选配件字段。

### Scoring Standard

- P1 [30]: 正确判定三个合法型号。
- P2 [20]: 正确指出无 060 尺寸。
- P3 [20]: 正确指出设计编号必须为 1。
- P4 [20]: 正确指出旋转方向只有 R/L。
- P5 [10]: 正确说明 E/H/J 与末尾 A 的字段边界。

### Accepted Variants

- `不合法` 可写为 `不符合 PDF 型号语法`。

### Forbidden Errors

- 不得将 H/J 当作旋转方向，或把 A 放在传感阀字段。

### Tolerance

- N/A

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 11, 18, 20, 22, 24
- Printed page: 609, 616, 618, 620, 622
- Section: 型号表示 / 各传感阀与 A 型型号范例
- Local scope path: LHW > 型号表示 > 主体尺寸、设计编号、R/L、E/H/J、A
- Evidence type: MODEL + TABLE + DRAWING
- Evidence: 型号页定义合法字段集合；E/H/J/A 各外形页给出对应范例并保持相同字段顺序。

## LHW-Q-0003

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHW
- Model / Scope: 内置动作确认与夹具设计特点

### Question

LHW 的内置动作确认结构如何支持自动化、超薄夹具和低耗气空气传感器？

### Standard Answer

LHW 在动作端内置动作确认机构，并把传感阀机构内置于本体，适用于需要夹紧/释放确认
的自动化流水线；动作确认气口高度在不同尺寸组合中通用，可简化气路并使夹具基板最小
厚度达到 30 mm；传感阀关闭时漏气为零，因此可选择空气消耗量较小的空气传感元件。

### Scoring Standard

- P1 [20]: 动作端内置动作确认机构。
- P2 [20]: 传感阀机构内置于本体并适用于自动化确认。
- P3 [20]: 不同尺寸组合的确认气口高度通用、气路可简化。
- P4 [20]: 夹具基板最小厚度 30 mm。
- P5 [20]: 关闭时零漏气，可选低耗气传感器。

### Accepted Variants

- `零漏气` 可写为 `关闭状态无空气泄漏`。

### Forbidden Errors

- 不得声称无需空气传感器即可直接输出电信号。

### Tolerance

- 30 mm 必须精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 5-6
- Printed page: 603-604
- Section: 产品特点 / 剖面结构
- Local scope path: LHW > 特点 > 内置传感阀、超薄夹具、简单气路
- Evidence type: TEXT + DRAWING
- Evidence: 页面说明内置机构、关闭零漏气、低耗气传感器和 30 mm 夹具基板，并画出混合尺寸气路。

## LHW-Q-0004

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHW-E
- Model / Scope: 夹紧与释放动作顺序

### Question

说明 LHW-E 从释放到夹紧、再从夹紧到释放时活塞杆的动作顺序。

### Standard Answer

供给夹紧油压时，活塞杆先边下降边旋转，旋转结束后再垂直下降并夹紧工件；供给释放
油压时，活塞杆先在夹紧行程范围内垂直上升，垂直动作结束后再边旋转边上升到释放端。

### Scoring Standard

- P1 [25]: 夹紧时先下降并旋转。
- P2 [25]: 旋转结束后垂直下降夹紧。
- P3 [25]: 释放时先在夹紧行程内垂直上升。
- P4 [25]: 随后边旋转边上升至释放端。

### Accepted Variants

- 可使用 `旋转行程`、`夹紧行程` 表达相同次序。

### Forbidden Errors

- 不得颠倒旋转行程和直线夹紧行程。

### Tolerance

- N/A

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 605
- Section: 动作原理（剖面结构）
- Local scope path: LHW > 动作原理 > 夹紧 / 释放
- Evidence type: STATE_DIAGRAM + TEXT
- Evidence: 夹紧与释放剖面图逐步描述活塞杆的旋转和垂直动作顺序。

## LHW-Q-0005

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHW
- Model / Scope: E/H/J 传感阀功能与 E 型确认状态

### Question

分别说明 E、H、J 传感阀符号的功能，并给出 E 型在夹紧端和释放端的两个确认输出状态。

### Standard Answer

E 为夹紧和释放动作确认型，H 仅确认夹紧动作，J 仅确认释放动作。E 型夹紧端为
夹紧确认 ON、释放确认 OFF；释放端为夹紧确认 OFF、释放确认 ON。

### Scoring Standard

- P1 [20]: E 为夹紧与释放确认。
- P2 [15]: H 仅夹紧确认。
- P3 [15]: J 仅释放确认。
- P4 [25]: 夹紧端 ON/OFF 状态正确。
- P5 [25]: 释放端 OFF/ON 状态正确。

### Accepted Variants

- `ON/OFF` 可写为 `有信号/无信号`，但须明确对应输出。

### Forbidden Errors

- 不得声称 H 或 J 同时提供两个确认输出。

### Tolerance

- 状态必须精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 7-9
- Printed page: 605-607
- Section: 动作原理 / 适用型号与传感阀符号
- Local scope path: LHW > 动作原理 > 夹紧确认与释放确认
- Evidence type: TABLE + STATE_DIAGRAM + TEXT
- Evidence: 状态图给出夹紧端和释放端的 ON/OFF；适用型号表定义 E/H/J 功能。

## LHW-Q-0006

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHW
- Model / Scope: 空气传感器选型与供气条件

### Question

列出资料推荐的两种空气传感元件、推荐供气压力、供气状态和连接管长度基准。

### Standard Answer

推荐 SMC `ISA3-G` 空气传感元件或 CKD `GPS3-E` 间隙开关；供气压力为
0.1～0.2 MPa；使用时保持常态供气；连接气管尽可能短，长度基准为 5 m 以内。

### Scoring Standard

- P1 [20]: SMC ISA3-G。
- P2 [20]: CKD GPS3-E。
- P3 [25]: 0.1～0.2 MPa。
- P4 [15]: 常态供气。
- P5 [20]: 连接气管 5 m 以内且尽量短。

### Accepted Variants

- `间隙开关` 可写为 `气隙开关`。

### Forbidden Errors

- 不得把 0.1～0.2 MPa 写成液压供给压力。

### Tolerance

- 型号、压力范围和 5 m 上限必须精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 9-10
- Printed page: 607-608
- Section: 关于空气传感器 / 空气传感流程图注意事项
- Local scope path: LHW > 空气传感器 > 推荐表与配管注意事项
- Evidence type: TABLE + TEXT
- Evidence: 推荐表给出 ISA3-G/GPS3-E 与 0.1～0.2 MPa；流程图注记要求常态供气和气管 5 m 以内。

## LHW-Q-0007

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHW
- Model / Scope: 排气口防堵与误动作风险

### Question

LHW 排气口应如何处理？若存在冷却液或切削屑风险，资料推荐什么防护件及开启压力？

### Standard Answer

排气口必须向大气开放，并防止冷却液和切削屑侵入；排气口堵塞会导致空气传感器误动作。
可使用低开启压力单向阀，推荐 SMC AKH 系列，开启压力 0.005 MPa。

### Scoring Standard

- P1 [25]: 排气口向大气开放。
- P2 [20]: 防止冷却液和切削屑侵入。
- P3 [20]: 堵塞会导致传感器误动作。
- P4 [20]: 推荐 SMC AKH 系列单向阀。
- P5 [15]: 开启压力 0.005 MPa。

### Accepted Variants

- `大气开放` 可写为 `不得封闭排气口`。

### Forbidden Errors

- 不得把排气口接入有背压的封闭回路。

### Tolerance

- 0.005 MPa 必须精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 607
- Section: 设计、施工、使用方面的注意事项
- Local scope path: LHW > 空气传感器 > 排气口大气开放与防侵入
- Evidence type: CAUTION + DRAWING + TEXT
- Evidence: 页面明确给出大气开放、堵塞后果和 AKH 系列 0.005 MPa 推荐值。

## LHW-Q-0008

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHW
- Model / Scope: LHW0401/0481/0551/0651/0751 面积与缸径

### Question

按主体尺寸顺序列出五种 LHW 的夹紧器面积、夹紧器内径和活塞杆径。

### Standard Answer

LHW0401/0481/0551/0651/0751 的夹紧器面积依次为 5.00/6.95/10.3/13.4/20.3 cm²；
内径依次为 31/37/44/51/62 mm；活塞杆径依次为 18/22/25/30/35.5 mm。

### Scoring Standard

- P1 [35]: 五个面积全部正确。
- P2 [35]: 五个内径全部正确。
- P3 [30]: 五个活塞杆径全部正确。

### Accepted Variants

- `cm²` 可写为 `cm2`。

### Forbidden Errors

- 不得交换型号列或以面积推算夹紧力。

### Tolerance

- 表值精确，不接受容差。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 610
- Section: 规格
- Local scope path: LHW > 规格 > 面积、内径、活塞杆径
- Evidence type: TABLE
- Evidence: 规格表按五个型号列出面积、内径和活塞杆径。

## LHW-Q-0009

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHW
- Model / Scope: 容量、行程与精度

### Question

按五个主体尺寸列出夹紧/释放容量、全行程、90°旋转行程和夹紧行程，并说明角度精度。

### Standard Answer

夹紧容量依次为 7.3/10.8/19.0/26.7/48.7 cm³，释放容量为
10.9/16.7/28.1/40.9/72.5 cm³；全行程为 14.5/15.5/18.5/20/24 mm；
90°旋转行程为 6.5/7.5/8.5/10/12 mm；夹紧行程为 8/8/10/10/12 mm。
旋转角度精度为 90°±3°，夹紧位置重复精度为 ±0.5°。

### Scoring Standard

- P1 [20]: 五个夹紧容量。
- P2 [20]: 五个释放容量。
- P3 [20]: 五个全行程。
- P4 [15]: 五个旋转行程。
- P5 [15]: 五个夹紧行程。
- P6 [10]: 两项角度精度。

### Accepted Variants

- N/A

### Forbidden Errors

- 不得把旋转行程长度误作旋转角度。

### Tolerance

- 表值精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 610
- Section: 规格
- Local scope path: LHW > 规格 > 容量、行程、角度精度
- Evidence type: TABLE
- Evidence: 规格表按型号列出夹紧/释放容量、三种行程和角度精度。

## LHW-Q-0010

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHW
- Model / Scope: 压力、温度、流体与重量

### Question

说明 LHW 的最高使用压力、最低动作压力、耐压、推荐空气压力、温度、流体，以及标准型五种重量。

### Standard Answer

最高使用压力 7.0 MPa，最低无负载动作压力 1.5 MPa，耐压 10.5 MPa；推荐空气压力
0.1～0.2 MPa；使用温度 0～70℃；流体为相当于 ISO-VG-32 的一般作动油。标准型
LHW0401/0481/0551/0651/0751 重量为 0.9/1.4/2.0/2.9/4.2 kg。

### Scoring Standard

- P1 [15]: 最高压力 7.0 MPa。
- P2 [15]: 最低动作压力 1.5 MPa。
- P3 [15]: 耐压 10.5 MPa。
- P4 [15]: 空气压力 0.1～0.2 MPa。
- P5 [10]: 温度 0～70℃。
- P6 [10]: ISO-VG-32 一般作动油。
- P7 [20]: 五个标准型重量。

### Accepted Variants

- `作动油` 可写为 `液压油`。

### Forbidden Errors

- 不得把耐压当作允许连续使用压力。

### Tolerance

- 表值精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 610
- Section: 规格
- Local scope path: LHW > 规格 > 压力、温度、流体、重量
- Evidence type: TABLE
- Evidence: 规格表给出共同压力/温度/流体条件及标准型各尺寸重量。

## LHW-Q-0011

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHW
- Model / Scope: 五种主体尺寸的夹紧力计算公式

### Question

写出五种 LHW 的夹紧力公式，并定义 F、P、L 的单位。

### Standard Answer

LHW0401: `F=P(1-0.0016L)/(2.0920+0.0040L)`；LHW0481:
`F=P(1-0.0009L)/(1.4892+0.0018L)`；LHW0551:
`F=P(1-0.0011L)/(1.0039+0.0011L)`；LHW0651:
`F=P(1-0.0009L)/(0.7822+0.0010L)`；LHW0751:
`F=P(1-0.0007L)/(0.5175+0.0006L)`。F 为夹紧力 kN，P 为供给油压 MPa，
L 为活塞中心至夹紧点的距离/压板长度 mm。

### Scoring Standard

- P1 [14]: LHW0401 公式。
- P2 [14]: LHW0481 公式。
- P3 [14]: LHW0551 公式。
- P4 [14]: LHW0651 公式。
- P5 [14]: LHW0751 公式。
- P6 [30]: F/P/L 的物理意义与单位。

### Accepted Variants

- 等价代数形式可接受。

### Forbidden Errors

- 不得删除任一分子中的 `1-aL` 项或混用型号系数。

### Tolerance

- 系数必须精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 12-14
- Printed page: 610-612
- Section: 规格 / 夹紧力曲线图
- Local scope path: LHW > 夹紧力 > 型号公式与变量定义
- Evidence type: TABLE + FORMULA
- Evidence: 规格表及曲线页逐型号印出公式，并定义 F、P、L 与单位。

## LHW-Q-0012

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHW
- Model / Scope: LHW0481，P=5.0 MPa，L=90 mm

### Question

用 PDF 公式计算夹紧力，最终按 `ROUND_HALF_UP` 保留 1 位小数。

### Standard Answer

`F=5.0×(1-0.0009×90)/(1.4892+0.0018×90)=2.7828246124... kN`，
按 `ROUND_HALF_UP` 保留 1 位小数为 `2.8 kN`。

### Scoring Standard

- P1 [25]: 使用 LHW0481 正确公式。
- P2 [20]: 正确代入 P=5.0 MPa、L=90 mm。
- P3 [25]: 未舍入值约 2.7828246124 kN。
- P4 [20]: 最终结果 2.8 kN。
- P5 [10]: 单位和 ROUND_HALF_UP 规则明确。

### Accepted Variants

- 中间值保留更多有效位可接受。

### Forbidden Errors

- 不得用夹紧器面积直接计算，或在中间步骤提前舍入。

### Tolerance

- 最终结果按 `ROUND_HALF_UP` 精确为 2.8 kN。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 12-13
- Printed page: 610-611
- Section: 规格 / LHW0481 夹紧力曲线
- Local scope path: LHW > 夹紧力 > LHW0481 公式
- Evidence type: FORMULA
- Evidence: 公式明确给出 LHW0481 的 P/L/F 关系和变量单位。

## LHW-Q-0013

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHW
- Model / Scope: LHW0651，L=120 mm，目标 F=5.0 kN

### Question

反算所需供给油压，按 `ROUND_HALF_UP` 保留 1 位小数，并用舍入后的压力回代验证夹紧力。

### Standard Answer

`P=5.0×(0.7822+0.0010×120)/(1-0.0009×120)=5.0571748879... MPa`，
保留 1 位小数为 `5.1 MPa`。回代：
`F=5.1×(1-0.0009×120)/(0.7822+0.0010×120)=5.0423409444... kN`，
保留 1 位小数为 `5.0 kN`；5.1 MPa 未超过该工况的允许压力范围。

### Scoring Standard

- P1 [25]: 正确变形并代入 LHW0651 公式。
- P2 [20]: 未舍入压力约 5.0571748879 MPa。
- P3 [15]: 最终压力 5.1 MPa。
- P4 [25]: 用 5.1 MPa 正确回代得约 5.0423409444 kN。
- P5 [10]: 回代最终为 5.0 kN。
- P6 [5]: 说明压力未越界。

### Accepted Variants

- 中间值保留更多有效位可接受。

### Forbidden Errors

- 不得只给反算压力而省略回代，或忽略分子修正项。

### Tolerance

- 压力与回代夹紧力均按 `ROUND_HALF_UP` 保留 1 位小数。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 12, 14
- Printed page: 610, 612
- Section: 规格 / LHW0651 夹紧力曲线
- Local scope path: LHW > 夹紧力 > LHW0651 公式与可使用范围
- Evidence type: FORMULA + CHART
- Evidence: LHW0651 公式支持反算；曲线页给出压力与压板长度的可使用边界。

## LHW-Q-0014

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHW
- Model / Scope: LHW0481，P=5.0 MPa，L=50 mm 的夹紧力曲线视觉读数

### Question

从夹紧力曲线视觉读取该工况的夹紧力，并说明允许读图范围。

### Standard Answer

曲线页示例读数约为 `3.1 kN`。按曲线线宽、刻度和视觉分辨率，接受范围为
`3.0～3.2 kN`。公式只能作为合理性复核，不能替代本题的视觉读图。

### Scoring Standard

- P1 [35]: 明确使用 LHW0481 曲线而非离散表替代。
- P2 [35]: 视觉 Gold 约 3.1 kN。
- P3 [20]: 接受范围 3.0～3.2 kN。
- P4 [10]: 说明公式仅作复核。

### Accepted Variants

- `约 3.1 kN` 或落在给定范围内均可。

### Forbidden Errors

- 不得把公式计算值声明为视觉 Gold，或使用其他主体尺寸曲线。

### Tolerance

- CHART tolerance: 3.0～3.2 kN。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 611
- Section: 夹紧力曲线图
- Local scope path: LHW > LHW0481 曲线 > P=5.0 MPa、L=50 mm 示例
- Evidence type: CHART + TEXT
- Evidence: 曲线页给出坐标、系列和该工况视觉示例“约 3.1 kN”。

## LHW-Q-0015

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHW
- Model / Scope: LHW0481，压板惯性力矩 0.0068 kg·m²

### Question

按容许动作时间图读取该压板的夹紧/释放 90°旋转时间及夹紧/释放全动作时间下限。

### Standard Answer

夹紧 90°旋转时间约 `0.44 s` 以上，释放 90°旋转时间约 `0.22 s` 以上；
夹紧全动作时间约 `0.90 s` 以上，释放全动作时间约 `0.45 s` 以上。

### Scoring Standard

- P1 [25]: 夹紧 90°约 0.44 s 以上。
- P2 [25]: 释放 90°约 0.22 s 以上。
- P3 [25]: 夹紧全动作约 0.90 s 以上。
- P4 [25]: 释放全动作约 0.45 s 以上。

### Accepted Variants

- 必须保留“以上/不短于”的下限含义。

### Forbidden Errors

- 不得将四个值当作目标最大时间，或把全动作时间与旋转时间互换。

### Tolerance

- CHART tolerance: 0.44 s 为 0.42～0.46；0.22 s 为 0.20～0.24；0.90 s 为 0.86～0.94；0.45 s 为 0.42～0.48。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 15-16
- Printed page: 613-614
- Section: 容许动作时间图表 / 图表解读方法
- Local scope path: LHW > LHW0481 容许动作时间 > I=0.0068 kg·m²
- Evidence type: CHART + TEXT
- Evidence: 图表按惯性力矩给出旋转与全动作曲线，下一页用同一工况标出四个视觉读数。

## LHW-Q-0016

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHW
- Model / Scope: 最短旋转时间、速度风险与控制方式

### Question

即使压板惯性力矩很小，90°旋转时间下限是多少？动作过快有何后果，推荐如何控制？

### Standard Answer

夹紧 90°旋转时间不得短于 0.2 s，释放不得短于 0.1 s。动作过快会使停止精度恶化，
并造成内部零件磨损或损伤。应根据惯性力矩和容许动作时间图调整，并采用回油节流回路
使夹紧器等速动作。

### Scoring Standard

- P1 [20]: 夹紧下限 0.2 s。
- P2 [20]: 释放下限 0.1 s。
- P3 [20]: 停止精度恶化。
- P4 [20]: 内部零件磨损/损伤。
- P5 [20]: 按图并用回油节流调整等速动作。

### Accepted Variants

- `回油节流` 可写为 `meter-out`。

### Forbidden Errors

- 不得把 0.2/0.1 s 当作必须追求的最快设定，或推荐进油节流作为 LHW 常规控制。

### Tolerance

- 时间下限精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 15
- Printed page: 613
- Section: 容许动作时间图表注意事项
- Local scope path: LHW > 容许动作时间 > 最短时间与回油节流
- Evidence type: CHART + CAUTION + TEXT
- Evidence: 注记给出 0.2/0.1 s 下限、过快后果和回油节流推荐。

## LHW-Q-0017

**Type: PROCEDURE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHW
- Model / Scope: LHW0551-CRE 标准型安装

### Question

安装 LHW0551-CRE 时，说明本体安装螺栓、紧固力矩、供油/供气口和随附件边界。

### Standard Answer

本体须使用全部安装孔和强度等级 12.9 的 M6 螺栓，按 14 N·m 紧固；夹紧与释放
供油口为 G1/8，E 型需分别设置夹紧确认和释放确认供气口，供气口直径范围 φ4～φ6，
排气口保持开放。本产品不附安装螺栓和速度控制阀，附带板式配管用 G 螺纹堵头。

### Scoring Standard

- P1 [20]: 全部安装孔、12.9 级 M6。
- P2 [15]: 14 N·m。
- P3 [15]: 夹紧/释放供油口 G1/8。
- P4 [20]: E 型两个确认供气口、φ4～φ6。
- P5 [10]: 排气口开放。
- P6 [20]: 安装螺栓和速度阀不附带、G 堵头附带。

### Accepted Variants

- N/A

### Forbidden Errors

- 不得声称安装螺栓或 BZL 随产品附带。

### Tolerance

- 螺栓、力矩和接口尺寸精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 17-18, 27
- Printed page: 615-616, 745
- Section: LHW-E 外形尺寸 / 安装施工注意事项
- Local scope path: LHW > LHW0551-CRE > 安装接口与本体安装表
- Evidence type: DRAWING + TABLE + PROCEDURE
- Evidence: 外形页定义供油/供气口和未附带件；安装表给出 LHW0551 的 M6、14 N·m。

## LHW-Q-0018

**Type: PROCEDURE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHW
- Model / Scope: LHW0551 标准锥形压板安装与拆卸

### Question

说明标准锥形压板安装前的清洁要求、螺母规格/力矩，以及避免活塞杆承受旋转力矩的作业要点。

### Standard Answer

压板、锥套和活塞杆连接面必须脱脂、清洗并去除油污异物。LHW0551 使用 M22×1.5
螺母，推荐紧固力矩 84～100 N·m。安装时先在夹具上定位并临时紧固，再卸下夹紧器，
用虎钳等固定压板后正式紧固；若在夹具上正式紧固，应以扳手固定活塞杆顶端六角或压板，
并在旋转角度中间位置作业。拆卸时同样固定并转到中间位置，螺母松 2～3 圈后用拔出器拆下。

### Scoring Standard

- P1 [20]: 三个连接部位脱脂清洗。
- P2 [15]: M22×1.5。
- P3 [15]: 84～100 N·m。
- P4 [20]: 定位临紧后固定压板正式紧固。
- P5 [15]: 固定活塞杆/压板且在旋转中间位置作业。
- P6 [15]: 拆卸松 2～3 圈并用拔出器，不向活塞杆施加旋转力矩。

### Accepted Variants

- `拔出器` 可写为 `拉拔器`。

### Forbidden Errors

- 不得直接让活塞杆承受正式紧固或拆卸的旋转力矩。

### Tolerance

- 规格和力矩范围精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 28-29
- Printed page: 746-747
- Section: 旋转压板的安装、拆卸
- Local scope path: 油压旋转式夹紧器 > 标准锥形压板型 > LHW0551
- Evidence type: PROCEDURE + TABLE + CAUTION
- Evidence: 注意事项页给出清洁、力矩表及避免活塞杆承受旋转力矩的安装/拆卸流程。

## LHW-Q-0019

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHW-A
- Model / Scope: 快换压板 A 型偏心夹紧点与相位销

### Question

LHW-A 使用偏心压板时夹紧点应位于何处？挡销兼相位调整销在安装和拆卸时分别有什么作用？

### Standard Answer

夹紧点必须位于以压板紧固部为基准的 90° 范围内。挡销兼相位调整销由客户自备，
安装时用于压板相位调整，拆卸时兼作挡块；若不使用该销，拆卸时必须另备挡块。

### Scoring Standard

- P1 [30]: 夹紧点在压板紧固部基准的 90° 范围内。
- P2 [25]: 相位销由客户自备。
- P3 [20]: 安装时调整相位。
- P4 [15]: 拆卸时兼作挡块。
- P5 [10]: 不使用时另备挡块。

### Accepted Variants

- `90°范围` 可写为 `图示扇形允许范围`，但须保留紧固部基准。

### Forbidden Errors

- 不得将 90° 解释为压板旋转行程的精度范围。

### Tolerance

- 90° 边界精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 25, 27, 29
- Printed page: 623, 745, 747
- Section: 快换压板 A 型设计 / 偏心压板 / 安装拆卸
- Local scope path: LHW-A > 挡销兼相位调整销与夹紧点范围
- Evidence type: DRAWING + CAUTION + TEXT
- Evidence: A 型设计页定义销的双重作用，注意事项图限定相对紧固部的 90° 夹紧点范围。

## LHW-Q-0020

**Type: PROCEDURE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHW-A
- Model / Scope: LHW0551-A 快换压板装拆

### Question

说明 LHW0551-A 的紧固套件螺栓规格/力矩、安装顺序和拆卸方法。

### Standard Answer

对应紧固套件使用 M6 螺栓，紧固力矩 8.0 N·m。安装顺序为活塞杆、旋转压板、
楔形块 1、楔形块 2，随后把压板推靠楔形块侧并按规定力矩锁紧螺栓。拆卸时松开
紧固螺栓，楔形机构解除后即可拆下压板；相位销或另备挡块须限制拆卸动作。

### Scoring Standard

- P1 [20]: M6。
- P2 [20]: 8.0 N·m。
- P3 [25]: 四个部件的安装顺序。
- P4 [20]: 推靠楔形块后按力矩锁紧。
- P5 [15]: 松螺栓解除楔形机构并由销/挡块限位拆卸。

### Accepted Variants

- 楔形块编号须保持 1、2 的顺序。

### Forbidden Errors

- 不得套用标准锥形压板的 M22×1.5、84～100 N·m。

### Tolerance

- 螺栓和力矩精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 26, 28-29
- Printed page: 624, 746-747
- Section: LZH-W 紧固套件 / 快换压板 A 型安装拆卸
- Local scope path: LHW0551-A > LZH0551-W > 紧固件与装拆流程
- Evidence type: TABLE + PROCEDURE + DRAWING
- Evidence: 附件表给出 M6、8.0 N·m；注意事项页画出楔形块安装和解除流程。

## LHW-Q-0021

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LZH 附件
- Model / Scope: LHW0401/0481/0551/0651/0751 对应压板附件

### Question

按五个 LHW 尺寸列出标准毛坯压板、A 型毛坯压板和 A 型紧固套件的型号，并说明毛坯材质/表面处理。

### Standard Answer

标准毛坯压板依次为 `LZH0400-T/LZH0480-T/LZH0550-T/LZH0650-T/LZH0750-T`；
A 型毛坯压板依次为 `LZH0400-A/LZH0480-A/LZH0550-A/LZH0650-A/LZH0750-A`；
紧固套件依次为 `LZH0401-W/LZH0481-W/LZH0551-W/LZH0651-W/LZH0751-W`。
两类毛坯压板材质为 S50CH，表面发黑处理。

### Scoring Standard

- P1 [30]: 五个标准 T 型号。
- P2 [30]: 五个 A 型毛坯型号。
- P3 [25]: 五个 W 紧固套件型号。
- P4 [10]: S50CH。
- P5 [5]: 发黑处理。

### Accepted Variants

- 型号可按尺寸逐行列出。

### Forbidden Errors

- 不得混淆设计编号 0 的毛坯压板与设计编号 1 的紧固套件。

### Tolerance

- 型号精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 26
- Printed page: 624
- Section: 附件：毛坯压板 / 快换压板 A 型附件
- Local scope path: LHW > LZH-T / LZH-A / LZH-W 对应表
- Evidence type: TABLE + MODEL + TEXT
- Evidence: 三张附件表按 LHW 尺寸给出对应型号；毛坯说明给出 S50CH 与发黑处理。

## LHW-Q-0022

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHW 压板
- Model / Scope: 标准与 A 型压板设计加工

### Question

压板长度和加工尺寸应如何确定？不按表加工会造成什么后果，A 型哪些附件不是随附品？

### Standard Answer

压板长度须依据能力曲线确定，标准型和 A 型均须严格按对应尺寸表加工；否则会造成
夹紧力达不到规格，或发生变形、卡滞、动作不正常。标准型定位销不附带；A 型紧固套件
LZH-W 为另售品，挡销兼相位调整销由客户自备。

### Scoring Standard

- P1 [20]: 按能力曲线确定长度。
- P2 [20]: 严格按对应尺寸表加工。
- P3 [25]: 夹紧力不足、变形/卡滞/动作异常后果。
- P4 [15]: 标准型定位销不附带。
- P5 [20]: LZH-W 另售、相位销客户自备。

### Accepted Variants

- `另售` 可写为 `需另行购买`。

### Forbidden Errors

- 不得声称任意压板尺寸均可，或 LZH-W/相位销随夹紧器附带。

### Tolerance

- N/A

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 25-26
- Printed page: 623-624
- Section: 压板设计尺寸 / 附件注意事项
- Local scope path: LHW > 标准/A 型压板 > 设计加工与随附边界
- Evidence type: CAUTION + TABLE + TEXT
- Evidence: 两类设计表给出长度依据、加工后果及定位销、LZH-W、相位销的供货边界。

## LHW-Q-0023

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZL-B
- Model / Scope: LHW 尺寸适配与低压回油节流规格

### Question

给出五种 LHW 对应的 BZL-B 型号，并列出两种相关 BZL-B 的 G 螺纹、开启压力、最大流道面积和推荐紧固力矩。

### Standard Answer

LHW0401/0481/0551 对应 `BZL0101-B`，LHW0651/0751 对应 `BZL0201-B`。
BZL0101-B 为 G1/8A、开启压力 0.12 MPa、最大流道面积 2.6 mm²、推荐力矩 10 N·m；
BZL0201-B 为 G1/4A、开启压力 0.12 MPa、最大流道面积 5.0 mm²、推荐力矩 25 N·m。
两者最高使用压力 7 MPa、耐压 10.5 MPa，控制方式为回油节流。

### Scoring Standard

- P1 [25]: 五种 LHW 与两个 BZL-B 的映射。
- P2 [20]: 两个 G 螺纹尺寸。
- P3 [15]: 开启压力均为 0.12 MPa。
- P4 [15]: 2.6/5.0 mm²。
- P5 [15]: 10/25 N·m。
- P6 [10]: 7/10.5 MPa 与回油节流。

### Accepted Variants

- `meter-out` 可写为 `回油节流`。

### Forbidden Errors

- 不得为 0401～0551 选 BZL0201-B，或为 0651/0751 选 BZL0101-B。

### Tolerance

- 型号和表值精确。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 39-40
- Printed page: 1259-1260
- Section: BZL 型号表示、规格与对应机器型号
- Local scope path: BZL-B > LHW 对应行与 B 型规格列
- Evidence type: TABLE + MODEL
- Evidence: 规格表定义 B 型回油节流参数；对应机器表按 LHW 尺寸分配 0101-B/0201-B。

## LHW-Q-0024

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZL-B
- Model / Scope: LHW 用 BZL 的安装与再使用限制

### Question

BZL 安装时为何必须使用推荐力矩？已经使用过的 BZL 能否转装到另一只夹紧器？

### Standard Answer

必须按推荐力矩安装，因为 BZL 端面为金属密封结构，力矩不足会使流量无法调整。
已经使用过的 BZL 不应再用于其他夹紧器；不同夹紧器的 G 螺纹底面深度差异可能造成
金属密封不严，进而无法调整流量。

### Scoring Standard

- P1 [25]: 必须使用推荐紧固力矩。
- P2 [25]: 金属端面密封，力矩不足无法调流量。
- P3 [20]: 使用过的 BZL 不应转装其他夹紧器。
- P4 [15]: 原因是 G 螺纹底面深度差异。
- P5 [15]: 后果是密封不严和流量无法调整。

### Accepted Variants

- `不应再用于` 可写为 `资料不允许转用于`。

### Forbidden Errors

- 不得强化为 BZL 在原夹紧器上维护后绝对不可继续使用。

### Tolerance

- N/A

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 1259
- Section: BZL 规格注意事项
- Local scope path: BZL > 金属密封安装力矩与跨夹紧器再使用限制
- Evidence type: CAUTION + TEXT
- Evidence: 注意事项明确说明力矩不足后果，以及 G 螺纹底面深度差造成的转装风险。

## LHW-Q-0025

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: 油压夹紧器与支撑器
- Model / Scope: LHW_R00_2023KW_C1N.pdf :: 油压系列通用安装施工 / 排气

### Question

油压回路进入大量空气后，按资料顺序说明排气步骤。

### Standard Answer

先把供油压力调到 2 MPa 以下；将最靠近夹紧器或支撑器的配管接头螺母松开约一圈；
左右摇动配管，使连接部松动并排出混有空气的液压油；空气排净后重新紧固接头螺母。
在回路最高端和最末端附近排气效果更佳，板式配管可在最高端附近设置排气阀。

### Scoring Standard

- P1 [20]: 压力调至 2 MPa 以下。
- P2 [20]: 松开最近接头约一圈。
- P3 [20]: 左右摇动配管并排出含气液压油。
- P4 [20]: 排净后重新紧固。
- P5 [20]: 最高端/最末端及板式排气阀建议。

### Accepted Variants

- `约一圈` 可写为 `一圈左右`。

### Forbidden Errors

- 不得在高于 2 MPa 的压力下松开接头，或完全拆除接头。

### Tolerance

- 2 MPa 为上限条件，步骤顺序必须保持。

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 31
- Printed page: 1725
- Section: 安装施工方面的注意事项（油压系列通用）
- Local scope path: 油压系列通用 > 排净油压回路内的空气 > 步骤 1-5
- Evidence type: PROCEDURE + TEXT
- Evidence: 通用页逐项给出降压、松接头、摇动排气、紧固和优选位置。

## LHW-Q-0026

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: 油压复动夹紧器
- Model / Scope: LHW_R00_2023KW_C1N.pdf :: 复动夹紧器速度控制回路

### Question

LHW 的夹紧侧和释放侧应采用哪种节流方式？说明为何不得套用资料列出的进油节流例外，以及回油节流时的供油量风险。

### Standard Answer

LHW 属于复动夹紧器，夹紧侧和释放侧均应采用回油节流。进油节流例外仅列给
LKE/LSE/TLA/TLB/TMA/TLV/TMV/TTA，LHW 不在其中。回油节流受供油量影响时，
动作中可能发生回路内压升高，应预先用流量调整阀减少供油量；尤其有顺序阀或确认压力
开关时，超过设定压力会使系统无法动作。

### Scoring Standard

- P1 [25]: LHW 两侧均回油节流。
- P2 [25]: 准确说明例外系列且 LHW 不在其中。
- P3 [20]: 供油量过大可能导致动作中内压升高。
- P4 [15]: 用流量调整阀预先减少供油量。
- P5 [15]: 顺序阀/压力开关系统可能超过设定值而无法动作。

### Accepted Variants

- `回油节流` 可写为 `meter-out`。

### Forbidden Errors

- 不得把 TLA/TLV 等进油节流例外迁移到 LHW。

### Tolerance

- N/A

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 32
- Printed page: 1726
- Section: 夹紧器的速度控制回路及注意事项
- Local scope path: 油压系列通用 > 复动夹紧器 > 回油节流与例外边界
- Evidence type: CIRCUIT_DIAGRAM + CAUTION + TEXT
- Evidence: 页面规定复动两侧回油节流，单列进油节流例外系列，并说明供油量导致的内压风险。

## LHW-Q-0027

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: 液压/气动装置
- Model / Scope: LHW_R00_2023KW_C1N.pdf :: 操作方面的安全注意事项

### Question

检查或拆卸装置前必须落实哪些安全条件？对动作中的夹紧器和产品改造有哪些禁令？

### Standard Answer

应由具备知识和经验的人员操作维护。检查或拆卸前要防止被驱动物坠落和误动作，切断
压力源与电源，确认油压/气压回路压力为零，并等待刚停止的设备完全冷却；重新启动前
检查连接部位。严禁接触动作中的夹紧器，严禁擅自解体或改造产品。

### Scoring Standard

- P1 [15]: 合格人员操作维护。
- P2 [20]: 防坠落和防误动作措施。
- P3 [20]: 切断压力源/电源并确认压力为零。
- P4 [15]: 等待冷却、重启前检查连接。
- P5 [15]: 禁止接触动作中的夹紧器。
- P6 [15]: 禁止擅自解体或改造。

### Accepted Variants

- N/A

### Forbidden Errors

- 不得只关闭控制信号而保留压力，或在运动/高温状态拆卸。

### Tolerance

- N/A

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 1727
- Section: 操作方面的注意事项
- Local scope path: 油压系列通用 > 操作安全 > 检查、拆卸、接触与改造
- Evidence type: CAUTION + TEXT
- Evidence: 通用页规定人员资格、防坠落、断源归零、冷却、禁止接触和禁止改造。

## LHW-Q-0028

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: 油压夹紧器
- Model / Scope: LHW_R00_2023KW_C1N.pdf :: 保养、检查

### Question

列出重新启用或日常维护 LHW 时应执行的主要保养检查项目。

### Standard Answer

拆卸前执行防坠落、防误动作、断开压力源/电源和回路归零，并在重新启动前检查连接；
定期清扫活塞杆/柱塞周围；长期自动对接供油时定期排气；检查配管、安装螺栓、螺母、
固定环和夹紧器是否松动并加固；检查液压油老化、异音以及动作是否正常顺畅，长期闲置
后尤其要确认动作；产品应存放在阴凉干燥处，解体大修委托 KOSMEK。

### Scoring Standard

- P1 [20]: 拆卸安全与重启前连接检查。
- P2 [15]: 清扫活塞杆/柱塞周围。
- P3 [15]: 自动对接长期使用时定期排气。
- P4 [15]: 检查并加固配管和各紧固件。
- P5 [20]: 检查油品老化、异音和动作，闲置后特别确认。
- P6 [15]: 阴凉干燥存放、大修委托厂家。

### Accepted Variants

- 可按检查清单形式回答。

### Forbidden Errors

- 不得在压力未归零时拆卸，或自行进行解体大修。

### Tolerance

- N/A

### Source

- PDF: LHW_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 1727
- Section: 保养、检查
- Local scope path: 油压系列通用 > 保养检查 > 项目 1-9
- Evidence type: PROCEDURE + CAUTION + TEXT
- Evidence: 通用页逐项规定拆卸安全、清扫、排气、紧固、油品/动作检查、保管和大修边界。
