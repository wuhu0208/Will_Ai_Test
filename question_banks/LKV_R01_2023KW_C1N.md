---
schema_version: will-ai-question-bank/v1
source_pdf: LKV_R01_2023KW_C1N.pdf
source_sha256: d6f28ce00837cefa6af489b9f08a92eaf4e4edb2a9bd47a6ad1e2e72fcd061b5
source_pages: 52
question_bank_version: V1
product_scope: LKV
---

# LKV_R01_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LKV_R01_2023KW_C1N.pdf`
- SHA-256: `d6f28ce00837cefa6af489b9f08a92eaf4e4edb2a9bd47a6ad1e2e72fcd061b5`
- 物理页数: 52
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器及文档内直接适用附件
- LKV 主要产品印刷页: 807-826
- 产品总览与专用注意事项印刷页: 749-752、943-944
- 文档内通用资料与附件印刷页: 1257-1272、1713-1716、1725-1730
- 来源证据原则: PDF 页面为 Source Truth；哈希绑定文本缓存仅用于定位，型号排版、图表、状态图和尺寸关系存在歧义时以页面视觉证据为准。

## 2. Scope

### 2.1 产品与文档范围

本题库的主要产品范围是 LKV 单回路双向检知型杠杆式夹紧器，覆盖夹紧与释放动作、
单气路双向检知、型号表示、规格、夹紧力、容许偏心量、安装和压板设计，以及 LKV
专用设计、施工和使用注意事项。

PDF 同时收录油压杠杆式夹紧器系列总览、液压通用注意事项、BZL/BZX/JZG/BZS 控制阀、
LZV 传感单元等资料。只有在 Target 明确绑定相应附件或页范围时，才可使用这些资料；
不得把 LKA、LKC、LKK、LKW、LJ/LM、LJV、TMV-2、TMA-1 等其他系列的规格迁移到 LKV。

公司地址、销售网点和销售网络图属于非技术联系信息，不进入产品能力题目。

### 2.2 LKV 型号语法

LKV 型号表示的规范结构为：

`LKV<主体尺寸>0-C<压板方向>E[-<选配件>]`

其中 `E` 是型号表示图中位于压板方向之后的固定字母；选择无符号标准型时省略末尾
选配件及其前置连字符。字段顺序不得改变。

| 字段 | 资料列出的值 | 含义与约束 |
|---|---|---|
| 主体尺寸 | `040`、`048`、`055`、`065`、`075` | 分别表示本体夹紧器部分外径 phi 40、48、55、65、75 mm。 |
| 设计编号 | `0` | 表示产品版本信息。 |
| 配管方式 | `C` | 板式配管型，配有 G 螺纹堵头；速度控制阀由用户另行购买，推荐 BZL-B。 |
| 压板方向 | `L`、`C`、`R` | 配管口位置朝向观察者时，分别表示左、中央、右夹紧方向。 |
| 固定字母 | `E` | 位于压板方向之后，必须按型号表示保留。 |
| 选配件 | `A`、`H`、`K`、无符号 | `A` 为快换压板 A 型；`H` 为高强度链接板型并增大容许偏心量；`K` 为带凸缘销、C 形定位环型；无符号为标准型。 |

资料要求选配件组合详情另行确认，因此字段值和顺序成立不代表任意组合均已被资料批准。
完整型号判断应优先采用资料明确列出的型号范例或对应表。

### 2.3 来源覆盖索引

下表按相邻物理页形成的印刷跨页记录来源对象、优先级和题库范围处置。

| Coverage ID | 物理页 / 印刷页 | 局部范围 | 证据类型 | 优先级 | 可测试对象与范围处置 |
|---|---|---|---|---|---|
| LKV-SI-001 | 1-2 / 749-750 | 油压杠杆式夹紧器总览 | TEXT + DRAWING | MEDIUM | 纳入 LKV 所属产品类别与复动动作边界；其他系列仅作范围排除。 |
| LKV-SI-002 | 3-4 / 751-752 | 杠杆式夹紧器产品类型 | TABLE + TEXT | MEDIUM | 纳入 LKV 单回路双向检知、低压复动及附件关系；其他型号规格不迁移。 |
| LKV-SI-003 | 5-6 / 807-808 | LKV 特点、目录与使用范例 | TEXT + DRAWING | HIGH | `LKV-Q-0002` 至 `LKV-Q-0004` 覆盖单气路双向检知、防冷却液密封、薄型夹具和直装速度控制阀边界。 |
| LKV-SI-004 | 7-8 / 809-810 | LKV 液压与空气动作原理 | STATE_DIAGRAM + TEXT | HIGH | 纳入夹紧、动作途中、释放状态及夹紧/释放确认输出关系。 |
| LKV-SI-005 | 9-10 / 811-812 | 空气传感流程与使用注意 | CHART + STATE_DIAGRAM + CAUTION | HIGH | `LKV-Q-0005`、`LKV-Q-0013` 覆盖空气传感器条件及排气孔防侵入要求；流程图状态映射保留为覆盖审计对象。 |
| LKV-SI-006 | 11-12 / 813-814 | 型号表示与规格 | MODEL + TABLE + DRAWING | HIGH | `LKV-Q-0001`、`LKV-Q-0006` 至 `LKV-Q-0008` 覆盖型号语法、通用压力与油液边界、代表型号规格及跨列选型。 |
| LKV-SI-007 | 13-14 / 815-816 | 夹紧力表、曲线与公式 | TABLE + CHART + FORMULA | HIGH | `LKV-Q-0009`、`LKV-Q-0010` 分别覆盖确定性公式计算和非离散表格点的真实曲线视觉读取。 |
| LKV-SI-008 | 15-16 / 817-818 | 标准/A/K 型容许偏心量 | TABLE + CHART + CAUTION | HIGH | 纳入代表工况视觉读取和超范围导致变形、卡住、漏油的后果。 |
| LKV-SI-009 | 17-18 / 819-820 | H 型容许偏心量 | TABLE + CHART + CAUTION | MEDIUM | 与标准/A/K 同类，保留一个能体现 H 型边界差异的代表对象。 |
| LKV-SI-010 | 19-20 / 821-822 | 标准/H/K 型外形与安装 | DRAWING + TABLE + CAUTION | HIGH | 纳入安装口、排气孔、单向阀、安装螺栓和选配结构边界；尺寸数值仅取代表项。 |
| LKV-SI-011 | 21-22 / 823-824 | A 型快换压板外形与安装 | DRAWING + TABLE + CAUTION | MEDIUM | 纳入 A 型压板方向、安装和拆卸限制；重复尺寸不逐型号设题。 |
| LKV-SI-012 | 23-24 / 825-826 | 压板设计与 LZK 毛坯压板 | DRAWING + TABLE + FORMULA + CAUTION | HIGH | 纳入压板长度、强度、加工尺寸和超范围故障；附件采购尺寸不扩展。 |
| LKV-SI-013 | 25-26 / 943-944 | 油压杠杆式夹紧器专用注意事项 | TEXT + PROCEDURE + CAUTION | HIGH | `LKV-Q-0011`、`LKV-Q-0014`、`LKV-Q-0015` 覆盖速度调整、双侧同时供压禁令和载荷边界；其他型号专属条款排除。 |
| LKV-SI-014 | 27-28 / 1725-1726 | 液压安装、油液与速度回路 | TEXT + PROCEDURE + STATE_DIAGRAM | HIGH | `LKV-Q-0012` 覆盖通用液压回路排气；复动速度回路保留为覆盖审计对象且不得迁移例外型号规则。 |
| LKV-SI-015 | 29-30 / 1727-1728 | 操作、维护与质量保证 | TEXT + PROCEDURE + CAUTION | MEDIUM | 纳入通用安全操作和维护检查；商业保证条款不作为产品能力题。 |
| LKV-SI-016 | 31-32 / 1729-1730 | 表面粗糙度与 O 形圈标示 | TABLE + MODEL | LOW | 仅作跨产品标示参考，不改变 LKV 核心答案，排除。 |
| LKV-SI-017 | 33-34 / 1257-1258 | 控制阀总览 | TABLE + TEXT | MEDIUM | 纳入 LKV 可直接安装控制阀的功能边界；独立附件规格仅在明确绑定时使用。 |
| LKV-SI-018 | 35-36 / 1259-1260 | BZL 低压速度控制阀 | MODEL + TABLE + CAUTION | HIGH | 纳入 LKV 推荐 BZL-B、安装扭矩、复用禁令和进/回油节流选择。 |
| LKV-SI-019 | 37-38 / 1261-1262 | BZL 外形与流量特性 | DRAWING + CHART | LOW | 独立附件尺寸和流量曲线不属于 LKV 核心能力，排除。 |
| LKV-SI-020 | 39-40 / 1265-1266 | BZX 排气阀 | MODEL + TABLE + CAUTION | LOW | 独立排气阀规格和操作不属于 LKV 核心产品，排除。 |
| LKV-SI-021 | 41-42 / 1267-1268 | JZG G 螺纹堵头 | MODEL + TABLE + CAUTION | LOW | 独立堵头规格排除；低压排气原则由通用施工对象覆盖。 |
| LKV-SI-022 | 43-44 / 1269-1270 | BZS 直装式顺序阀 | MODEL + TABLE + CAUTION | LOW | 独立顺序阀并非 LKV 专用必需件，排除。 |
| LKV-SI-023 | 45-46 / 1271-1272 | BZS 外形、动作与安装 | DRAWING + TEXT + CAUTION | LOW | 独立顺序阀的 P1/P2 和调压范围不迁移为 LKV 本体要求，排除。 |
| LKV-SI-024 | 47-48 / 1713-1714 | LZV0010 传感单元 | MODEL + TABLE + TEXT | MEDIUM | 纳入 LKV 对应的集成传感单元功能和连接边界；电气采购配置不扩展。 |
| LKV-SI-025 | 49-50 / 1715-1716 | LZV0020/LZV0030 及线缆 | MODEL + TABLE + CAUTION | LOW | 独立传感器和线缆型号采购信息排除。 |
| LKV-SI-026 | 51-52 / 1749-1750 | 公司地址与销售网络 | TEXT + DRAWING | LOW | 非耐久技术联系信息，排除。 |

## 3. Question Statistics

- Total: 15
- FACT: 2
- SPEC_LOOKUP: 3
- TABLE: 2
- MODEL: 1
- CALCULATION: 1
- CHART: 1
- PROCEDURE: 2
- CAUTION: 3

## 4. Questions

## LKV-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV0550-CLE-H

### Question

请按 PDF 的型号表示顺序解读 `LKV0550-CLE-H` 的主体尺寸、设计编号、配管方式、
压板方向、固定字母 `E` 和选配件，并判断该写法是否属于资料明确列出的型号范例。

### Standard Answer

`LKV0550-CLE-H` 中，`055` 表示本体夹紧器部分外径 phi 55 mm；`0` 是设计编号；
`C` 表示板式配管型并配有 G 螺纹堵头；`L` 表示配管口朝向观察者时压板向左夹紧；
`E` 是位于压板方向后的固定字母，必须保留；`H` 表示高强度链接板型，并增大容许偏心量。
该完整写法是资料直接列出的型号范例，字段值和顺序符合资料的型号表示。

### Scoring Standard

- P1 [15]: 正确说明 `055` 表示本体夹紧器部分外径 phi 55 mm。
- P2 [10]: 正确说明 `0` 是设计编号。
- P3 [15]: 正确说明 `C` 为板式配管型并配有 G 螺纹堵头。
- P4 [15]: 正确说明 `L` 是压板向左夹紧。
- P5 [10]: 正确说明固定字母 `E` 的位置并保留该字母。
- P6 [20]: 正确说明 `H` 为高强度链接板型且容许偏心量增大。
- P7 [15]: 明确判断该完整写法是资料列出的型号范例且字段顺序正确。

### Accepted Variants

- `phi 55 mm` 可写为 `φ55 mm`、`Φ55 mm` 或 `直径 55 mm`。
- `板式配管型` 可写为 `板式连接型`，但必须保留 G 螺纹堵头。
- `高强度链接板` 可写为 `高强度连杆板`，但必须保留容许偏心量增大的含义。

### Forbidden Errors

- 将 `L` 解释为低压型或左侧配管，而不是压板向左夹紧。
- 省略、移动或改写固定字母 `E`。
- 将 `H` 解释为快换压板 A 型或带凸缘销 K 型。
- 声称任意主体尺寸、压板方向和选配件组合均已被资料批准。

### Tolerance

- 型号代码、字段顺序和主体尺寸必须精确匹配；无数值容差。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 11
- Printed page: 813
- Section: LKV 型号表示
- Local scope path: LKV > 型号表示 > LKV0550-CLE-H 范例及字段 1-5
- Evidence type: MODEL + DRAWING + TEXT
- Evidence: 型号表示图定义主体尺寸、设计编号、配管方式、压板方向和选配件，显示方向字段后固定为 `E`；同页直接列出 `LKV0550-CLE-H` 范例，并定义 `055`、`0`、`C`、`L`、`H` 的含义。

## LKV-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV 全系列的驱动与动作确认架构

### Question

LKV 的驱动方式、动作确认气路数量和可确认的动作分别是什么？该确认机构主要面向哪类设备？

### Standard Answer

LKV 是液压复动型杠杆式夹紧器。其动作确认只使用一路气，即可同时检知夹紧和松开
两个动作；该新型动作确认机构主要面向需要夹紧、释放确认的自动化设备或自动化流水线。

### Scoring Standard

- P1 [30]: 正确说明 LKV 为液压复动型。
- P2 [35]: 正确说明动作确认只使用一路气。
- P3 [20]: 正确说明该一路气同时确认夹紧和松开两个动作。
- P4 [15]: 正确说明主要应用于需要动作确认的自动化设备或自动化流水线。

### Accepted Variants

- `松开` 可写为 `释放`。
- `一路气` 可写为 `单气路` 或 `一个气路`。

### Forbidden Errors

- 声称夹紧确认和松开确认必须分别使用两路气。
- 将 LKV 说成弹簧释放的液压单动型。

### Tolerance

- N/A

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 807
- Section: 单回路双向检知型杠杆式夹紧器
- Local scope path: LKV > 产品首页 > 驱动方式、新型动作确认机构及一路气对比图
- Evidence type: TEXT + DRAWING
- Evidence: 页面将 LKV 标为液压复动型，明确写明仅用一路气可同时检知夹紧及松开动作，并说明该机构适用于需要夹紧、释放确认的自动化设备。

## LKV-Q-0003

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV 剖面结构中的防冷却液密封

### Question

LKV 的防冷却液密封采用了哪些设计和材料措施？资料对高压冷却液及长期使用氯系冷却液分别给出什么结论？

### Standard Answer

LKV 采用专用防尘设计，因此对高压冷却液具有很高的密封性能；同时采用高性能耐腐蚀
防尘材料，即使长期使用氯系冷却液，也不会降低密封性能。

### Scoring Standard

- P1 [25]: 正确说明采用专用防尘设计。
- P2 [25]: 正确说明对高压冷却液具有很高的密封性能。
- P3 [25]: 正确说明采用高性能耐腐蚀防尘材料。
- P4 [25]: 正确说明长期使用氯系冷却液不会降低密封性能。

### Accepted Variants

- `防尘材料` 可写为 `防尘密封材料`。
- `不会降低密封性能` 可写为 `密封性能不会下降`。

### Forbidden Errors

- 声称资料允许任何冷却液从排气孔进入夹紧器。
- 将耐氯系冷却液结论扩大为对所有未知腐蚀介质均无条件适用。

### Tolerance

- N/A

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 808
- Section: 剖面结构
- Local scope path: LKV > 剖面结构 > 优异的防冷却液密封
- Evidence type: TEXT
- Evidence: 页面把专用防尘设计与高压冷却液密封性能相连，并把高性能耐腐蚀防尘材料与长期使用氯系冷却液时密封性能不降低相连。

## LKV-Q-0004

**Type: SPEC_LOOKUP**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV0400 的薄型夹具示例及 LKV 直装速度控制阀接口

### Question

在资料展示的 LKV0400 薄型夹具示例中，夹具基板最小厚度是多少？LKV 可直接安装哪类速度控制阀，该阀是否随夹紧器提供？

### Standard Answer

LKV0400 示例中的夹具基板最小厚度为 20 mm。LKV 可直接安装带内置排气功能的速度
控制阀，但该速度控制阀需要另行购买，不随夹紧器提供。

### Scoring Standard

- P1 [40]: 正确给出 LKV0400 示例的最小夹具基板厚度为 20 mm。
- P2 [35]: 正确说明可直接安装带内置排气功能的速度控制阀。
- P3 [25]: 正确说明速度控制阀需要另行购买。

### Accepted Variants

- `20 mm` 可写为 `20毫米`。
- `内置排气功能` 可写为 `带排气功能`，但不得省略该功能边界。

### Forbidden Errors

- 将 20 mm 宣称为所有 LKV 型号的通用最小基板厚度。
- 声称速度控制阀是夹紧器的标准随附件。

### Tolerance

- 最小厚度必须精确为 20 mm；无数值容差。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 808
- Section: 剖面结构
- Local scope path: LKV > 剖面结构 > 可实现超薄型的夹具设计、可以直接安装的速度控制阀
- Evidence type: DRAWING + TEXT
- Evidence: 剖面图标注夹具基板最小厚度 20 mm 并限定为 LKV0400；相邻说明写明可直接安装内置排气功能的速度控制阀，且需另行购买。

## LKV-Q-0005

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV 空气传感元件的类型、连接数量和推荐供气条件

### Question

为同时确认 LKV 的夹紧与释放动作，空气传感器应采用什么输出类型？一台传感器通常连接几台夹紧器，连接一台时如何处理？推荐空气压力范围是多少，连接四台时还有什么下限要求？

### Standard Answer

应使用两点检出型空气传感器。一台空气传感器通常连接 2-4 台夹紧器；只连接 1 台时
需要向厂家垂询。推荐空气压力为 0.1-0.2 MPa；连接 4 台夹紧器时，气压必须在
0.15 MPa 以上使用。

### Scoring Standard

- P1 [20]: 正确说明使用两点检出型空气传感器。
- P2 [20]: 正确给出一台传感器连接 2-4 台夹紧器。
- P3 [20]: 正确说明连接一台夹紧器时需要向厂家垂询。
- P4 [20]: 正确给出推荐空气压力 0.1-0.2 MPa。
- P5 [20]: 正确说明连接四台时气压必须在 0.15 MPa 以上。

### Accepted Variants

- `两点检出型` 可写为 `双点检测型` 或 `两点输出型`。
- `向厂家垂询` 可写为 `另行咨询 KOSMEK`。

### Forbidden Errors

- 声称一台传感器可标准连接任意数量的夹紧器。
- 将 0.15 MPa 误写成连接四台时的压力上限。
- 省略 MPa 单位或把推荐空气压力写成液压压力。

### Tolerance

- 连接数量和压力值必须精确匹配；无数值容差。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 811
- Section: 动作原理（关于传感的说明以及空气传感流程图）
- Local scope path: LKV > 关于空气传感元件 > 输出类型、连接数量和推荐空气压力
- Evidence type: TEXT + TABLE
- Evidence: 页面明确要求两点检出型空气传感器，规定一台传感器连接 2-4 台、连接一台需垂询，并给出推荐压力 0.1-0.2 MPa 及连接四台时 0.15 MPa 以上的条件。

## LKV-Q-0006

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV 规格表中的通用压力、温度、流体和空气压力边界

### Question

请给出 LKV 规格表规定的最高使用油压、最低动作油压、耐压、推荐空气压力、使用温度范围和使用流体。

### Standard Answer

LKV 的最高使用油压为 7.0 MPa，最低动作油压为 1.0 MPa，耐压为 10.5 MPa；推荐
空气压力为 0.1-0.2 MPa；使用温度范围为 0-70 °C；使用流体为相当于 ISO-VG-32
粘度等级的一般液压油。

### Scoring Standard

- P1 [20]: 正确给出最高使用油压 7.0 MPa。
- P2 [20]: 正确给出最低动作油压 1.0 MPa。
- P3 [20]: 正确给出耐压 10.5 MPa。
- P4 [15]: 正确给出推荐空气压力 0.1-0.2 MPa。
- P5 [10]: 正确给出使用温度范围 0-70 °C。
- P6 [15]: 正确说明使用 ISO-VG-32 一般液压油。

### Accepted Variants

- `7.0 MPa`、`1.0 MPa` 可分别写为 `7 MPa`、`1 MPa`。
- `0-70 °C` 可写为 `0～70℃`。
- `ISO-VG-32` 可写为 `ISO VG 32`。

### Forbidden Errors

- 将最低动作油压写成推荐空气压力。
- 将 10.5 MPa 耐压当作允许连续使用的最高油压。
- 省略压力单位或把空气压力和油压互换。

### Tolerance

- 压力、温度范围和油液等级必须精确匹配；无数值容差。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 814
- Section: 规格
- Local scope path: LKV > 规格表 > 全型号通用油压、空气压力、温度与流体行
- Evidence type: TABLE
- Evidence: 规格表的全型号共通栏给出最高使用压力 7.0 MPa、最低动作压力 1.0 MPa、耐压 10.5 MPa、推荐空气压力 0.1-0.2 MPa、0-70 °C 和 ISO-VG-32 一般液压油。

## LKV-Q-0007

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV0550-C□E-□ 规格表列

### Question

根据 LKV 规格表，给出 LKV0550 的夹紧侧面积、全行程、夹紧行程、行程余量和不含压板的夹紧器单体重量。

### Standard Answer

LKV0550 的夹紧侧面积为 8.84 cm²，全行程为 26 mm，夹紧行程为 23 mm，行程余量
为 3 mm；不含压板的夹紧器单体重量为 1.6 kg。

### Scoring Standard

- P1 [25]: 正确给出夹紧侧面积 8.84 cm²。
- P2 [20]: 正确给出全行程 26 mm。
- P3 [20]: 正确给出夹紧行程 23 mm。
- P4 [15]: 正确给出行程余量 3 mm。
- P5 [20]: 正确给出不含压板的单体重量 1.6 kg。

### Accepted Variants

- `cm²` 可写为 `平方厘米`。
- `不含压板` 可写为 `除压板外`。

### Forbidden Errors

- 混用其他主体尺寸型号的列值。
- 声称 1.6 kg 包含压板重量。
- 将全行程、夹紧行程和行程余量互换。

### Tolerance

- 表格值和单位必须精确匹配；无数值容差。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 814
- Section: 规格
- Local scope path: LKV > 规格表 > LKV0550-C□E-□ 列 > 夹紧侧面积、行程与重量行
- Evidence type: TABLE
- Evidence: LKV0550 列分别给出夹紧侧面积 8.84 cm²、全行程 26 mm、夹紧行程 23 mm、行程余量 3 mm 和重量 1.6 kg；表下注明重量不含压板。

## LKV-Q-0008

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV0400、LKV0480、LKV0550、LKV0650、LKV0750 的全行程与单体重量比较

### Question

仅在 LKV0400、LKV0480、LKV0550、LKV0650、LKV0750 中选择：若要求全行程至少 26 mm，且不含压板的夹紧器单体重量不超过 1.6 kg，哪个型号满足两项条件？请用规格表数值说明其余型号为何不满足。

### Standard Answer

只有 LKV0550 满足两项条件，其全行程为 26 mm，单体重量为 1.6 kg。LKV0400 和
LKV0480 的重量分别为 0.8 kg、1.2 kg，但全行程只有 20.5 mm、23.5 mm，不足
26 mm；LKV0650 和 LKV0750 的全行程分别为 29.5 mm、35 mm，但重量分别为
2.7 kg、3.8 kg，超过 1.6 kg。规格表中的重量均为不含压板的夹紧器单体重量。

### Scoring Standard

- P1 [30]: 正确选择 LKV0550。
- P2 [20]: 正确给出 LKV0550 的 26 mm 全行程和 1.6 kg 重量。
- P3 [20]: 正确说明 LKV0400、LKV0480 因全行程 20.5 mm、23.5 mm 而不满足。
- P4 [20]: 正确说明 LKV0650、LKV0750 因重量 2.7 kg、3.8 kg 而不满足。
- P5 [10]: 正确说明重量口径不含压板。

### Accepted Variants

- `至少 26 mm` 可表述为 `大于或等于 26 mm`。
- `不超过 1.6 kg` 可表述为 `小于或等于 1.6 kg`。

### Forbidden Errors

- 选择两个或更多型号作为同时满足条件的答案。
- 把不同型号的全行程和重量拼接成一个虚构型号结果。
- 把压板重量计入规格表中的夹紧器单体重量。

### Tolerance

- 型号、表格值和单位必须精确匹配；无数值容差。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 814
- Section: 规格
- Local scope path: LKV > 规格表 > 五个主体尺寸型号列 > 全行程与重量行
- Evidence type: TABLE
- Evidence: 五个型号的全行程依次为 20.5、23.5、26、29.5、35 mm，重量依次为 0.8、1.2、1.6、2.7、3.8 kg；表下注明重量不含压板。

## LKV-Q-0009

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV0550，供给油压 P=4.0 MPa，压板长度 L=70 mm

### Question

LKV0550 在供给油压 `P=4.0 MPa`、压板长度 `L=70 mm` 时，按资料公式
`F=(16.70×P)/(L-21)` 计算夹紧力。请给出代入过程、未舍入结果、按
`ROUND_HALF_UP` 保留 1 位小数的最终结果及单位，并用未舍入结果反代油压。

### Standard Answer

代入公式：

`F=(16.70×4.0)/(70-21)=66.80/49=1.363265306122448979591836735 kN`

按 `ROUND_HALF_UP` 保留 1 位小数，最终夹紧力为 `1.4 kN`。用未舍入结果反代：

`P=F×(L-21)/16.70=1.363265306122448979591836735×49/16.70≈4.0 MPa`

反代结果与输入油压一致。

### Scoring Standard

- P1 [15]: 正确使用 LKV0550 公式 `F=(16.70×P)/(L-21)`。
- P2 [15]: 正确代入 `P=4.0 MPa` 和 `L=70 mm`。
- P3 [15]: 正确计算分母 `70-21=49 mm`。
- P4 [20]: 正确给出未舍入结果 `1.363265306122448979591836735 kN`，或足以得到相同舍入值的等价高精度结果。
- P5 [20]: 按 `ROUND_HALF_UP` 给出最终结果 `1.4 kN`。
- P6 [15]: 使用未舍入结果反代并得到约 `4.0 MPa`。

### Accepted Variants

- 未舍入值可写为 `1.3632653061 kN` 或更多有效位。
- `ROUND_HALF_UP` 可写为 `四舍五入`，但最终结果必须为 1 位小数。

### Forbidden Errors

- 把分母写成 `L`，漏掉支点偏移量 `21 mm`。
- 使用其他主体尺寸型号的系数或偏移量。
- 用曲线目测值代替公式计算，或只给最终值而无代入过程。
- 反代时使用已舍入的 `1.4 kN` 并声称其应精确还原 `4.0 MPa`。

### Tolerance

- 最终结果必须按 `ROUND_HALF_UP` 精确舍入为 `1.4 kN`；反代使用未舍入值，接受 `4.0 MPa` 或与其绝对误差不超过 `0.000001 MPa` 的结果。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 815
- Section: 夹紧力曲线图
- Local scope path: LKV > 夹紧力曲线图 > LKV0550 > 夹紧力计算公式
- Evidence type: FORMULA + TABLE
- Evidence: LKV0550 区块规定 `F=(16.70×P)/(L-21)`，并定义 F 为夹紧力 kN、P 为供给油压 MPa、L 为压板长度 mm；表格包含 L=70 mm 且 4.0 MPa 未超过该列最高使用压力。

## LKV-Q-0010

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV0400 夹紧力曲线，压板长度 L=50 mm

### Question

在 LKV0400 夹紧力曲线图上，沿 `L=50 mm` 曲线读取供给油压 `P=4.25 MPa`
时的夹紧力。请给出约值和单位；该压力不是表格中的离散行，必须按曲线读取。

### Standard Answer

在横轴 `4.25 MPa` 处与 `L=50 mm` 曲线相交，纵轴读数约为 `0.9 kN`。

### Scoring Standard

- P1 [20]: 正确选择 LKV0400 的 `L=50 mm` 曲线。
- P2 [20]: 正确在供给油压横轴定位 `4.25 MPa`。
- P3 [40]: 正确读得夹紧力约 `0.9 kN`。
- P4 [20]: 明确结果是曲线约读值并保留 `kN` 单位。

### Accepted Variants

- `约 0.9 kN` 可写为 `大约 0.9 千牛`。

### Forbidden Errors

- 改用其他压板长度曲线或其他主体尺寸型号的图。
- 把横轴 MPa 当成纵轴 kN。
- 声称 `4.25 MPa` 是表格中已有的离散压力行。

### Tolerance

- CHART tolerance: 接受 `0.8-1.0 kN`；必须说明为曲线约读值。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 815
- Section: 夹紧力曲线图
- Local scope path: LKV > 夹紧力曲线图 > LKV0400 > L=50 mm 系列
- Evidence type: CHART
- Evidence: 图表横轴为供给油压 MPa、纵轴为夹紧力 kN；LKV0400 图中的 `L=50 mm` 曲线在 4.25 MPa 处约对应 0.9 kN。该点由页面视觉读取，公式仅用于合理性校验。

## LKV-Q-0011

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV 速度调整步骤与动作时间限制

### Question

调整 LKV 动作速度时，资料规定的动作时间标准、调整前准备、速度控制阀旋转方向和过快动作的后果分别是什么？

### Standard Answer

应按全部动作时间超过 1 秒的标准调整速度。调整前必须排净回路中的空气，否则无法
准确调速。调整时应将速度控制阀从低速侧（小流量）慢慢向高速侧（大流量）旋转；
若动作过快，会加速各部件的磨耗或损伤。

### Scoring Standard

- P1 [25]: 正确说明全部动作时间应超过 1 秒。
- P2 [25]: 正确说明调速前必须排净回路中的空气。
- P3 [25]: 正确说明从低速侧、小流量慢慢向高速侧、大流量调整。
- P4 [25]: 正确说明动作过快会加速部件磨耗或损伤。

### Accepted Variants

- `超过 1 秒` 可写为 `大于 1 秒`。
- `磨耗` 可写为 `磨损`。

### Forbidden Errors

- 从高速侧直接向低速侧作为资料规定的起始调整方法。
- 在回路仍混有空气时进行最终速度设定。
- 将动作时间标准写成不超过 1 秒。

### Tolerance

- 动作时间边界必须为超过 1 秒；无数值容差。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 26
- Printed page: 944
- Section: 油压杠杆式夹紧器注意事项
- Local scope path: 油压杠杆式夹紧器 > 注意事项 > 5) 调整速度
- Evidence type: PROCEDURE + CAUTION
- Evidence: 该项依次规定全部动作时间超过 1 秒、调速前排净回路空气、从低速小流量慢慢向高速大流量调整，并警告动作过快会加速磨耗或损伤。

## LKV-Q-0012

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压系列通用安装施工资料，适用于 LKV
- Model / Scope: LKV_R01_2023KW_C1N.pdf :: 安装施工方面的注意事项 > 排净油压回路内的空气

### Question

LKV 液压回路在配管施工结束后或因泵油箱变空而进入空气时，应按什么顺序排气？请给出供油压力限制、接头操作、排出空气的方法、复紧步骤和优先排气位置。

### Standard Answer

先将油压回路供油压力调整到 2 MPa 以下；将离夹紧器、支撑器最近的配管接头螺母
再旋松一圈；左右摇动配管，使连接部位松动并排出混有空气的液压油；空气排净后拧紧
管接头螺母。在油压回路最上端以及最末端附近进行排气，效果更佳；板式配管时可在
回路最上端附近设置排气阀。

### Scoring Standard

- P1 [20]: 正确将供油压力调整到 2 MPa 以下。
- P2 [20]: 正确将离夹紧器、支撑器最近的配管接头螺母再旋松一圈。
- P3 [20]: 正确说明左右摇动配管并排出混有空气的液压油。
- P4 [20]: 正确说明空气排净后拧紧管接头螺母。
- P5 [20]: 正确说明最上端和最末端附近优先排气，或板式配管在最上端附近设置排气阀。

### Accepted Variants

- `2 MPa 以下` 可写为 `不高于 2 MPa`。
- `左右摇动配管` 可写为 `来回轻摇配管`。

### Forbidden Errors

- 在高于 2 MPa 的供油压力下执行资料所述排气步骤。
- 完成排气后仍保持管接头螺母松开。
- 把空气传感器清洁回路误作液压油路排气步骤。

### Tolerance

- 供油压力必须为 2 MPa 以下；步骤顺序和关键动作必须保持一致。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 27
- Printed page: 1725
- Section: 安装施工方面的注意事项（液压系列通用）
- Local scope path: 液压系列通用事项 > 安装施工方面的注意事项 > 4) 排净油压回路内的空气
- Evidence type: PROCEDURE + TEXT
- Evidence: 编号 4 明确给出 2 MPa 以下、松开最近接头螺母一圈、摇动配管排油、排净后复紧，以及在回路最上端和最末端附近排气更有效的顺序与条件。

## LKV-Q-0013

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV 动作确认系统的排气孔

### Question

LKV 的排气孔在设计、施工和使用时必须怎样处理？应防止哪些物质进入，堵塞会导致什么后果，资料推荐用什么开启压力的单向阀防止侵入？

### Standard Answer

排气孔必须向大气开放，并防止冷却液和切削屑侵入；若排气孔被堵塞，会导致空气
传感器误动作。资料推荐设置低开启压力单向阀，推荐开启压力为 0.005 MPa，以防止
冷却液和切削屑侵入。

### Scoring Standard

- P1 [25]: 正确说明排气孔必须向大气开放。
- P2 [25]: 正确说明必须防止冷却液和切削屑侵入。
- P3 [25]: 正确说明堵塞会导致空气传感器误动作。
- P4 [25]: 正确给出低开启压力单向阀及推荐开启压力 0.005 MPa。

### Accepted Variants

- `误动作` 可写为 `错误动作` 或 `误检`。
- `0.005 MPa` 可写为 `5 kPa`。

### Forbidden Errors

- 封堵排气孔或把排气孔接成封闭回路。
- 声称冷却液可经排气孔进入而不影响传感。
- 把 0.005 MPa 写成动作确认用供气压力。

### Tolerance

- 推荐开启压力必须精确为 0.005 MPa；无数值容差。

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 811
- Section: 设计时、施工时、使用时的注意事项
- Local scope path: LKV > 空气传感元件 > 排气孔的大气开放与防侵入实例
- Evidence type: CAUTION + TEXT + DRAWING
- Evidence: 页面要求排气孔向大气开放、防止冷却液和切削屑侵入，说明堵塞会导致空气传感器误动作，并推荐开启压力 0.005 MPa 的低开启压力单向阀。

## LKV-Q-0014

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV 液压回路设计中的夹紧侧与释放侧供压

### Question

设计 LKV 油压回路时，夹紧侧和释放侧能否同时供给油压？油压回路设计错误会造成什么后果？

### Standard Answer

严禁同时向夹紧侧和释放侧供给油压。油压回路设计错误会导致机器误动作、破损等事故。

### Scoring Standard

- P1 [60]: 明确说明严禁同时向夹紧侧和释放侧供给油压。
- P2 [40]: 正确说明设计错误会导致机器误动作、破损等事故。

### Accepted Variants

- `释放侧` 可写为 `松开侧`。
- `误动作` 可写为 `错误动作`。

### Forbidden Errors

- 声称可通过同时向两侧供压实现正常夹紧或保压。
- 省略禁令而只描述一般性的回路设计建议。

### Tolerance

- N/A

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 943
- Section: 油压杠杆式夹紧器注意事项
- Local scope path: 油压杠杆式夹紧器 > 设计方面的注意事项 > 2) 设计回路时的注意事项
- Evidence type: CAUTION + TEXT
- Evidence: 该条警告油压回路设计错误会导致误动作、破损等事故，并明确严禁同时向夹紧侧和释放侧供给油压；页首适用型号包含 LKV。

## LKV-Q-0015

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKV 单回路双向检知型杠杆式夹紧器
- Model / Scope: LKV 活塞杆受力方向与压板偏心载荷设计

### Question

设计 LKV 压板时，对活塞杆受力方向和压板偏心载荷分别有什么限制？错误施加非轴向力会产生什么机械风险？

### Standard Answer

不得向夹紧器活塞杆施加轴向以外的作用力，否则会使活塞杆产生极大的弯曲应力。
压板承受偏心载荷时，必须在 LKV 容许偏心量表给出的范围内使用。

### Scoring Standard

- P1 [35]: 正确说明不得向活塞杆施加轴向以外的作用力。
- P2 [30]: 正确说明非轴向力会使活塞杆产生极大的弯曲应力。
- P3 [35]: 正确说明压板偏心载荷必须处于 LKV 容许偏心量表范围内。

### Accepted Variants

- `轴向以外的作用力` 可写为 `横向力` 或 `非轴向力`。
- `弯曲应力` 可写为 `弯曲载荷`，但必须保留风险显著增大的含义。

### Forbidden Errors

- 声称 LKV 可无条件承受任意横向力或偏心载荷。
- 把资料中其他型号禁止偏心压板的规则直接改写为 LKV 一律禁止偏心。

### Tolerance

- N/A

### Source

- PDF: LKV_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 943
- Section: 油压杠杆式夹紧器注意事项
- Local scope path: 油压杠杆式夹紧器 > 设计方面的注意事项 > 3) 压板设计方面的注意事项
- Evidence type: CAUTION + TEXT + DRAWING
- Evidence: 该条禁止向活塞杆施加轴向以外的力并说明会产生极大弯曲应力，同时要求压板偏心载荷在容许偏心量表范围内；页首适用型号包含 LKV。
