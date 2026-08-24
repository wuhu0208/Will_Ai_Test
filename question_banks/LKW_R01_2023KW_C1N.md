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

## 3. Question Statistics

- Total: 19
- FACT: 3
- SPEC_LOOKUP: 3
- TABLE: 2
- MODEL: 2
- CALCULATION: 1
- CHART: 2
- PROCEDURE: 2
- CAUTION: 4

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

- Binding: MODEL_FAMILY
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

## LKW-Q-0010

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: `LKW0551` 的夹紧力计算公式

### Question

`LKW0551` 的供给油压 `P=5.0 MPa`、压板长度 `L=50 mm`。按 PDF 公式计算夹紧力
`F`，保留中间未舍入值，并以 `ROUND_HALF_UP` 四舍五入到 `0.01 kN`。再用未舍入的
`F` 反算供给油压，作为计算校验。

### Standard Answer

PDF 对 `LKW0551` 规定 `F=(18.18×P)/(L-21)`，其中 `F` 的单位为 kN、`P` 为 MPa、
`L` 为 mm。代入后分母为 `50-21=29 mm`，未舍入夹紧力为
`18.18×5.0/29=3.134482758620689655... kN`；按 `ROUND_HALF_UP` 到 `0.01 kN`
得到 **`3.13 kN`**。使用未舍入值反算
`P=F×(L-21)/18.18=5.00 MPa`，与输入一致。

### Scoring Standard

- P1 [20]: 正确使用 `LKW0551` 公式 `F=(18.18×P)/(L-21)`。
- P2 [15]: 正确说明 `F/P/L` 的单位分别为 kN、MPa、mm。
- P3 [15]: 正确代入并得到分母 `29 mm`。
- P4 [20]: 给出未舍入值 `3.1344827586... kN`。
- P5 [20]: 按 `ROUND_HALF_UP` 到 `0.01 kN` 得到 `3.13 kN`。
- P6 [10]: 使用未舍入值反算得到 `5.00 MPa`。

### Accepted Variants

- 未舍入值可截写为至少 `3.13448 kN`，但最终舍入值必须为 `3.13 kN`。
- `ROUND_HALF_UP` 可写为明确的十进制四舍五入规则。

### Forbidden Errors

- 使用其他 LKW 主体尺寸的公式系数或偏置量。
- 用规格表的夹紧器面积或 `L=0` 的夹紧器推力代替本公式。
- 对中间值提前舍入后再执行反算。
- 省略最终单位。

### Tolerance

- 最终夹紧力必须按 `ROUND_HALF_UP` 精确舍入到 `0.01 kN`，即 `3.13 kN`；反算值必须为 `5.00 MPa`。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 835
- Section: 夹紧力曲线图
- Local scope path: LKW > 夹紧力曲线图 > LKW0551 表、公式与变量注记
- Evidence type: FORMULA + TABLE
- Evidence: `LKW0551` 栏明确给出 `F=(18.18×P)/(L-21)`，并把 `F/P/L` 分别定义为夹紧力 kN、供给油压 MPa、压板长度 mm；页面同时禁止用规格栏公式求取 `L=0` 的夹紧器推力。

## LKW-Q-0011

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: `LKW0551` 夹紧力曲线中的 `L=70 mm` 系列

### Question

从 `LKW0551` 夹紧力曲线图读取：当压板长度 `L=70 mm`、供给油压 `P=4.2 MPa`
时，夹紧力约为多少？说明所用横轴、纵轴和曲线系列；公式只能作为读图后的合理性校验。

### Standard Answer

横轴是供给油压 `P`（MPa），纵轴是夹紧力 `F`（kN），应沿 `L=70 mm` 曲线读取。
在 `P=4.2 MPa` 处，图上夹紧力约为 **`1.6 kN`**。公式校验值约为
`18.18×4.2/(70-21)=1.56 kN`，与视觉读数一致，但该公式值不是本题标准答案的读图来源。

### Scoring Standard

- P1 [15]: 正确识别横轴为供给油压 `P`，单位 MPa。
- P2 [15]: 正确识别纵轴为夹紧力 `F`，单位 kN。
- P3 [20]: 正确选择 `L=70 mm` 曲线系列。
- P4 [40]: 给出约 `1.6 kN` 的视觉读数，且在规定容差内。
- P5 [10]: 明确公式仅用于合理性校验，未把公式计算冒充图表读取。

### Accepted Variants

- `1.6 kN` 可写为容差范围内的近似值，并明确其为曲线读数。

### Forbidden Errors

- 读取 `L=50 mm`、`L=120 mm` 或其他曲线。
- 把横轴和纵轴互换，或省略单位。
- 声称该非离散输入直接来自表格单元格。

### Tolerance

- CHART 容差：`1.45-1.75 kN`（中心读数约 `1.6 kN`，反映图中 1 kN 主刻度下的视觉读取不确定性）。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 835
- Section: 夹紧力曲线图
- Local scope path: LKW > 夹紧力曲线图 > LKW0551 > `L=70 (s=40)` 曲线
- Evidence type: CHART
- Evidence: `LKW0551` 图以供给油压 MPa 为横轴、夹紧力 kN 为纵轴；`L=70 mm` 曲线在 `P=4.2 MPa` 的交点位于约 `1.6 kN`。

## LKW-Q-0012

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: `LKW0551` 标准/A/K 型与 H 高强度链接板型的容许偏心量曲线

### Question

分别从两张 `LKW0551` 容许偏心量曲线读取：供给油压 `P=4.5 MPa`、压板长度
`L=85 mm` 时，标准型（无符号，A/K 同曲线）与 H 高强度链接板型的容许偏心量
各约多少？哪一种更大，约大多少？

### Standard Answer

标准/A/K 型曲线读数约为 **`17 mm`**；H 高强度链接板型曲线读数约为
**`69 mm`**。H 型更大，差值约为 **`52 mm`**。两张图均以压板长度 `L`（mm）
为横轴、容许偏心量 `H`（mm）为纵轴，并选择 `P=4.5 MPa` 曲线。

### Scoring Standard

- P1 [15]: 正确识别两图横轴为压板长度 `L`、纵轴为容许偏心量 `H`，单位均为 mm。
- P2 [15]: 两图均正确选择 `P=4.5 MPa` 曲线。
- P3 [25]: 标准/A/K 型读数约为 `17 mm`，且在规定容差内。
- P4 [25]: H 型读数约为 `69 mm`，且在规定容差内。
- P5 [10]: 正确判断 H 型容许偏心量更大。
- P6 [10]: 给出约 `52 mm` 的差值，且在规定容差内。

### Accepted Variants

- 标准型可写为 `无符号型`，并可说明 A、K 与其共用该曲线。
- 近似值可按图表容差表达。

### Forbidden Errors

- 将传感阀符号 H 与末尾选配件 H 混淆。
- 把 H 型曲线值用于无符号/A/K 型。
- 用相邻表格离散点冒充 `L=85 mm` 的直接表格值。

### Tolerance

- CHART 容差：标准/A/K 型 `15-19 mm`；H 型 `67-71 mm`；差值 `48-56 mm`。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 15, 17
- Printed page: 837, 839
- Section: 容许偏心量曲线图
- Local scope path: LKW > 容许偏心量曲线图 > LKW0551 > 无符号/A/K 与末尾选配件 H > `P=4.5 MPa`
- Evidence type: CHART
- Evidence: 标准/A/K 图和 H 高强度链接板图分别给出 `LKW0551` 的 `P=4.5 MPa` 曲线；在非离散点 `L=85 mm` 处视觉读数约为 17 mm 与 69 mm。

## LKW-Q-0013

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: `LKW-C□E` 夹紧/释放动作确认型的液压与确认状态

### Question

对 `LKW-C□E`，分别说明向夹紧供油口和释放供油口供压时，活塞杆动作、夹紧/释放
油压 ON/OFF 以及夹紧/释放动作确认 ON/OFF 的对应关系。解除相应侧油压后，资料还提示
了什么弹簧微动边界？

### Standard Answer

向夹紧供油口供压时，活塞杆上升并夹紧工件：夹紧油压 ON、释放油压 OFF，夹紧动作
确认 ON、释放动作确认 OFF；仅 `LKW0401` 在该夹紧状态解除夹紧侧油压时，活塞杆可能
受内置弹簧作用发生微动。向释放供油口供压时，活塞杆下降并释放：夹紧油压 OFF、
释放油压 ON，夹紧动作确认 OFF、释放动作确认 ON；在该释放状态解除释放侧油压时，
活塞杆可能受内置弹簧作用发生微动。

### Scoring Standard

- P1 [15]: 正确说明夹紧供压使活塞杆上升并夹紧工件。
- P2 [10]: 正确给出夹紧状态油压为夹紧 ON、释放 OFF。
- P3 [15]: 正确给出夹紧状态确认为夹紧 ON、释放 OFF。
- P4 [15]: 正确说明释放供压使活塞杆下降并释放工件。
- P5 [10]: 正确给出释放状态油压为夹紧 OFF、释放 ON。
- P6 [15]: 正确给出释放状态确认为夹紧 OFF、释放 ON。
- P7 [10]: 正确说明释放状态解除释放侧油压后可能发生弹簧微动。
- P8 [10]: 正确限定夹紧状态解除夹紧侧油压后的微动提示仅适用于 `LKW0401`。

### Accepted Variants

- `ON/OFF` 可写为 `开启/关闭` 或 `有压/无压`，但必须保持四个状态对应关系准确。

### Forbidden Errors

- 将夹紧与释放时的活塞杆方向或确认信号对调。
- 声称夹紧和释放油压应同时为 ON。
- 把 `LKW0401` 的夹紧侧微动例外扩展到全部 LKW 型号。

### Tolerance

- 状态、方向和型号例外必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 829
- Section: 动作原理（剖面结构）
- Local scope path: LKW > 动作原理 > `LKW-C□E` 夹紧状态表、释放状态表与弹簧微动注记
- Evidence type: STATE_DIAGRAM + TEXT
- Evidence: 夹紧图和释放图分别给出活塞杆方向、两侧油压与两个动作确认的 ON/OFF 表；夹紧侧解除供压后的微动注记只标于 LKW0401，释放侧解除供压后的微动注记未限于该型号。

## LKW-Q-0014

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: LKW 动作确认空气回路的排气、防侵入与检出稳定性

### Question

为避免 LKW 动作确认误检，排气口/排气孔和连接气管应如何处理？若使用低开启压力
单向阀，资料推荐什么系列和开启压力？为什么不宜选空气消耗量过大的空气传感器？

### Standard Answer

排气口/排气孔必须向大气开放，并防止冷却液和切削屑侵入；堵塞会导致空气传感器
误动作。可设置低开启压力单向阀，推荐 SMC `AKH` 系列、开启压力 `0.005 MPa`。
连接气管应尽可能短，基准为 `5 m` 以内。空气消耗量过大的传感器会使传感阀开启时
的传感压力升高，导致检出压差减小。

### Scoring Standard

- P1 [15]: 正确说明排气口/排气孔必须向大气开放。
- P2 [15]: 正确说明必须防止冷却液和切削屑侵入。
- P3 [15]: 正确说明堵塞会导致空气传感器误动作。
- P4 [15]: 正确给出推荐单向阀为 SMC `AKH` 系列。
- P5 [10]: 正确给出开启压力 `0.005 MPa`。
- P6 [15]: 正确说明连接气管应尽可能短，基准 `5 m` 以内。
- P7 [15]: 正确说明高耗气量会抬高阀开启时压力并减小检出压差。

### Accepted Variants

- `大气开放` 可写为 `不得封堵并直接通大气`。
- `AKH` 可写为 `SMC AKH 系列`。

### Forbidden Errors

- 建议封闭排气孔来阻止冷却液进入。
- 将 `0.005 MPa` 写成空气传感器供给压力。
- 声称空气消耗量越大，检出压差必然越大。

### Tolerance

- 单向阀系列、开启压力和气管长度基准必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 9-10
- Printed page: 831-832
- Section: 动作原理与空气传感流程图注意事项
- Local scope path: LKW > 空气传感流程图 > 排气口防侵入实例、连接气管与传感阀开启压力注记
- Evidence type: CAUTION + TEXT + STATE_DIAGRAM
- Evidence: 页面要求排气口大气开放并防止冷却液/切削屑侵入，给出堵塞导致误动作、SMC AKH 0.005 MPa 单向阀、连接气管 5 m 以内基准，以及高耗气传感器减小检出压差的因果关系。

## LKW-Q-0015

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器及 LZK 毛坯压板
- Model / Scope: 为 LKW 设计加工 LZK 毛坯压板时的长度和加工尺寸边界

### Question

使用 LZK 毛坯压板为 LKW 自行设计加工压板时，压板长度和加工尺寸分别应依据什么
确定？若超出资料表规定的加工尺寸范围，可能出现哪些结果？

### Standard Answer

压板长度应依据对应 LKW 的能力曲线图确定；设计加工尺寸必须保持在毛坯压板表规定
的尺寸范围内。超出范围会使夹紧力无法满足规格值，并可能导致变形、卡住、
动作不正常。

### Scoring Standard

- P1 [25]: 正确说明压板长度应依据对应 LKW 能力曲线图确定。
- P2 [25]: 正确说明加工尺寸必须在毛坯压板表规定范围内。
- P3 [20]: 正确说明超范围会使夹紧力无法满足规格值。
- P4 [10]: 正确说明可能导致变形。
- P5 [10]: 正确说明可能导致卡住。
- P6 [10]: 正确说明可能导致动作不正常。

### Accepted Variants

- `卡住` 可写为 `卡滞`。
- `夹紧力无法满足规格值` 可写为 `达不到规定夹紧力`。

### Forbidden Errors

- 仅按毛坯外形或经验任意决定压板长度。
- 声称超出表中尺寸范围只影响外观，不影响能力或动作。

### Tolerance

- N/A

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 28
- Printed page: 850
- Section: 压板设计尺寸 / 附件：毛坯压板
- Local scope path: LKW > LZK 毛坯压板 > 压板设计尺寸计算方法表 > 注意事项 1-2
- Evidence type: CAUTION + TABLE + DRAWING
- Evidence: 页面要求依据能力曲线图确定压板长度，并禁止超出表中加工尺寸范围；明确列出夹紧力不满足规格值以及变形、卡住、动作不正常的后果。

## LKW-Q-0016

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: LKW 速度调整步骤与动作时间边界

### Question

对 LKW 调整动作速度时，应遵循什么动作时间基准、准备步骤和调节方向？未排净空气
或把动作调得过快分别会有什么后果？

### Standard Answer

全部动作时间应调整为超过 `1 s`。调整前必须排净液压回路中的空气；随后从低速侧
（小流量）开始，缓慢向高速侧（大流量）方向旋转速度控制阀。回路中混有空气时无法
准确调整速度；动作过快会加速各部件磨耗或损伤。

### Scoring Standard

- P1 [20]: 正确给出全部动作时间应超过 `1 s`。
- P2 [20]: 正确说明调整前必须排净回路中的空气。
- P3 [20]: 正确说明从低速侧（小流量）开始。
- P4 [15]: 正确说明缓慢向高速侧（大流量）方向调整。
- P5 [10]: 正确说明混有空气时无法准确调整速度。
- P6 [15]: 正确说明动作过快会加速部件磨耗或损伤。

### Accepted Variants

- `超过 1 s` 可写为 `大于 1 秒`。
- `低速侧到高速侧` 可写为 `由小流量逐步增至大流量`。

### Forbidden Errors

- 在未排气时直接进行最终速度设定。
- 从高速/大流量侧开始快速向更高速度调整。
- 将动作时间基准写成不超过 1 s。

### Tolerance

- 动作时间边界和调整顺序必须精确匹配；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 29-30
- Printed page: 943-944
- Section: 油压杠杆式夹紧器注意事项
- Local scope path: 杠杆式夹紧器全般 > 安装施工方面的注意事项 > 5. 调整速度
- Evidence type: PROCEDURE + CAUTION + TEXT
- Evidence: 专用注意事项规定全部动作时间超过 1 s、先排净空气，并从低速小流量侧缓慢调向高速大流量侧；同时给出混气无法准确调整和过快加速磨耗/损伤的后果。

## LKW-Q-0017

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LKW 传感器内置式杠杆式夹紧器
- Model / Scope: LKW 复动液压速度控制回路

### Question

为 LKW 设计复动液压速度控制回路时，夹紧侧与释放侧应采用哪种节流方式？能否同时
向两侧供压？若改用进油节流或回路设计错误，资料指出什么风险？

### Standard Answer

LKW 是复动夹紧器且不在资料列出的进油节流例外型号中，因此夹紧侧和释放侧都应采用
回油节流。严禁同时向夹紧侧和释放侧供给油压。采用进油节流时容易受回路中混入空气
影响，难以控制速度；液压回路设计错误会导致装置误动作或损坏。

### Scoring Standard

- P1 [25]: 正确说明 LKW 的夹紧侧采用回油节流。
- P2 [25]: 正确说明 LKW 的释放侧也采用回油节流。
- P3 [20]: 正确说明严禁同时向夹紧侧和释放侧供压。
- P4 [15]: 正确说明进油节流易受混入空气影响而难以控制速度。
- P5 [15]: 正确说明回路设计错误可能导致误动作或损坏。

### Accepted Variants

- `回油节流` 可写为 `出口节流` 或 `meter-out`。

### Forbidden Errors

- 将 LKW 误列为必须在两侧使用进油节流的例外型号。
- 建议同时给夹紧侧和释放侧加压来提高速度。
- 只在一侧设置回油节流而声称符合资料要求。

### Tolerance

- N/A

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 29, 31-32
- Printed page: 943, 1725-1726
- Section: 杠杆式夹紧器设计注意事项 / 夹紧器的速度控制回路及注意事项
- Local scope path: 杠杆式夹紧器全般 > 设计回路时的注意事项；液压系列通用事项 > 复动夹紧器的速度控制回路
- Evidence type: CAUTION + TEXT
- Evidence: 杠杆式夹紧器专用页禁止同时向夹紧侧和释放侧供压；通用速度回路页规定非例外复动夹紧器两侧均用回油节流，并说明进油节流受混气影响以及错误设计导致误动作/损坏。

## LKW-Q-0018

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压夹紧装置
- Model / Scope: LKW_R01_2023KW_C1N.pdf :: 适用于 LKW 的液压装置操作与保养通用事项

### Question

对装有 LKW 的液压装置进行拆卸、维护和重新启动时，资料要求哪些关键安全步骤？日常
应怎样维护活塞杆/柱塞周围及连接部位，并检查哪些运行状态？

### Standard Answer

拆卸或维护前，应先对被驱动物体落实防坠落和防误动作措施，切断压力源与电源，并确认
油压、气压回路压力为零；刚停止的设备须待完全冷却后再拆卸。重新启动前应检查螺栓等
连接部位有无异常。日常应定期清扫活塞杆和柱塞周围，避免污物损伤密封而导致动作不正常
或漏油；还应检查配管、安装螺栓、螺母、固定环和夹紧器是否松动并及时加固，同时确认
液压油是否老化、有无异音以及动作是否正常顺畅。

### Scoring Standard

- P1 [15]: 正确说明拆卸前应落实防坠落和防误动作措施。
- P2 [15]: 正确说明必须切断压力源和电源。
- P3 [15]: 正确说明必须确认油压、气压回路压力为零。
- P4 [10]: 正确说明刚停止的设备须完全冷却后再拆卸。
- P5 [10]: 正确说明重新启动前检查螺栓等连接部位异常。
- P6 [15]: 正确说明定期清扫活塞杆/柱塞周围及污物对密封、动作和漏油的后果。
- P7 [10]: 正确说明定期检查配管、紧固件、固定环和夹紧器松动并加固。
- P8 [10]: 正确说明检查油液老化、异音和动作是否正常顺畅。

### Accepted Variants

- `防误动作` 可写为 `防止意外启动`。
- `压力为零` 可写为 `完全卸压`，但必须同时覆盖油压与气压回路。

### Forbidden Errors

- 仅断电而不切断压力源或不确认回路压力为零。
- 在设备尚未冷却时立即拆卸。
- 声称活塞杆周围污物不会影响密封或漏油。

### Tolerance

- N/A

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 33-34
- Printed page: 1727-1728
- Section: 操作方面的注意事项 / 保养、检查
- Local scope path: 液压系列通用事项 > 操作方面的注意事项 2；保养、检查 1-7
- Evidence type: PROCEDURE + CAUTION + TEXT
- Evidence: 操作事项规定防坠落/防误动作、切断压力和电源、确认回路零压、等待冷却和重启前检查；保养事项规定清扫活塞杆/柱塞、检查松动、油液老化、异音和动作状态，并给出污物损伤密封及漏油后果。

## LKW-Q-0019

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZL 低压速度控制阀，用于 LKW 直装速度控制
- Model / Scope: `BZL0101-B` 与 `BZL0201-B` 的安装紧固和复用边界

### Question

把 `BZL0101-B` 或 `BZL0201-B` 安装到对应 LKW 时，各自的本体推荐紧固力矩是多少？
为什么紧固不足会使流量无法调整？已使用过的 BZL 能否改装到另一台夹紧器？

### Standard Answer

`BZL0101-B` 的本体推荐紧固力矩为 `10 N·m`，`BZL0201-B` 为 `25 N·m`。
BZL 端面采用金属密封结构，紧固力矩不足会导致无法调整流量。
已使用过的 BZL 不得再装到其他夹紧器；不同夹紧器的 G 螺纹底面深度可能有差异，
复用会造成金属密封不严密并导致流量无法调整。

### Scoring Standard

- P1 [20]: 正确给出 `BZL0101-B` 推荐紧固力矩 `10 N·m`。
- P2 [20]: 正确给出 `BZL0201-B` 推荐紧固力矩 `25 N·m`。
- P3 [20]: 正确说明 BZL 端面为金属密封结构。
- P4 [15]: 正确说明紧固不足会导致无法调整流量。
- P5 [10]: 正确说明已使用过的 BZL 不得改装到其他夹紧器。
- P6 [15]: 正确说明 G 螺纹底面深度差异会导致金属密封不严密并使流量无法调整。

### Accepted Variants

- `N·m` 可写为 `N m` 或 `牛·米`。
- `不得复用` 可写为 `不能跨夹紧器重复安装`。

### Forbidden Errors

- 将 `10 N·m` 与 `25 N·m` 对调。
- 声称紧固力矩不足只会松动而不影响金属密封和流量调整。
- 建议把已使用的 BZL 任意换装到另一台夹紧器。

### Tolerance

- 紧固力矩必须精确匹配型号；无数值容差。

### Source

- PDF: LKW_R01_2023KW_C1N.pdf
- Physical page: 39-40
- Printed page: 1259-1260
- Section: BZL 速度控制阀（低压用）规格与注意事项
- Local scope path: 控制阀 > BZL > 规格表 > 本体推荐紧固力矩；注意事项 1-2
- Evidence type: TABLE + CAUTION + TEXT
- Evidence: BZL 规格表将 G1/8 的 0101 型和 G1/4 的 0201 型分别绑定 10、25 N·m；注意事项说明端面金属密封、紧固不足无法调流量，以及因不同夹紧器 G 螺纹底面深度差异禁止跨夹紧器复用。
