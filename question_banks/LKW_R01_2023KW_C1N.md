---
schema_version: will-ai-question-bank/v1
source_pdf: LKW_R01_2023KW_C1N.pdf
source_sha256: fa9aeec4f6e0372cfcea2feeca751948b84f2d1e25609b677f8f2cb278c43064
source_pages: 52
question_bank_version: V1
product_scope: LKW
---

# LKW_R01_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LKW_R01_2023KW_C1N.pdf`
- SHA-256: `fa9aeec4f6e0372cfcea2feeca751948b84f2d1e25609b677f8f2cb278c43064`
- 物理页数: 52
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器及文档内直接适用附件
- LKW 主要产品印刷页: 827-850
- 产品总览与专用注意事项印刷页: 749-752、943-944
- 文档内通用资料与附件印刷页: 1257-1272、1725-1730
- 来源证据原则: PDF 页面为 Source Truth；哈希绑定文本缓存仅用于定位，型号排版、图表、状态图和尺寸关系存在歧义时以页面视觉证据为准。

## 2. Scope

### 2.1 产品与文档范围

本题库的主要产品范围是 LKW 传感器内置式杠杆式夹紧器，覆盖液压复动、
夹紧/释放动作确认、传感阀符号、型号表示、规格、夹紧力、容许偏心量、安装、压板
设计，以及 LKW 专用设计、施工和使用注意事项。

PDF 同时收录油压杠杆式夹紧器系列总览、液压通用注意事项、BZL/BZX/JZG/BZS 控制阀
等资料。只有在 Target 明确绑定相应附件或页范围时，才可使用这些资料；不得把
LKA、LKC、LKK、LKV、LJ/LM、LJV、TMV-2、TMA-1 等其他系列的规格迁移到 LKW。

公司地址、销售网点和销售网络图属于非技术联系信息，不进入产品能力题目。

### 2.2 LKW 型号语法

LKW 型号表示的规范结构为：

`LKW<主体尺寸>1-C<压板方向><传感阀符号>[-<选配件>]`

选择无符号标准型时，省略末尾选配件及其前置连字符。传感阀符号是压板方向之后的
必填字段，不得与末尾选配件混淆；字段顺序不得改变。

| 字段 | 资料列出的值 | 含义与约束 |
|---|---|---|
| 主体尺寸 | `040`、`048`、`055`、`065`、`075` | 分别表示本体外径 phi 40、48、55、65、75 mm。 |
| 设计编号 | `1` | 表示产品版本信息。 |
| 配管方式 | `C` | 板式连接型，附带 G 螺纹堵头；速度控制阀由用户另行购买，推荐 BZL-B。 |
| 压板方向 | `L`、`C`、`R` | 面向供油口时，分别表示左、中央、右压板方向。 |
| 传感阀符号 | `E`、`H`、`J` | `E` 为夹紧和释放动作确认型；`H` 为夹紧动作确认型；`J` 为释放动作确认型。 |
| 选配件 | `A`、`H`、`K`、无符号 | `A` 为快换压板 A 型；`H` 为高强度链接板型并增大容许偏心量；`K` 为端面接触式铰链销、C 形挡圈；无符号为标准型。 |

资料要求选配件组合详情另行询问，因此字段值和顺序成立不代表任意组合均已被批准。
特别是字母 `H` 在传感阀字段中表示夹紧动作确认，在末尾选配件字段中则表示高强度链接板。

### 2.3 来源覆盖索引

下表按相邻物理页形成的印刷跨页记录来源对象、优先级和题库范围初始处置。

| Coverage ID | 物理页 / 印刷页 | 局部范围 | 证据类型 | 优先级 | 可测试对象与范围处置 |
|---|---|---|---|---|---|
| LKW-SI-001 | 1-2 / 749-750 | 油压杠杆式夹紧器总览 | TEXT + DRAWING | MEDIUM | 纳入 LKW 所属产品类别和复动边界；其他系列仅作范围排除。 |
| LKW-SI-002 | 3-4 / 751-752 | 杠杆式夹紧器产品类型 | TABLE + TEXT | MEDIUM | 纳入 LKW 传感器内置、低压复动和动作确认类型；其他型号规格不迁移。 |
| LKW-SI-003 | 5-6 / 827-828 | LKW 特点、目录与应用范例 | TEXT + DRAWING | HIGH | `LKW-Q-0002`、`LKW-Q-0003` 覆盖内置传感阀、零泄气、供气口高度和超薄夹具边界。 |
| LKW-SI-004 | 7-8 / 829-830 | 液压动作与内置传感阀原理 | STATE_DIAGRAM + TEXT | HIGH | 纳入夹紧/释放供油、活塞杆动作、阀开闭和确认状态；LKW0401 弹簧微动例外保留。 |
| LKW-SI-005 | 9-10 / 831-832 | 空气传感流程与使用注意 | CHART + STATE_DIAGRAM + CAUTION | HIGH | `LKW-Q-0004` 覆盖供气和推荐元件；检出压差、排气孔防侵入和 E/H/J 状态边界留待 WP3。 |
| LKW-SI-006 | 11-12 / 833-834 | 型号表示与规格 | MODEL + TABLE + DRAWING | HIGH | `LKW-Q-0001`、`LKW-Q-0005` 至 `LKW-Q-0007` 覆盖型号语法、通用规格、代表型号列和传感类型重量差异。 |
| LKW-SI-007 | 13-14 / 835-836 | 夹紧力曲线、表与公式 | TABLE + CHART + FORMULA | HIGH | 纳入代表公式计算与非离散点真实曲线读取。 |
| LKW-SI-008 | 15-16 / 837-838 | 标准/A/K 型容许偏心量 | TABLE + CHART + CAUTION | HIGH | 纳入代表曲线读取及超范围变形、卡滞、漏油后果。 |
| LKW-SI-009 | 17-18 / 839-840 | H 高强度链接板型容许偏心量 | TABLE + CHART + CAUTION | MEDIUM | 保留能体现 H 型与标准型边界差异的代表对象；不逐型号换数。 |
| LKW-SI-010 | 19-20 / 841-842 | E 夹紧/释放确认型外形与安装 | DRAWING + TABLE + CAUTION | HIGH | `LKW-Q-0009` 覆盖代表型号的 G 螺纹接口与速度阀选型；其余安装注意留待 WP3。 |
| LKW-SI-011 | 21-22 / 843-844 | H 夹紧动作确认型外形 | DRAWING + TABLE + CAUTION | MEDIUM | 纳入 H 传感阀符号对应的单夹紧确认结构；重复尺寸不扩展。 |
| LKW-SI-012 | 23-24 / 845-846 | J 释放动作确认型外形 | DRAWING + TABLE + CAUTION | MEDIUM | 纳入 J 传感阀符号对应的单释放确认结构；重复尺寸不扩展。 |
| LKW-SI-013 | 25-26 / 847-848 | A 快换压板型外形与安装 | DRAWING + TABLE + CAUTION | MEDIUM | `LKW-Q-0008` 覆盖 A 型销钉、本体尺寸引用和另售快换套件边界。 |
| LKW-SI-014 | 27-28 / 849-850 | 压板设计与 LZK 毛坯压板 | DRAWING + TABLE + FORMULA + CAUTION | HIGH | 纳入压板长度、加工尺寸、附件边界和超范围失效；采购尺寸不逐型号设题。 |
| LKW-SI-015 | 29-30 / 943-944 | 油压杠杆式夹紧器专用注意事项 | TEXT + PROCEDURE + CAUTION | HIGH | 纳入速度调整、双侧同时供压禁令和载荷边界；其他型号专属条款排除。 |
| LKW-SI-016 | 31-32 / 1725-1726 | 液压安装、油液与速度回路 | TEXT + PROCEDURE + STATE_DIAGRAM | HIGH | 纳入通用排气与适用 LKW 的复动速度回路，不迁移例外型号规则。 |
| LKW-SI-017 | 33-34 / 1727-1728 | 操作、保养与质量保证 | TEXT + PROCEDURE + CAUTION | MEDIUM | 纳入通用安全操作和保养检查；商业保证条款不作为产品能力题。 |
| LKW-SI-018 | 35-36 / 1729-1730 | 表面粗糙度与 O 形圈标示 | TABLE + MODEL | LOW | 仅作跨产品标示参考，不改变 LKW 核心答案，排除。 |
| LKW-SI-019 | 37-38 / 1257-1258 | 控制阀总览 | TABLE + TEXT | MEDIUM | 纳入 LKW 可直接安装控制阀的功能边界；独立附件规格只在明确绑定时使用。 |
| LKW-SI-020 | 39-40 / 1259-1260 | BZL 低压速度控制阀 | MODEL + TABLE + CAUTION | HIGH | `LKW-Q-0009` 覆盖 LKW 推荐 BZL-B、螺纹字段和回油节流；安装紧固和复用禁令留待 WP3。 |
| LKW-SI-021 | 41-42 / 1261-1262 | BZL 外形与流量特性 | DRAWING + CHART | LOW | 独立附件尺寸和流量曲线不属于 LKW 核心能力，排除。 |
| LKW-SI-022 | 43-44 / 1265-1266 | BZX 排气阀 | MODEL + TABLE + CAUTION | LOW | 独立排气阀规格和操作不属于 LKW 核心产品，排除。 |
| LKW-SI-023 | 45-46 / 1267-1268 | JZG G 螺纹堵头 | MODEL + TABLE + CAUTION | LOW | 独立堵头规格排除；低压排气原则由通用施工对象覆盖。 |
| LKW-SI-024 | 47-48 / 1269-1270 | BZS 直装式顺序阀 | MODEL + TABLE + CAUTION | LOW | 独立顺序阀并非 LKW 专用必需件，排除。 |
| LKW-SI-025 | 49-50 / 1271-1272 | BZS 外形、动作与安装 | DRAWING + TEXT + CAUTION | LOW | 独立顺序阀的 P1/P2 和调压范围不迁移为 LKW 本体要求，排除。 |
| LKW-SI-026 | 51-52 / 1749-1750 | 公司地址与销售网络 | TEXT + DRAWING | LOW | 非耐久技术联系信息，排除。 |

## 3. Question Statistics

- Total: 9
- FACT: 2
- SPEC_LOOKUP: 3
- TABLE: 2
- MODEL: 2

## 4. Questions

## LKW-Q-0001

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: LKW 型号表示语法，以 `LKW0481-CRE-H` 为字段解读例

### Question

请按 PDF 的型号字段顺序解读 `LKW0481-CRE-H` 的主体尺寸、设计编号、配管方式、
压板方向、传感阀符号和选配件。请同时说明两个 `H` 字段位置分别代表什么，以及
仅凭字段符合语法能否认定任意选配组合均已被资料批准。

### Standard Answer

`LKW0481-CRE-H` 中，`048` 表示本体外径 phi 48 mm；`1` 是设计编号；`C` 表示
板式连接型并附带 G 螺纹堵头；`R` 表示面向供油口时压板向右；`E` 是传感阀
符号，表示夹紧和释放动作确认型；末尾 `H` 是选配件，表示高强度链接板型并
增大容许偏心量。若 `H` 出现在压板方向后的传感阀字段，则表示夹紧动作确认型，
而不是高强度链接板。该写法的字段顺序符合型号语法，但 PDF 明确要求选配件组合详情
另行询问，因此不能仅凭语法认定任意组合均已被批准。

### Scoring Standard

- P1 [15]: 正确说明 `048` 表示本体外径 phi 48 mm。
- P2 [10]: 正确说明 `1` 是设计编号。
- P3 [15]: 正确说明 `C` 是附带 G 螺纹堵头的板式连接型。
- P4 [15]: 正确说明 `R` 表示面向供油口时压板向右。
- P5 [15]: 正确说明传感阀符号 `E` 表示夹紧和释放动作确认型。
- P6 [15]: 正确说明末尾选配件 `H` 表示高强度链接板型并增大容许偏心量。
- P7 [5]: 正确区分传感阀字段中的 `H` 表示夹紧动作确认型。
- P8 [10]: 明确说明语法正确不等于任意组合均已被批准，选配件组合详情需另行询问。

### Accepted Variants

- `phi 48 mm` 可写为 `φ48 mm`、`Φ48 mm` 或 `直径 48 mm`。
- `板式连接型` 可写为 `板式配管型`，但必须保留 G 螺纹堵头。
- `高强度链接板` 可写为 `高强度连杆板`，但必须保留容许偏心量增大的含义。

### Forbidden Errors

- 将传感阀符号 `H` 和末尾选配件 `H` 解释为同一含义。
- 将 `E` 误作选配件或省略传感阀符号字段。
- 将 `R` 解释为右侧配管，而不是压板向右。
- 声称任意主体尺寸、压板方向、传感阀符号和选配件组合均已被资料批准。

### Tolerance

- 型号字段、顺序和两个 `H` 位置的含义必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 11
- Printed page: 833
- Section: LKW 型号表示
- Local scope path: LKW > 型号表示 > 字段 1-6、传感阀符号与选配件组合注记
- Evidence type: MODEL + DRAWING + TEXT
- Evidence: 型号表示图依次定义主体尺寸、设计编号、配管方式、压板方向、传感阀符号和选配件；同页定义 `E/H/J` 传感功能和无符号/`A/H/K` 选配件，并要求选配件组合详情另行询问。

## LKW-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: LKW 全系列的动作确认与低耗气设计

### Question

LKW 为自动化设备提供了什么内置动作确认结构？资料如何说明该结构对夹具厚度、
传感阀关闭时漏气和空气传感器耗气量选择的影响？

### Standard Answer

LKW 在动作端内置动作确认机构，并把传感阀装入夹紧器本体，适合实现设备自动化；
选择 E 型时，可用于需要夹紧和释放确认的自动化流水线。内置结构可实现超薄型夹具
设计；传感阀关闭时漏气为零，因此可以选择空气消耗量较小的空气传感器。

### Scoring Standard

- P1 [20]: 正确说明动作端内置动作确认机构。
- P2 [20]: 正确说明传感阀内置于夹紧器本体。
- P3 [20]: 正确说明该结构适合实现设备自动化。
- P4 [20]: 正确说明内置结构可实现超薄型夹具设计。
- P5 [10]: 正确说明传感阀关闭时漏气为零。
- P6 [10]: 正确说明可选择空气消耗量较小的空气传感器。

### Accepted Variants

- `动作确认` 可写为 `夹紧/释放状态确认`。
- `漏气为零` 可写为 `关闭状态无空气泄漏`。

### Forbidden Errors

- 声称传感阀必须外置。
- 声称传感阀关闭时仍需要持续排出检测空气。
- 将适用范围扩大为无需空气传感器即可输出确认信号。

### Tolerance

- N/A

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 5-6
- Printed page: 827-828
- Section: LKW 产品首页与剖面结构
- Local scope path: LKW > 产品特点与剖面结构 > 内置动作确认机构、超薄夹具和零漏气说明
- Evidence type: TEXT + DRAWING
- Evidence: 产品首页说明动作端内置确认机构并适用于自动化；剖面页把内置传感阀与超薄夹具相连，并明确传感阀关闭时漏气为零、可选低耗气空气传感器。

## LKW-Q-0003

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: LKW-E 夹紧/释放动作确认型的夹具基板与供气口布置

### Question

对 LKW-E 夹紧/释放动作确认型，资料给出的夹具基板最小厚度是多少，哪个型号是例外？
动作确认用供气口高度在哪些组合中可以共用，夹紧器上还可直接安装什么附件？

### Standard Answer

夹具基板最小厚度通常为 30 mm；`LKW0481-C□E` 是例外，最小厚度为 32 mm。
动作确认用供气口高度在不同主体尺寸的 LKW-E 组合中通用，在 LKW-E 与传感阀内置式
旋转夹紧器 LHW-E 组合时也可共用。夹紧器可直接安装速度控制阀。

### Scoring Standard

- P1 [25]: 正确给出通常最小夹具基板厚度为 30 mm。
- P2 [25]: 正确指出 `LKW0481-C□E` 的例外值为 32 mm。
- P3 [20]: 正确说明不同主体尺寸的 LKW-E 可共用动作确认供气口高度。
- P4 [15]: 正确说明 LKW-E 与 LHW-E 组合时也可共用该高度。
- P5 [15]: 正确说明可直接安装速度控制阀。

### Accepted Variants

- `30 mm`、`32 mm` 可分别写为 `30毫米`、`32毫米`。
- `供气口高度通用` 可写为 `动作确认气路可在同一高度连接`。

### Forbidden Errors

- 将 30 mm 无条件应用于 `LKW0481-C□E`。
- 声称所有未知产品系列都可共用该供气口高度。

### Tolerance

- 厚度值必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 828
- Section: 剖面结构与简单的气路设计
- Local scope path: LKW > 剖面结构 > 超薄夹具、动作确认供气口高度和直装速度控制阀
- Evidence type: DRAWING + TEXT
- Evidence: 剖面图标注夹具基板最小厚度 30 mm，并将 `LKW0481-C□E` 限定为 32 mm；同页说明不同尺寸 LKW-E 以及 LKW-E/LHW-E 组合的供气口高度可共用，并标注可直接安装速度控制阀。

## LKW-Q-0004

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: LKW 动作确认空气传感器的推荐配置

### Question

LKW 要实现动作确认时是否必须配置空气传感器？请给出推荐供气压力、推荐的两种
传感器型号及厂家、回路过滤精度，并说明供气应保持什么状态。

### Standard Answer

实现动作确认必须配置空气传感器。推荐供气压力为 0.1-0.2 MPa；推荐型号为
SMC 的 ISA3-G 空气传感元件，或 CKD 的 GPS3-E 间隙开关。空气回路图要求 5 μm
过滤，并在使用时保持向气口常态供气。

### Scoring Standard

- P1 [15]: 正确说明动作确认必须配置空气传感器。
- P2 [20]: 正确给出推荐供气压力 0.1-0.2 MPa。
- P3 [20]: 正确给出 SMC ISA3-G。
- P4 [20]: 正确给出 CKD GPS3-E。
- P5 [10]: 正确给出 5 μm 过滤精度。
- P6 [15]: 正确说明使用时须保持向气口常态供气。

### Accepted Variants

- `0.1-0.2 MPa` 可写为 `0.1～0.2MPa`。
- `5 μm` 可写为 `5微米`。
- `常态供气` 可写为 `持续供气`。

### Forbidden Errors

- 将 0.1-0.2 MPa 写成液压供油压力。
- 将 ISA3-G 与 GPS3-E 的厂家互换。
- 声称动作确认期间可以停止供气。

### Tolerance

- 压力范围、型号和过滤精度必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 831
- Section: 关于空气传感器
- Local scope path: LKW > 动作原理 > 空气传感器要求、推荐表与空气回路图
- Evidence type: TABLE + STATE_DIAGRAM + TEXT
- Evidence: 页面要求动作确认配置空气传感器，给出 0.1-0.2 MPa、SMC ISA3-G、CKD GPS3-E，回路图标注 5 μm，并要求使用时保持常态供气。

## LKW-Q-0005

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: LKW 规格表中的通用压力、温度、流体和空气压力边界

### Question

请给出 LKW 规格表规定的最高使用油压、无负载最低动作油压、耐压、推荐空气压力、
使用温度范围和使用流体。

### Standard Answer

LKW 的最高使用油压为 7.0 MPa，无负载最低动作油压为 0.5 MPa，耐压为 10.5 MPa；
推荐空气压力为 0.1-0.2 MPa；使用温度范围为 0-70 °C；使用流体为相当于
ISO-VG-32 粘度等级的一般液压油。

### Scoring Standard

- P1 [20]: 正确给出最高使用油压 7.0 MPa。
- P2 [20]: 正确给出无负载最低动作油压 0.5 MPa。
- P3 [20]: 正确给出耐压 10.5 MPa。
- P4 [15]: 正确给出推荐空气压力 0.1-0.2 MPa。
- P5 [10]: 正确给出使用温度范围 0-70 °C。
- P6 [15]: 正确说明使用 ISO-VG-32 一般液压油。

### Accepted Variants

- `7.0 MPa` 可写为 `7 MPa`。
- `0-70 °C` 可写为 `0～70℃`。
- `ISO-VG-32` 可写为 `ISO VG 32`。

### Forbidden Errors

- 将最低动作油压写成推荐空气压力。
- 将 10.5 MPa 耐压当作允许连续使用的最高油压。
- 省略压力单位或把空气压力和油压互换。

### Tolerance

- 压力、温度范围和油液等级必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 834
- Section: 规格
- Local scope path: LKW > 规格表 > 全型号通用油压、空气压力、温度与流体行
- Evidence type: TABLE
- Evidence: 规格表共通栏给出最高使用压力 7.0 MPa、最低动作压力 0.5 MPa、耐压 10.5 MPa、推荐空气压力 0.1-0.2 MPa、0-70 °C 和 ISO-VG-32 一般液压油；表下注明最低动作压力为无负载动作值。

## LKW-Q-0006

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: `LKW0551-C□E-□` 规格表列

### Question

根据规格表，给出 `LKW0551-C□E-□` 的夹紧器面积、全行程、夹紧行程、行程余量
和不含压板的夹紧器单体重量。

### Standard Answer

`LKW0551-C□E-□` 的夹紧器面积为 9.62 cm²，全行程为 26 mm，夹紧行程为
23 mm，行程余量为 3 mm；不含压板的夹紧器单体重量为 1.6 kg。

### Scoring Standard

- P1 [20]: 正确给出夹紧器面积 9.62 cm²。
- P2 [20]: 正确给出全行程 26 mm。
- P3 [20]: 正确给出夹紧行程 23 mm。
- P4 [15]: 正确给出行程余量 3 mm。
- P5 [25]: 正确给出不含压板的单体重量 1.6 kg。

### Accepted Variants

- `cm²` 可写为 `平方厘米`。
- `不含压板` 可写为 `除压板外`。

### Forbidden Errors

- 混用其他主体尺寸型号列的数值。
- 声称 1.6 kg 包含压板重量。
- 将全行程、夹紧行程和行程余量互换。

### Tolerance

- 表格值和单位必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 834
- Section: 规格
- Local scope path: LKW > 规格表 > LKW0551-C□E-□ 列 > 夹紧器面积、行程与重量行
- Evidence type: TABLE
- Evidence: LKW0551 列分别给出 9.62 cm²、26 mm、23 mm、3 mm 和选择 E/H 时的 1.6 kg；表下注明重量不含压板。

## LKW-Q-0007

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: LKW 规格表中传感阀符号 E/H 与 J 的单体重量差异

### Question

在 LKW 五种主体尺寸中，哪些尺寸的夹紧器单体重量会因选择 E/H 或 J 传感阀符号
而不同？请给出这些差异值，并说明其余尺寸的重量关系。重量口径是否包含压板？

### Standard Answer

只有 LKW0401 和 LKW0481 的重量因传感阀符号不同。LKW0401 选择 E/H 时为
0.8 kg，选择 J 时为 0.7 kg；LKW0481 选择 E/H 时为 1.2 kg，选择 J 时为
1.1 kg。LKW0551、LKW0651、LKW0751 在 E/H 与 J 下重量相同，分别为
1.6 kg、2.7 kg、3.8 kg。规格表重量均为不含压板的夹紧器单体重量。

### Scoring Standard

- P1 [15]: 正确指出只有 LKW0401、LKW0481 存在 E/H 与 J 的重量差异。
- P2 [15]: 正确给出 LKW0401 的 E/H 重量 0.8 kg。
- P3 [15]: 正确给出 LKW0401 的 J 重量 0.7 kg。
- P4 [15]: 正确给出 LKW0481 的 E/H 重量 1.2 kg。
- P5 [15]: 正确给出 LKW0481 的 J 重量 1.1 kg。
- P6 [15]: 正确说明 0551/0651/0751 不随 E/H/J 改变且分别为 1.6/2.7/3.8 kg。
- P7 [10]: 正确说明重量不含压板。

### Accepted Variants

- `E/H` 可写为 `选择 E 或 H`。
- `不含压板` 可写为 `除压板外`。

### Forbidden Errors

- 声称五种主体尺寸都因 E/H/J 而改变重量。
- 将 E/H 行与 J 行的 0401 或 0481 数值互换。
- 将压板重量计入规格表数值。

### Tolerance

- 型号、重量和单位必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 834
- Section: 规格
- Local scope path: LKW > 规格表 > 重量 > 选择 E/H 行与选择 J 行
- Evidence type: TABLE
- Evidence: 重量两行在 0401、0481 列分别为 0.8/0.7 kg 和 1.2/1.1 kg；0551、0651、0751 两行均为 1.6、2.7、3.8 kg；注 4 限定为除压板外的单体重量。

## LKW-Q-0008

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: 选配件 A 快换压板型

### Question

LKW 选择 `-A` 快换压板型时，与无符号/H/K 型相比，压板安装销和夹紧器本体尺寸
有什么差异？该页尺寸图的范围是什么，快换成套零件是否随本体提供？

### Standard Answer

选择 A 型时，本体不附带压板安装用销钉；杠杆式夹紧器本体尺寸与无符号/H/K 型
一致。A 型页面只记载快换压板部分的尺寸，本体尺寸及安装部加工尺寸应参考 E、H 或 J
相应本体页面。安装罩（含螺栓）、活塞杆销、压板销等快换成套零件为另售品。

### Scoring Standard

- P1 [20]: 正确说明 A 型为快换压板型。
- P2 [20]: 正确说明 A 型本体不附带压板安装用销钉。
- P3 [20]: 正确说明本体尺寸与无符号/H/K 型一致。
- P4 [20]: 正确说明 A 型页只记载快换压板部分尺寸，本体和安装加工尺寸需参考相应本体页。
- P5 [20]: 正确说明安装罩、螺栓、活塞杆销和压板销等快换成套零件为另售品。

### Accepted Variants

- `压板安装用销钉` 可写为 `压板销`。
- `另售品` 可写为 `需要另行购买`。

### Forbidden Errors

- 声称 A 型本体尺寸与无符号/H/K 型不同。
- 声称快换成套零件或压板安装销已随夹紧器本体标准提供。
- 用 A 型局部尺寸图替代本体安装部加工尺寸图。

### Tolerance

- N/A

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 25-26
- Printed page: 847-848
- Section: LKW-A 快换压板 A 型外形尺寸
- Local scope path: LKW > 外形尺寸 > 选配件 A 快换压板型 > 图示范围与另售件注意事项
- Evidence type: DRAWING + TEXT
- Evidence: 页面限定本图只记载 A 型快换压板部分尺寸，说明 A 型不附带压板安装用销钉、本体尺寸与无符号/H/K 一致，并将安装罩、螺栓、活塞杆销和压板销列为另售快换成套零件。

## LKW-Q-0009

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器及 BZL 低压速度控制阀
- Model / Scope: `LKW0551-C□E-□`、`LKW0651-C□E-□` 的直装回油节流速度阀选型

### Question

若分别为 `LKW0551-C□E-□` 和 `LKW0651-C□E-□` 选择资料推荐的 BZL-B 回油节流
速度控制阀，请给出各夹紧器供油口的 G 螺纹尺寸及完整 BZL 型号。型号末尾 `B`
表示什么，速度控制阀是否随 LKW 提供？

### Standard Answer

`LKW0551-C□E-□` 的夹紧、释放供油口均为 G1/8，应选 `BZL0101-B`；
`LKW0651-C□E-□` 的供油口为 G1/4，应选 `BZL0201-B`。BZL 型号中的 `10`
表示 G1/8、`20` 表示 G1/4，设计编号均为 `1`；末尾 `B` 表示回油节流。
速度控制阀由用户另行购买，不随 LKW 提供。

### Scoring Standard

- P1 [15]: 正确给出 LKW0551 的供油口为 G1/8。
- P2 [20]: 正确选择 `BZL0101-B`。
- P3 [15]: 正确给出 LKW0651 的供油口为 G1/4。
- P4 [20]: 正确选择 `BZL0201-B`。
- P5 [15]: 正确说明末尾 `B` 表示回油节流。
- P6 [15]: 正确说明速度控制阀由用户另行购买。

### Accepted Variants

- `G1/8`、`G1/4` 可分别写为 `G 1/8`、`G 1/4`。
- `回油节流` 可写为 `出口节流` 或 `meter-out`。

### Forbidden Errors

- 为 LKW0551 选择 G1/4 的 `BZL0201-B`。
- 为 LKW0651 选择 G1/8 的 `BZL0101-B`。
- 将末尾 `B` 解释为进油节流。
- 声称速度控制阀随 LKW 标准提供。

### Tolerance

- 接口尺寸和型号必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 11, 20, 39
- Printed page: 833, 842, 1259
- Section: LKW 型号表示、LKW-E 外形尺寸表、BZL 型号表示
- Local scope path: LKW > 板式连接型与推荐 BZL-B > LKW-E 供油口 G 螺纹行 > BZL 螺纹尺寸、设计编号和控制方式字段
- Evidence type: MODEL + TABLE + DRAWING + TEXT
- Evidence: LKW 型号页规定速度控制阀另购并推荐 BZL-B；LKW-E 表将 0551 的供油口绑定 G1/8、0651 绑定 G1/4；BZL 型号页把 `10/20` 分别定义为 G1/8/G1/4、设计编号为 1、`B` 定义为回油节流。
