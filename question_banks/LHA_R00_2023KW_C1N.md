---
schema_version: will-ai-question-bank/v1
source_pdf: LHA_R00_2023KW_C1N.pdf
source_sha256: 662f538ada8c6b218e89e59b519079738cde290a3e1c1657116ef3618113947f
source_pages: 68
question_bank_version: V1
product_scope: LHA
---

# LHA_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LHA_R00_2023KW_C1N.pdf`
- SHA-256: `662f538ada8c6b218e89e59b519079738cde290a3e1c1657116ef3618113947f`
- 物理页数: 68
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- 来源证据原则: PDF 页面及其结构化表格、图表、图示和文字为 Source Truth；旧题库与 OCR 仅用于导航和转换。

## 2. Scope

### 2.1 产品与文档范围

本题库覆盖 LHA 油压复动旋转式夹紧器的产品结构、动作原理、型号表示、规格、
夹紧力公式与能力曲线、外形尺寸、空气传感器、压板设计、安装和使用注意事项。
资料中直接列出的 BZL、BZS、BZX、JZG、板式安装座和压板等附件或关联产品，
仅在题目 Target 明确绑定其产品或型号时收录；液压通用注意事项、标示对照和
保修内容按 DOCUMENT_COMMON 绑定。公司地址、销售网点等非技术联系信息不收录。

同一知识对象中仅更换型号或数字的表格题采用代表性样本；不同的型号解析、
图表视觉读取、正算、反算、边界判断和多输出计算能力分别保留。

### 2.2 LHA 型号语法

LHA 主体尺寸代码为 `036`、`040`、`048`、`055`、`065`、`075`、`090`、`105`，
本资料的设计编号为 `0`。配管方式使用 `C`（板式连接）或 `S`（外配管），
夹紧时旋转方向使用 `R`（顺时针）或 `L`（逆时针），配管与方向代码连续书写，
例如 `LHA0480-CL`、`LHA0550-CR-P`，不得写成 `LHA0550-C-R-P`。
动作确认代码包括无符号、`D`、`M`、`N`；选配代码包括 `A`、`F`、`P`、
`Q` 加夹紧行程值以及 `Y30`、`Y45`、`Y60`。动作确认方式与选配件组合时，
必须按资料要求另行确认，不得自行假定任意组合均合法。

### 2.3 来源覆盖索引

下表按物理页汇总实际保留题目。每道题的精确局部范围、证据类型和证据摘要见题目内 Source。

| 物理页 | 印刷页 | 局部范围 | 题目覆盖 |
|---|---|---|---|
| 1 | 499 | 产品总览 | `LHA-Q-0005`-`LHA-Q-0007` |
| 5 | 503 | LHA产品说明、压板设计 | `LHA-Q-0001`、`LHA-Q-0003`、`LHA-Q-0014`-`LHA-Q-0015` |
| 6 | 504 | LHA产品说明 | `LHA-Q-0002`、`LHA-Q-0004` |
| 7 | 505 | LHA附件、型号表示 | `LHA-Q-0022`、`LHA-Q-0024`、`LHA-Q-0026`-`LHA-Q-0031`、`LHA-Q-0067` |
| 8 | 506、508 | LHA规格、Q型夹紧行程范围、夹紧力与规格计算、能力曲线 | `LHA-Q-0017`、`LHA-Q-0055`、`LHA-Q-0098`、`LHA-Q-0206`、`LHA-Q-0212`、`LHA-Q-0214`、`LHA-Q-0228`、`LHA-Q-0230` |
| 9 | 507 | 夹紧力与规格计算、能力曲线 | `LHA-Q-0018`、`LHA-Q-0199`-`LHA-Q-0201`、`LHA-Q-0203`、`LHA-Q-0231` |
| 10 | 506、508 | 夹紧力与规格计算、能力曲线 | `LHA-Q-0198`、`LHA-Q-0206`、`LHA-Q-0209`、`LHA-Q-0217`、`LHA-Q-0221`、`LHA-Q-0223`、`LHA-Q-0225`、`LHA-Q-0230` |
| 11 | 509 | 能力曲线 | `LHA-Q-0019` |
| 12 | 510 | 能力曲线 | `LHA-Q-0021` |
| 14 | 512 | 外形尺寸 | `LHA-Q-0071` |
| 16 | 514 | 外形尺寸 | `LHA-Q-0074` |
| 18 | 516 | 外形尺寸 | `LHA-Q-0077` |
| 20 | 518 | 外形尺寸 | `LHA-Q-0080` |
| 22 | 520 | 外形尺寸 | `LHA-Q-0083` |
| 24 | 522 | 外形尺寸 | `LHA-Q-0086` |
| 26 | 524 | 外形尺寸 | `LHA-Q-0089` |
| 30 | 528 | 外形尺寸 | `LHA-Q-0092` |
| 32 | 530 | 外形尺寸 | `LHA-Q-0095` |
| 33 | 531 | 推荐空气传感器、注意事项、空气传感器 | `LHA-Q-0009`-`LHA-Q-0013`、`LHA-Q-0100`-`LHA-Q-0101`、`LHA-Q-0167` |
| 35 | 533 | 压板设计尺寸 | `LHA-Q-0105` |
| 36 | 534 | F型压板设计尺寸 | `LHA-Q-0103` |
| 37 | 535 | LZH-A附件表、LZH-T附件表、其他压板附件表 | `LHA-Q-0109`、`LHA-Q-0112`、`LHA-Q-0117` |
| 38 | 536 | LZH-F附件表、其他压板附件表 | `LHA-Q-0115`、`LHA-Q-0118` |
| 39 | 745 | LHA专项注意事项、注意事项 | `LHA-Q-0032`、`LHA-Q-0034`-`LHA-Q-0035`、`LHA-Q-0169`-`LHA-Q-0171` |
| 40 | 746 | LHA专项注意事项、注意事项 | `LHA-Q-0033`、`LHA-Q-0172`-`LHA-Q-0173` |
| 41 | 747 | 注意事项 | `LHA-Q-0174` |
| 42 | 748 | LHA专项注意事项、注意事项 | `LHA-Q-0036`-`LHA-Q-0037`、`LHA-Q-0175`、`LHA-Q-0194` |
| 43 | 1725 | 注意事项、液压通用注意事项 | `LHA-Q-0063`-`LHA-Q-0064`、`LHA-Q-0066`、`LHA-Q-0178`-`LHA-Q-0179` |
| 44 | 1726 | 注意事项 | `LHA-Q-0180`-`LHA-Q-0182` |
| 45 | 1727 | 注意事项、液压通用注意事项 | `LHA-Q-0065`、`LHA-Q-0183`-`LHA-Q-0186` |
| 46 | 1728 | 注意事项 | `LHA-Q-0187`-`LHA-Q-0190` |
| 47 | 1729 | 表面粗糙度标示对照 | `LHA-Q-0120` |
| 48 | 1730 | O形密封圈新旧标示、注意事项 | `LHA-Q-0123`、`LHA-Q-0192` |
| 49 | 1257 | 控制阀总览 | `LHA-Q-0051` |
| 50 | 1258 | BZL、直装控制阀对应表 | `LHA-Q-0043`、`LHA-Q-0131` |
| 51 | 1259 | BZL、BZL规格表 | `LHA-Q-0042`、`LHA-Q-0126` |
| 54 | 1262 | BZL外形尺寸表 | `LHA-Q-0129` |
| 55 | 1265 | BZX、BZX规格表 | `LHA-Q-0050`、`LHA-Q-0133` |
| 56 | 1266 | BZX外形尺寸表 | `LHA-Q-0136` |
| 57 | 1267 | JZG规格表 | `LHA-Q-0139` |
| 58 | 1268 | JZG外形尺寸表 | `LHA-Q-0142` |
| 59 | 1269 | BZS、BZS规格表、注意事项 | `LHA-Q-0049`、`LHA-Q-0145`、`LHA-Q-0191` |
| 61 | 1271 | BZS外形尺寸表 | `LHA-Q-0148` |
| 62 | 1272 | BZS | `LHA-Q-0044`-`LHA-Q-0045`、`LHA-Q-0047`-`LHA-Q-0048` |
| 63 | 1697 | 板式安装座 | `LHA-Q-0040` |
| 64 | 1698 | 板式安装座适用型号表、注意事项 | `LHA-Q-0156`-`LHA-Q-0158`、`LHA-Q-0193` |
| 65 | 1699 | 板式安装座 | `LHA-Q-0038`-`LHA-Q-0039`、`LHA-Q-0041` |
| 66 | 1700 | LZ-MP尺寸重量表、LZ-MS尺寸重量表 | `LHA-Q-0151`、`LHA-Q-0154` |

## 3. Question Statistics

- Total: 127
- Direct LHA: 72
- Accessory / Related Product: 35
- Document Common: 20
- FACT: 24
- SPEC_LOOKUP: 1
- MODEL: 7
- TABLE: 43
- CALCULATION: 12
- CHART: 3
- PROCEDURE: 6
- CAUTION: 31

## 4. Questions

## LHA-Q-0001

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: A

### Question

LHA快换压板A型更换压板时需要拆装几根螺栓？

### Standard Answer

只需1根螺栓。

### Scoring Standard

- P1 [100]: 只需1根螺栓

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 503
- Section: LHA产品说明
- Local scope path: LHA产品说明 > 压板更换
- Evidence type: TEXT
- Evidence: LHA快换压板A型页面标注：压板更换仅需1根螺栓。

## LHA-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA采用什么措施防止冷却液侵入？

### Standard Answer

采用专用密封设计提高密封性，并使用耐腐蚀防尘材料；即使使用氯系冷却液也能保持较高耐久性。

### Scoring Standard

- P1 [34]: 采用专用密封设计
- P2 [33]: 使用耐腐蚀防尘材料
- P3 [33]: 使用氯系冷却液时仍具耐久性

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 504
- Section: LHA产品说明
- Local scope path: LHA产品说明 > 密封
- Evidence type: TEXT
- Evidence: 采用高性能的耐腐蚀防尘材料，即使使用氯系冷却液也能保证其高耐久性。 | 并且扩大了活塞杆直径，有效抑制了扭矩，还通过大钢球、旋转槽形状的 | 采用专用的密封设计，能防止高压冷却液侵入，实现了高密封性。 | 钢球挡环部位 | 优异的防冷却液侵入结构 | 优异的防冷却液侵入结构 | 的阻力降至极限。

## LHA-Q-0003

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA的钢球挡环旋转结构如何提高旋转性能和耐久性？

### Standard Answer

挡环随活塞杆与钢球一起旋转，将旋转阻力降到较低水平；同时通过扩大活塞杆直径、大钢球和优化旋转槽形状提高耐久性。

### Scoring Standard

- P1 [17]: 挡环随活塞杆旋转
- P2 [17]: 挡环随钢球旋转
- P3 [17]: 旋转阻力降低
- P4 [17]: 扩大活塞杆直径
- P5 [16]: 采用大钢球
- P6 [16]: 优化旋转槽形状

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 503
- Section: LHA产品说明
- Local scope path: LHA产品说明 > 旋转机构
- Evidence type: DRAWING
- Evidence: 钢球挡环随活塞杆与钢球一起旋转，将旋转阻力降至极限；扩大活塞杆直径，并采用大钢球和优化的旋转槽形状以提高耐久性。

## LHA-Q-0004

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA为什么能够使用加长型旋转压板？

### Standard Answer

本体上部和活塞杆端采用长导向比设计，能够强有力地支撑活塞杆，因此可对应加长型旋转压板。

### Scoring Standard

- P1 [34]: 本体上部采用长导向比
- P2 [33]: 活塞杆端采用长导向比
- P3 [33]: 可支撑加长型旋转压板

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 504
- Section: LHA产品说明
- Local scope path: LHA产品说明 > 长导向
- Evidence type: DRAWING
- Evidence: 并且扩大了活塞杆直径，有效抑制了扭矩，还通过大钢球、旋转槽形状的 | 采用高性能的耐腐蚀防尘材料，即使使用氯系冷却液也能保证其高耐久性。 | 采用专用的密封设计，能防止高压冷却液侵入，实现了高密封性。 | 所以可对应加长型旋转压板。 | 通过长导向比设计(本体上部和活塞杆端)强有力地支持了活塞杆， | 紧凑型夹紧器 | 钢球挡环部位

## LHA-Q-0005

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK 油压旋转式夹紧器系列（LHA 资料内附件或关联产品）
- Model / Scope: 油压旋转式夹紧器系列 系列

### Question

PDF列出的油压旋转式夹紧器典型使用工序有哪些？

### Standard Answer

包括机加工、压装或铆接、清洗、去毛刺，以及需要较高重复夹紧位置精度的工序。

### Scoring Standard

- P1 [20]: 包括机加工
- P2 [20]: 包括压装或铆接
- P3 [20]: 包括清洗
- P4 [20]: 包括去毛刺
- P5 [20]: 包括需要较高重复夹紧位置精度的工序

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 1
- Printed page: 499
- Section: 产品总览
- Local scope path: 产品总览 > 使用范例
- Evidence type: DRAWING
- Evidence: 用于需要重复夹紧位置精度高的工序 | 用于去毛刺 | 用于清洗工序 | 用于机加工工序

## LHA-Q-0006

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA旋转式夹紧器从释放到夹紧依次经历哪些动作？

### Standard Answer

从释放状态开始，压板边下降边旋转；旋转结束后开始垂直下降；最终到达夹紧状态。

### Scoring Standard

- P1 [34]: 从释放状态开始，压板边下降边旋转
- P2 [33]: 旋转结束后开始垂直下降
- P3 [33]: 最终到达夹紧状态

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 1
- Printed page: 499
- Section: 产品总览
- Local scope path: 产品总览 > 动作原理
- Evidence type: DRAWING
- Evidence: 边下降边旋转动作 | (LHS型不下降，实施水平 | 垂直下降 | 旋转结束后开始 | 动作原理 | 动作结束 | (释放状态) | (夹紧状态)

## LHA-Q-0007

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA油压旋转式夹紧器的总体特点是什么？

### Standard Answer

采用强韧的旋转机构，强调高刚性、长寿命、高精度，并具有快速动作能力。

### Scoring Standard

- P1 [20]: 采用强韧的旋转机构
- P2 [20]: 具有高刚性
- P3 [20]: 具有长寿命
- P4 [20]: 具有高精度
- P5 [20]: 具有快速动作能力

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 1
- Printed page: 499
- Section: 产品总览
- Local scope path: 产品总览 > 特点
- Evidence type: TEXT
- Evidence: 强韧的旋转机构。高刚性、长寿命、高精度、快速动作。

## LHA-Q-0009

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: M/N

### Question

供给LHA动作确认空气传感器的气压应设定为多少？

### Standard Answer

答案为：0.2 MPa。

### Scoring Standard

- P1 [100]: 正确给出：0.2 MPa

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 531
- Section: 空气传感器
- Local scope path: 空气传感器 > 供气
- Evidence type: TABLE
- Evidence: 确认活塞杆的动作需要设置空气传感器。 推荐使用空气压力：0.2MPa 推荐空气传感器 名称 空气传感器 间隙开关 供给空气传感器的气压请设定为0.2MPa。

## LHA-Q-0010

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: M/N

### Question

使用LHA-M/N进行动作确认时，空气传感器应连接到哪些确认口？

### Standard Answer

应连接到夹紧确认用口和释放确认用口，以确认活塞杆的夹紧与释放动作。

### Scoring Standard

- P1 [34]: 连接夹紧确认用口
- P2 [33]: 连接释放确认用口
- P3 [33]: 用于确认活塞杆夹紧与释放动作

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 531
- Section: 空气传感器
- Local scope path: 空气传感器 > 动作确认
- Evidence type: TEXT + PROCEDURE
- Evidence: 空气传感器连接型 （动作确认方式･･･M：空气传感器板式连接型 / N：空气传感器外配管型） | 将空气传感器连接在夹紧确认用口、释放确认用 | 口上，检测两者的差压，从而确认活塞杆的动作。 | 油压复动旋转式夹紧器 空气传感器连接型 | 确认活塞杆的动作需要设置空气传感器。 | ● M:空气传感器板式连接型时、请在气传感器O形密封圈部 | model LHA-M / LHA-N

## LHA-Q-0011

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: M/N

### Question

LHA空气传感器的排气口应如何设置，原因是什么？

### Standard Answer

排气口必须向大气开放，并防止冷却液和切屑侵入；排气口堵塞会导致空气传感器检测异常或误动作。

### Scoring Standard

- P1 [25]: 排气口向大气开放
- P2 [25]: 防止冷却液侵入排气口
- P3 [25]: 防止切屑侵入排气口
- P4 [25]: 排气口堵塞会造成传感器误动作

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 531
- Section: 空气传感器
- Local scope path: 空气传感器 > 排气口
- Evidence type: TEXT
- Evidence: ● 排气口必须向大气排放，并防止冷却液、切 ● M:空气传感器板式连接型时、请在气传感器O形密封圈部 全行程 mm 13.5 14.5 15.5 18.5 20 24 26 32 屑粉尘等侵入。排气口一旦堵塞，空气传感 涂布适量的甘油。 旋转行程 mm 5.5 6.5 7.5 8.5 10 12 14 16 导致空气传感器出现误动作。

## LHA-Q-0012

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: M/N

### Question

为保证稳定检测，每台空气传感器连接的LHA夹紧器数量应限制为多少？

### Standard Answer

4台以下。

### Scoring Standard

- P1 [100]: 4台以下

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 531
- Section: 空气传感器
- Local scope path: 空气传感器 > 连接数量
- Evidence type: TEXT
- Evidence: 1台空气传感器连接的夹紧器数量请控制在4台以下。

## LHA-Q-0013

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: M/N

### Question

LHA-M与LHA-N的空气传感器连接方式有什么区别？

### Standard Answer

M为空气传感器板式连接型；N为空气传感器外配管型。

### Scoring Standard

- P1 [50]: M为空气传感器板式连接型
- P2 [50]: N为空气传感器外配管型

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 531
- Section: 空气传感器
- Local scope path: 空气传感器 > 连接方式
- Evidence type: TABLE
- Evidence: 油压复动旋转式夹紧器 空气传感器连接型 model LHA-M / LHA-N 旋转夹紧器 剖面结构 规格 能力曲线图 外形尺寸 空气传感器 压板设计尺寸 附件 P.745 空气传感器连接型 （动作确认方式･･･M：空气传感器板式连接型 / N：空气传感器外配管型） 空气传感流程图 将空气传感器连接在夹紧确认用口、释放确认用 关于空气传感器

## LHA-Q-0014

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: A

### Question

LHA快换压板A型通过什么结构降低压板紧固操作量？

### Standard Answer

采用楔形结构，以较小力矩紧固压板；更换时只需操作1根螺栓，且无需固定活塞杆。

### Scoring Standard

- P1 [25]: 采用楔形结构
- P2 [25]: 可用较小力矩紧固压板
- P3 [25]: 更换时只需操作1根螺栓
- P4 [25]: 不需要固定活塞杆

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 503
- Section: 压板设计
- Local scope path: 压板设计 > 快换A型
- Evidence type: DRAWING
- Evidence: LHA快换压板A型采用楔形结构，以小力矩实现压板紧固；压板更换仅需1根螺栓，且因紧固力矩小而不需要固定活塞杆。

## LHA-Q-0015

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA标准锥形夹紧压板如何便于自制压板和调整相位？

### Standard Answer

锥套为标准配置，并设有压板定位专用槽，便于自制旋转压板及调整压板相位。

### Scoring Standard

- P1 [25]: 锥套是标准配置
- P2 [25]: 设有压板定位专用槽
- P3 [25]: 便于自制旋转压板
- P4 [25]: 便于调整压板相位

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 503
- Section: 压板设计
- Local scope path: 压板设计 > 锥形压板
- Evidence type: DRAWING
- Evidence: LHA锥套为标准配置，便于用户自制旋转压板；压板定位专用槽用于调整压板相位。

## LHA-Q-0017

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

解释LHA夹紧力曲线时，为什么不能只用夹紧器内径和活塞杆直径计算夹紧力？

### Standard Answer

PDF明确说明夹紧力不可由夹紧器内径与活塞杆径直接算出，应使用夹紧力曲线或规定公式；夹紧力还随供给油压和压板长度变化。

### Scoring Standard

- P1 [34]: 夹紧力不可由内径和活塞杆径直接算出
- P2 [33]: 应使用夹紧力曲线或规定公式
- P3 [33]: 夹紧力随供给油压和压板长度变化

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 506
- Section: 能力曲线
- Local scope path: 能力曲线 > 夹紧力曲线
- Evidence type: TEXT
- Evidence: 无符号： 无(标准：锥形夹紧压板型) 无符号 A F 最高使用压力 MPa 7 Q□ ： 行程加长型 注意事项 ※1. 夹紧力不可从夹紧器内径与活塞杆径算出。请参照夹紧力曲线图。 (□内是夹紧行程值(请参照外形尺寸图)) P Q□ Y□ ※2. F , F1 , F2： 夹紧力(kN)、P： 供给油压(MPa)、L , L1 ,L2： 活塞中心至夹紧点的距离(mm)、L3： (mm)

## LHA-Q-0018

**Type: FACT**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0480

### Question

根据PDF示例，LHA0480在供给油压5.0 MPa、压板长度50 mm时的夹紧力约为多少？

### Standard Answer

约3.1 kN。

### Scoring Standard

- P1 [100]: 约3.1 kN

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 507
- Section: 能力曲线
- Local scope path: 能力曲线 > 夹紧力曲线
- Evidence type: TEXT
- Evidence: 夹紧力曲线图 ※ LHA□0-□□□-P：双压臂型时不符合本图表的能力曲线。请通过计算公式另行计算。 L： 压板长度 (mm) C R D A 1. 本图表及曲线图表示夹紧力(kN)与供给油压(MPa)之间的关系。 P： 供给油压 (MPa) (例) 使用LHA0480时 7. 本图表中数据是参考值，详细数据请根据各夹紧力计算公式求取。 供给油压为5.0MPa、压板长度L=50mm时, 夹紧力约为3.1kN。 ※1. 在夹紧力计算公式中，F： 夹紧力(kN)、P： 供给油压(MPa)、L： 压板长度(mm)。 (MPa) (kN) 压板长度 L (mm) (L) 2 L=50(s=30) (MPa) (kN) 压板长度 L (mm) (L) 旋转式夹紧器

## LHA-Q-0019

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA旋转动作时间过短可能造成什么后果？

### Standard Answer

可能导致重复停止精度恶化，并可能损伤内部零部件。

### Scoring Standard

- P1 [50]: 动作时间过短会使重复停止精度恶化
- P2 [50]: 动作时间过短可能损伤内部零部件

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 11
- Printed page: 509
- Section: 能力曲线
- Local scope path: 能力曲线 > 容许动作时间
- Evidence type: TEXT
- Evidence: 1. LHA□-Q：行程加长型时的全部动作时间与图表并不一致，请另行根据计算公式求取。(90°旋转时间如图表所示。) 2. 本图表示夹紧器活塞杆在等速运动时，与压板惯性矩相对应的容许动作时间。 5. 如果旋转动作时间过短，可能会导致停止精度恶化以及内部零部件损伤等事故。

## LHA-Q-0021

**Type: FACT**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0480

### Question

PDF示例中，LHA0480在压板惯性矩0.0068 kg·m²时，夹紧全部动作容许时间至少约为多少？

### Standard Answer

夹紧全部动作容许时间约0.9秒以上。

### Scoring Standard

- P1 [100]: 夹紧全部动作容许时间约0.9秒以上

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 510
- Section: 能力曲线
- Local scope path: 能力曲线 > 容许动作时间
- Evidence type: TEXT
- Evidence: LHA0480 (旋转行程) 全部动作时间 (例) 使用LHA0480时， 0.016 伤等故障。 ③夹紧时全部动作容许时间 ： 约0.9秒以上 ④释放时全部动作容许时间 ： 约0.45秒以上 0.004 1．本图的全部动作容许时间表示全行程动作时的容许动作时间。 ②

## LHA-Q-0022

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA主体尺寸代码包含哪些规格？

### Standard Answer

答案为：036、040、048、055、065、075、090、105。

### Scoring Standard

- P1 [13]: 正确给出：036
- P2 [13]: 正确给出：040
- P3 [13]: 正确给出：048
- P4 [13]: 正确给出：055
- P5 [12]: 正确给出：065
- P6 [12]: 正确给出：075
- P7 [12]: 正确给出：090
- P8 [12]: 正确给出：105

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 505
- Section: 型号表示
- Local scope path: 型号表示 > 主体尺寸
- Evidence type: TEXT
- Evidence: 主体尺寸：036、040、048、055、065、075、090、105。

## LHA-Q-0024

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: D/M/N

### Question

LHA动作确认代码无符号、D、M、N分别表示什么？

### Standard Answer

无符号表示无动作确认的标准型；D为双出杆型；M为空气传感器板式连接型；N为空气传感器外配管型。

### Scoring Standard

- P1 [25]: 无符号表示无动作确认的标准型
- P2 [25]: D表示双出杆型
- P3 [25]: M表示空气传感器板式连接型
- P4 [25]: N表示空气传感器外配管型

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 505
- Section: 型号表示
- Local scope path: 型号表示 > 动作确认
- Evidence type: MODEL + TABLE
- Evidence: 动作确认方式：无符号为无动作确认（标准），D为双出杆型，M为空气传感器板式连接型，N为空气传感器外配管型。

## LHA-Q-0026

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0480-CR

### Question

请解释型号LHA0480-CR中主体尺寸代码048、配管代码C和旋转方向代码R的含义。

### Standard Answer

048表示主体外径φ48 mm；C表示板式连接型并附带G螺纹堵头；R表示夹紧时顺时针旋转。

### Scoring Standard

- P1 [25]: 048表示主体外径φ48 mm
- P2 [25]: C表示板式连接型
- P3 [25]: C型附带G螺纹堵头
- P4 [25]: R表示夹紧时顺时针旋转

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 505
- Section: 型号表示
- Local scope path: 型号表示 > 完整编码
- Evidence type: MODEL + TABLE
- Evidence: 048表示主体外径φ48 mm；C表示板式连接型（附带G螺纹堵头）；R表示夹紧时顺时针旋转。

## LHA-Q-0027

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

需要主体外径φ48 mm、设计编号0、板式连接、夹紧时逆时针旋转、无动作确认且无选配件的LHA，应组成什么型号？

### Standard Answer

答案为：LHA0480-CL。

### Scoring Standard

- P1 [100]: 正确给出：LHA0480-CL

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 505
- Section: 型号表示
- Local scope path: 型号表示 > 完整编码
- Evidence type: MODEL + TABLE
- Evidence: 型号表示依次为LHA、主体尺寸048、设计编号0、配管方式C、夹紧时旋转方向L；无动作确认代码和选配代码时组成LHA0480-CL。

## LHA-Q-0028

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

能否仅依据型号表认定LHA动作确认方式与任意选配件都可以组合？

### Standard Answer

不能。PDF明确要求动作确认方式与选配件组合使用时另行垂询确认。

### Scoring Standard

- P1 [100]: 不能。PDF明确要求动作确认方式与选配件组合使用时另行垂询确认

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 505
- Section: 型号表示
- Local scope path: 型号表示 > 选配件
- Evidence type: MODEL + TABLE
- Evidence: ※ 动作确认方式与选配件组合使用时，敬请垂询。 ※ Y0型请另行参照 “LHA-Y0” 的网页·综合样本。 F F1 F2

## LHA-Q-0029

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: A/F/P

### Question

LHA选配代码A、F、P分别表示什么？

### Standard Answer

A为快换压板A型，F为快换压板F型，P为双压臂型。

### Scoring Standard

- P1 [34]: A表示快换压板A型
- P2 [33]: F表示快换压板F型
- P3 [33]: P表示双压臂型

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 505
- Section: 型号表示
- Local scope path: 型号表示 > 选配件
- Evidence type: MODEL + TABLE
- Evidence: 型号表示的选配代码：A为快换压板A型，F为快换压板F型，P为双压臂型。

## LHA-Q-0030

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: Q/Y

### Question

LHA选配代码Q后的数字和Y30、Y45、Y60分别表示什么？

### Standard Answer

Q后的数字表示夹紧行程值；Y30、Y45、Y60分别表示30°、45°、60°特殊旋转角度。

### Scoring Standard

- P1 [25]: Q后的数字表示夹紧行程值。
- P2 [25]: Y30表示30°特殊旋转角度。
- P3 [25]: Y45表示45°特殊旋转角度。
- P4 [25]: Y60表示60°特殊旋转角度。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 505
- Section: 型号表示
- Local scope path: 型号表示 > 选配件
- Evidence type: MODEL + TABLE
- Evidence: 型号表示的选配代码：Q后数字为夹紧行程值；Y30、Y45、Y60分别表示30°、45°、60°特殊旋转角度。

## LHA-Q-0031

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: C/S

### Question

LHA型号中的配管方式C和S有什么区别？

### Standard Answer

C为板式连接型并附带G螺纹堵头；S为外配管型，使用Rc螺纹。

### Scoring Standard

- P1 [25]: C表示板式连接型
- P2 [25]: C型附带G螺纹堵头
- P3 [25]: S表示外配管型
- P4 [25]: S型使用Rc螺纹

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 505
- Section: 型号表示
- Local scope path: 型号表示 > 配管方式
- Evidence type: TABLE
- Evidence: 请参照第1257页。 | 1 2 3 4 5 6 | C ： 板式连接型 (附带G螺纹堵头) | 3 配管方式 | 附带G螺纹堵头 | 036 ： φD=36mm | 075 ： φD=75mm | 2 设计编号

## LHA-Q-0032

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA-A使用偏心压板时，夹紧点范围有什么限制？

### Standard Answer

夹紧点必须位于以压板紧固部为基准的90°范围内。

### Scoring Standard

- P1 [100]: 夹紧点必须位于以压板紧固部为基准的90°范围内

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 745
- Section: LHA专项注意事项
- Local scope path: LHA专项注意事项 > 偏心压板
- Evidence type: TEXT
- Evidence: LLV 7) -A (快换压板A型)型夹紧器上使用偏心压板时 LLW ● 请保证夹紧点在以压板紧固部为基准的90°范围内。 直线夹紧器/ 夹紧点范围 TLA-1 TLA1602-1 / TLV1600-2 M8 25 LHA0480-A / LHC0480-A TLA2002-1 / TLV2000-2 LHA-A LHV0480-A / LHW0481-A 压板紧固部位

## LHA-Q-0033

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

安装LHA旋转压板前为什么必须清洁压板、锥套和活塞杆连接部？

### Standard Answer

连接部的油污或异物可能导致压板松动，因此必须充分脱脂、清洗。

### Scoring Standard

- P1 [34]: 油污或异物可能导致压板松动
- P2 [33]: 安装前应脱脂
- P3 [33]: 安装前应清洗

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 40
- Printed page: 746
- Section: LHA专项注意事项
- Local scope path: LHA专项注意事项 > 压板安装清洁
- Evidence type: TEXT
- Evidence: M30×1.5 175 〜 210 | M39×1.5 280 〜 335 | M22×1.5 93 〜 112 | M36×1.5 235 〜 282 | 93 〜 112 | ● 如果压板、锥套、活塞杆的连接部位沾有油污或异物，就可能会 | 导致压板松动。应充分进行脱脂、清洗，去除油污或异物。

## LHA-Q-0034

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

设计油压回路时应遵循什么要求？

### Standard Answer

必须设计适当的油压回路；错误回路可能导致机械设备误动作、破损等事故。

### Scoring Standard

- P1 [34]: 应设计适当油压回路
- P2 [33]: 错误回路可能导致误动作
- P3 [33]: 错误回路可能导致设备破损

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 745
- Section: LHA专项注意事项
- Local scope path: LHA专项注意事项 > 回路设计
- Evidence type: TEXT
- Evidence: ● 在设计油压回路时，请认真阅读“夹紧器的速度控制回路和注意事项”， ● 安装本体时应用足所有的安装螺栓孔，并按下表所示力矩紧固 | 设计适当的油压回路。回路设计错误会导致机械设备误动作、破损等 | ● 必须参照液压油一览表(第1725页)，选用适当的液压油。 | ● 惯性力矩过大会导致压板的停止精度恶化，以及油压旋转夹紧器破损等 | 内六角螺栓(强度等级12.9)。 | 故障。另外，有时会因供给油压或压板安装姿势导致夹紧器无法旋转。 | 2) 回路设计时的注意事项

## LHA-Q-0035

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

LHA旋转压板惯性力矩过大可能造成什么后果？

### Standard Answer

会使压板停止精度恶化，可能损坏旋转夹紧器；还可能因供给油压或安装姿势而无法旋转。

### Scoring Standard

- P1 [25]: 惯性力矩过大会使停止精度恶化
- P2 [25]: 惯性力矩过大可能损坏旋转夹紧器
- P3 [25]: 供给油压不当可能导致无法旋转
- P4 [25]: 压板安装姿势不当可能导致无法旋转

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 745
- Section: LHA专项注意事项
- Local scope path: LHA专项注意事项 > 惯性力矩
- Evidence type: TEXT
- Evidence: ● 在设计油压回路时，请认真阅读“夹紧器的速度控制回路和注意事项”， ● 安装本体时应用足所有的安装螺栓孔，并按下表所示力矩紧固 | ● 惯性力矩过大会导致压板的停止精度恶化，以及油压旋转夹紧器破损等 | 故障。另外，有时会因供给油压或压板安装姿势导致夹紧器无法旋转。 | 3) 请降低旋转压板的惯性力矩。 | 2) 回路设计时的注意事项 | model LHA/LHC/LHD/LHS/LHV/LHW/LG/LT/LGV/TLA-2/TLB-2/TLA-1/TLV-2 | ● 必须参照液压油一览表(第1725页)，选用适当的液压油。

## LHA-Q-0036

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

设备安装后的磨合期应重点检查什么？

### Standard Answer

螺栓和压板安装螺母可能松动，应适时检查并重新紧固。

### Scoring Standard

- P1 [34]: 磨合期螺栓可能松动
- P2 [33]: 磨合期压板安装螺母可能松动
- P3 [33]: 应适时检查并加固

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 42
- Printed page: 748
- Section: LHA专项注意事项
- Local scope path: LHA专项注意事项 > 磨合检查
- Evidence type: TEXT
- Evidence: 活塞前端后，然后安装探头。螺纹零部件的夹紧力矩如下图所示。 | ● 设备安装后的磨合期里，螺栓、压板安装螺母会发生松动。请适时 | 如夹紧动作特别快，就会加剧各部位的磨耗和损伤， | 进行松动检查和加固作业。 | TLV-2 | TLA-2 | TLB-2

## LHA-Q-0037

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

调整LHA动作速度时应按什么方向逐步调整，动作过快会有什么后果？

### Standard Answer

应从低速、小流量侧逐渐调向高速、大流量侧；动作过快会加剧磨耗、造成损伤并导致故障。

### Scoring Standard

- P1 [20]: 从低速小流量侧开始调整
- P2 [20]: 逐渐向高速大流量侧调整
- P3 [20]: 动作过快会加剧磨耗
- P4 [20]: 动作过快会造成损伤
- P5 [20]: 动作过快会导致故障

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 42
- Printed page: 748
- Section: LHA专项注意事项
- Local scope path: LHA专项注意事项 > 速度调整
- Evidence type: TEXT
- Evidence: 调整速度时，将速度控制阀从低速侧（小流量）慢慢向高速侧（大流量）调整；夹紧动作特别快会加剧各部位磨耗和损伤并导致故障。

## LHA-Q-0038

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LZY-MD（LHA 资料内附件或关联产品）
- Model / Scope: LZY-MD 系列

### Question

LZY-MD板式安装座的表面处理是什么？

### Standard Answer

黑色酸化皮膜。

### Scoring Standard

- P1 [100]: 黑色酸化皮膜

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 65
- Printed page: 1699
- Section: 板式安装座
- Local scope path: 板式安装座 > LZY-MD
- Evidence type: TEXT
- Evidence: 材质：S45C 表面处理：黑色酸化皮膜

## LHA-Q-0039

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK WHZ-MD（LHA 资料内附件或关联产品）
- Model / Scope: WHZ-MD 系列

### Question

WHZ-MD板式安装座的表面处理是什么？

### Standard Answer

锆石处理（氧化锆处理）。

### Scoring Standard

- P1 [100]: 锆石处理（氧化锆处理）

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 65
- Printed page: 1699
- Section: 板式安装座
- Local scope path: 板式安装座 > WHZ-MD
- Evidence type: TEXT
- Evidence: 注意事项 1. 材质：A2017BE-T4 表面处理：锆石处理(氧化锆处理) DZ-M 2. 本产品未附带安装螺栓。请用户根据安装高度并参照A尺寸自行配备。 3. 所需板式安装座的厚度(A尺寸)与上记厚度不同时，请在使用前对Z面进行补充加工。或参考本图自行制作。 外配管式安装座 螺母 板式安装座

## LHA-Q-0040

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK 板式安装座（LHA 资料内附件或关联产品）
- Model / Scope: 板式安装座 :: 多系列

### Question

PDF中的板式安装座主要用于什么？

### Standard Answer

用于调整夹紧器的安装高度。

### Scoring Standard

- P1 [100]: 用于调整夹紧器的安装高度

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 63
- Printed page: 1697
- Section: 板式安装座
- Local scope path: 板式安装座 > 用途
- Evidence type: TEXT
- Evidence: 用板式安装座调整夹紧器的安装高度。 | Model TMZ-2MB | 板式安装座 | 板式安装座 | 板式安装座 | 板式安装座

## LHA-Q-0041

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK 板式安装座（LHA 资料内附件或关联产品）
- Model / Scope: 板式安装座 :: 多系列

### Question

所需板式安装座厚度与PDF标准尺寸不同时应如何处理？

### Standard Answer

应在使用前对图示Z面进行追加加工，或参考PDF图纸自行制作；安装螺栓需由用户根据安装高度自行配备。

### Scoring Standard

- P1 [34]: 可对图示Z面追加加工
- P2 [33]: 可参考图纸自行制作
- P3 [33]: 安装螺栓由用户按安装高度配备

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 65
- Printed page: 1699
- Section: 板式安装座
- Local scope path: 板式安装座 > 追加加工
- Evidence type: TEXT + PROCEDURE
- Evidence: 注意事项 1. 材质：A2017BE-T4 表面处理：锆石处理(氧化锆处理) DZ-M 2. 本产品未附带安装螺栓。请用户根据安装高度并参照A尺寸自行配备。 3. 所需板式安装座的厚度(A尺寸)与上记厚度不同时，请在使用前对Z面进行补充加工。或参考本图自行制作。 外配管式安装座 螺母 板式安装座

## LHA-Q-0042

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZL（LHA 资料内附件或关联产品）
- Model / Scope: BZL :: 低压

### Question

为什么安装BZL速度控制阀时必须使用本体推荐的紧固力矩？

### Standard Answer

BZL端面采用金属密封结构，紧固力矩不足会导致无法正常进行流量调整。

### Scoring Standard

- P1 [50]: BZL端面采用金属密封
- P2 [50]: 紧固力矩不足会导致无法正常调整流量

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 51
- Printed page: 1259
- Section: BZL
- Local scope path: BZL > 安装注意
- Evidence type: TEXT
- Evidence: 注意事项 1. 必须按本体推荐紧固力矩安装速度控制阀。速度控制阀端面为金属密封结构，紧固力矩不足将无法进行流量调整。 | BZL0101-A BZL0201-A BZL0301-A BZL0101-B BZL0201-B BZL0301-B | 否则可能会因夹紧器的G螺纹底面深度差异而导致金属密封不严密，从而无法进行流量调整。 | 2. 不准将曾经使用过的BZL (速度控制阀)再用于其他夹紧器上。 | 10.2 | (DBA0250-C□) (DBC0250-C□) (FVA0401) (FVC0630) (FVD1600) LC0263-C□-□ LCW0363-C□ | DBA0250-C□ DBC0250-C□ FVA0401 FVC0630 FVD1600

## LHA-Q-0043

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZL（LHA 资料内附件或关联产品）
- Model / Scope: BZL :: 低压

### Question

BZL低压速度控制阀除流量调整外，还可以怎样进行回路排气？

### Standard Answer

旋松速度控制阀本体即可排除回路中的空气。

### Scoring Standard

- P1 [100]: 旋松速度控制阀本体即可排除回路中的空气

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 50
- Printed page: 1258
- Section: BZL
- Local scope path: BZL > 用途
- Evidence type: TEXT
- Evidence: 旋松速度控制阀本体，即可排除回路中的空气。 | 旋松Ｇ螺纹堵头本体，即可排除回路中的空气。 | 通过操作扳手，即可排除回路中的空气。 | 35MPa以下 | 35MPa以下 | 35MPa以下 | 35MPa以下 | 35MPa以下

## LHA-Q-0044

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZS（LHA 资料内附件或关联产品）
- Model / Scope: BZS 系列

### Question

BZS顺序阀出厂时是否已设定压力，现场设定结束后还需要做什么？

### Standard Answer

出厂时压力未设定；现场应根据需要用压力表确认，设定结束后至少紧固一侧旋转防止套件。

### Scoring Standard

- P1 [34]: 出厂时压力未设定
- P2 [33]: 现场用压力表确认设定
- P3 [33]: 设定后至少紧固一侧旋转防止套件

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 62
- Printed page: 1272
- Section: BZS
- Local scope path: BZS > 压力设定
- Evidence type: TEXT + PROCEDURE
- Evidence: 4. 设定压力和实际供给压力的压差应在1MPa以上。 手动设备 5. 使用多台顺序阀(BZS)进行顺序动作时，请在各顺序阀间设置1MPa以上的压差。 附件 6. 需要使复数台夹紧器的动作一致时，请边确认夹紧器的动作边进行顺序阀的微调整。 注意事项・其他 10. 发货时，顺序阀压力处于未设定状态，请参照下图进行设定。另外，请根据实际需要在回路内设置压力表来确定压力。压力设定结束后， 请至少紧固一侧旋转防止套件。 (紧固力矩：0.2Ｎ・m)

## LHA-Q-0045

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZS（LHA 资料内附件或关联产品）
- Model / Scope: BZS :: 多台

### Question

使用多台BZS顺序阀时，各顺序阀之间至少应设置多大压差？

### Standard Answer

1 MPa以上。

### Scoring Standard

- P1 [100]: 1 MPa以上

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 62
- Printed page: 1272
- Section: BZS
- Local scope path: BZS > 压差
- Evidence type: TABLE
- Evidence: 2. 内部未设置过滤网。如果切屑和密封胶带碎屑等异物混入内部，可能会导致顺序阀不能进行正常动作。内部零部件受损时， 请务必考虑回路的流量控制。(由于BZS是直接安装在夹紧器上的单台专用顺序阀，所以更容易受供给油量的影响。) 液压单元 4. 设定压力和实际供给压力的压差应在1MPa以上。 手动设备 5. 使用多台顺序阀(BZS)进行顺序动作时，请在各顺序阀间设置1MPa以上的压差。 附件 10. 发货时，顺序阀压力处于未设定状态，请参照下图进行设定。另外，请根据实际需要在回路内设置压力表来确定压力。压力设定结束后，

## LHA-Q-0047

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZS（LHA 资料内附件或关联产品）
- Model / Scope: BZS 系列

### Question

BZS内部是否设置过滤网，异物进入可能造成什么后果？

### Standard Answer

BZS内部没有过滤网；切屑、密封胶带碎屑等异物进入可能使顺序阀无法正常动作，内部件受损后即使清除异物也可能无法恢复。

### Scoring Standard

- P1 [25]: BZS内部没有过滤网
- P2 [25]: 异物可能使顺序阀无法正常动作
- P3 [25]: 异物可能损坏内部件
- P4 [25]: 内部件受损后清除异物也可能无法恢复

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 62
- Printed page: 1272
- Section: BZS
- Local scope path: BZS > 异物
- Evidence type: TEXT
- Evidence: 直装式顺序阀 model BZS 全般 P.1257 型号表示 规格 对应机器型号 外形尺寸 附件 2. 内部未设置过滤网。如果切屑和密封胶带碎屑等异物混入内部，可能会导致顺序阀不能进行正常动作。内部零部件受损时， 即使清除异物后也有可能不能正常使用。 液压系列 请务必考虑回路的流量控制。(由于BZS是直接安装在夹紧器上的单台专用顺序阀，所以更容易受供给油量的影响。) 液压单元 5. 使用多台顺序阀(BZS)进行顺序动作时，请在各顺序阀间设置1MPa以上的压差。 附件

## LHA-Q-0048

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZS（LHA 资料内附件或关联产品）
- Model / Scope: BZS 系列

### Question

安装BZS为什么可能使夹紧器动作时间变长？

### Standard Answer

安装BZS会使夹紧器的最小通路面积变小，因而可能延长动作时间；过大供给流量也可能妨碍正常顺序动作。

### Scoring Standard

- P1 [34]: BZS会使最小通路面积变小
- P2 [33]: 最小通路面积变小可能延长动作时间
- P3 [33]: 过大供给流量可能妨碍顺序动作

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 62
- Printed page: 1272
- Section: BZS
- Local scope path: BZS > 流量影响
- Evidence type: TEXT
- Evidence: 3. 根据构成回路(夹紧器的容量、配管的直径和长度等)的不同，过大的供给油量有可能会导致顺序阀不能进行顺序动作， 请务必考虑回路的流量控制。(由于BZS是直接安装在夹紧器上的单台专用顺序阀，所以更容易受供给油量的影响。) 液压单元 5. 使用多台顺序阀(BZS)进行顺序动作时，请在各顺序阀间设置1MPa以上的压差。 附件 6. 需要使复数台夹紧器的动作一致时，请边确认夹紧器的动作边进行顺序阀的微调整。 注意事项・其他 7. 安装本产品会使夹紧器的最小通路面积变小。可能会导致动作时间变长，请一定注意。

## LHA-Q-0049

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZS（LHA 资料内附件或关联产品）
- Model / Scope: BZS 系列

### Question

BZS直装式顺序阀的主要用途是什么？

### Standard Answer

用于控制多个夹紧器按顺序动作；达到顺序动作设定压力后阀门开启，使后续夹紧器动作。

### Scoring Standard

- P1 [34]: BZS用于控制多个夹紧器顺序动作
- P2 [33]: 达到设定压力后阀门开启
- P3 [33]: 阀门开启后后续夹紧器动作

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 59
- Printed page: 1269
- Section: BZS
- Local scope path: BZS > 用途
- Evidence type: DRAWING
- Evidence: 4. 使用多台顺序阀(BZS)进行顺序动作时，请在各顺序阀间设置1MPa以上的压差。 | 请务必考虑回路的流量控制。(由于BZS是直接安装在夹紧器上的单台专用顺序阀，所以更容易受供给油量的影响。) | 顺序阀用于控制多个夹紧器的顺序动作，能够控制工件的 | 一次侧 (P1 口 ) 的压力到达顺序动作压力设定值时，液压油 | 20 ： 螺纹部 G1/4A | 1 2 | G1/4A

## LHA-Q-0050

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZX（LHA 资料内附件或关联产品）
- Model / Scope: BZX 系列

### Question

使用BZX排气阀时，对压力和堵头旋松量有什么安全要求？

### Standard Answer

必须在低压条件下排气，不能在高压下作业；排气时不得过度旋松堵头。

### Scoring Standard

- P1 [34]: 应在低压条件下排气
- P2 [33]: 不得在高压下排气
- P3 [33]: 不得过度旋松堵头

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 55
- Printed page: 1265
- Section: BZX
- Local scope path: BZX > 排气安全
- Evidence type: TEXT
- Evidence: BZX注意事项：排气作业时不得从完全关闭状态旋松堵头2周以上；高压排气非常危险，必须在相当于回路内机器最低动作压力的低压条件下排气。

## LHA-Q-0051

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK 控制阀（LHA 资料内附件或关联产品）
- Model / Scope: 控制阀 :: 多产品

### Question

PDF中的直装控制阀及相关产品包括哪些类别？

### Standard Answer

包括速度控制阀、排气阀、G螺纹堵头和直装式顺序阀。

### Scoring Standard

- P1 [34]: 包括速度控制阀
- P2 [33]: 包括排气阀
- P3 [33]: 包括G螺纹堵头和直装式顺序阀

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 49
- Printed page: 1257
- Section: 控制阀总览
- Local scope path: 控制阀总览 > 产品类别
- Evidence type: TEXT
- Evidence: 速度控制阀 排气阀 Ｇ螺纹堵头 直装式顺序阀 VFP

## LHA-Q-0055

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0360

### Question

LHA0360夹紧器内径是多少？

### Standard Answer

答案为：26 mm。

### Scoring Standard

- P1 [100]: 正确给出：26 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 506
- Section: LHA规格
- Local scope path: LHA规格 > 小规格
- Evidence type: TABLE
- Evidence: 型号表示 型号 LHA0360 LHA0400 LHA0480 LHA0550 夹紧器内径※1 mm 26 31 37 44

## LHA-Q-0063

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 液压通用注意事项

### Question

液压回路中混入大量空气会有什么影响，应如何处理？

### Standard Answer

大量空气会使动作时间异常变长。排气步骤：1）供油压力调至2 MPa以下；2）将离夹紧器或支撑器最近的配管接头螺母旋松一圈；3）左右摇动配管，使连接部松动并排出混有空气的液压油；4）空气排净后重新紧固接头；5）在回路最高处和最末端附近排气效果更好。

### Scoring Standard

- P1 [15]: 大量空气会使动作时间异常变长
- P2 [15]: 供油压力调至2 MPa以下
- P3 [14]: 将最近的配管接头螺母旋松一圈
- P4 [14]: 摇动配管排出含空气液压油
- P5 [14]: 空气排净后紧固接头
- P6 [14]: 优先在回路最高处排气
- P7 [14]: 优先在回路末端附近排气

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 43
- Printed page: 1725
- Section: 液压通用注意事项
- Local scope path: 液压通用注意事项 > 回路排气
- Evidence type: TEXT + PROCEDURE
- Evidence: 液压回路混入大量空气会使动作时间异常变长。排气时将供油压力调至2 MPa以下，旋松离夹紧器或支撑器最近的管接头螺母一圈，左右摇动配管排出混有空气的液压油，排净后紧固螺母；在回路最上端及最末端附近排气效果更佳。

## LHA-Q-0064

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 液压通用注意事项

### Question

PDF指定的通用液压油粘度等级是什么？

### Standard Answer

相当于ISO VG 32粘度等级的一般液压油。

### Scoring Standard

- P1 [100]: 相当于ISO VG 32粘度等级的一般液压油

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 43
- Printed page: 1725
- Section: 液压通用注意事项
- Local scope path: 液压通用注意事项 > 液压油
- Evidence type: TEXT
- Evidence: ● 安装施工方面的注意事项 (油压系列通用) | ● 务请参照“液压油一览表”，选用适当的液压油。 | ISO 粘度等级ISO-VG-32 | ● 液压油一览表 | 1) | Showa Shell Sekiyu Tellus S2 M 32 Morlina S2 B 32 | Idemitsu Kosan Daphne Hydraulic Fluid 32 Daphne Super Multi Oil 32

## LHA-Q-0065

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 液压通用注意事项

### Question

是否允许擅自分解或改造PDF中的液压产品？

### Standard Answer

不允许擅自分解或改造。

### Scoring Standard

- P1 [50]: 不得擅自分解产品
- P2 [50]: 不得擅自改造产品

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 45
- Printed page: 1727
- Section: 液压通用注意事项
- Local scope path: 液压通用注意事项 > 禁止改造
- Evidence type: TEXT
- Evidence: 请不要擅自对产品进行分解或改造。

## LHA-Q-0066

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 液压通用注意事项

### Question

液压配管施工前为什么必须清洁管路并防止异物进入？

### Standard Answer

切屑、密封材料碎屑等异物会造成阀和夹紧器动作不良或损伤，因此施工前必须清洁并防止异物进入。

### Scoring Standard

- P1 [25]: 切屑可能造成动作不良或损伤
- P2 [25]: 密封材料碎屑可能造成动作不良或损伤
- P3 [25]: 施工前清洁管路
- P4 [25]: 施工时防止异物进入

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 43
- Printed page: 1725
- Section: 液压通用注意事项
- Local scope path: 液压通用注意事项 > 配管清洁
- Evidence type: TEXT
- Evidence: 配管、管接头和夹具油路在连接前必须充分冲洗，防止切屑和密封材料碎屑等异物进入回路。

## LHA-Q-0067

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: C

### Question

LHA哪种配管方式可以直接安装速度控制阀？

### Standard Answer

板式连接型C。

### Scoring Standard

- P1 [100]: 板式连接型C

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号数据
- 不得加入PDF无法支持的关键事实
- 不得混淆产品、型号、适用关系或规格条件。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 505
- Section: LHA附件
- Local scope path: LHA附件 > 速度控制阀
- Evidence type: TEXT
- Evidence: ( Y30：30° / Y45：45° / Y60：60°) | 请参照第1257页。 | 可安装速度控制阀 无板式配管口 | 1 2 3 4 5 6 | 速度控制阀由用户自备 | C ： 板式连接型 (附带G螺纹堵头) | ※ 速度控制阀(BZL)由用户另行购买。

## LHA-Q-0071

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

在LHA标准型外形尺寸表中，LHA0650的A是多少？

### Standard Answer

答案为：156 mm。

### Scoring Standard

- P1 [100]: 正确给出：156 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 14
- Printed page: 512
- Section: 外形尺寸
- Local scope path: 外形尺寸 > A > 外形尺寸及安装部位加工尺寸表
- Evidence type: TABLE
- Evidence: 表名：外形尺寸及安装部位加工尺寸表；行：A；列：LHA0650；原值：156 mm。

## LHA-Q-0074

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

在LHA-D双出杆型外形尺寸表中，LHA0650系列D型的DA是多少？

### Standard Answer

答案为：14 mm。

### Scoring Standard

- P1 [100]: 正确给出：14 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 16
- Printed page: 514
- Section: 外形尺寸
- Local scope path: 外形尺寸 > DA > D型外形尺寸及安装部位加工尺寸表
- Evidence type: TABLE
- Evidence: 表名：D型外形尺寸及安装部位加工尺寸表；行：DA；列：LHA0650；原值：14 mm。

## LHA-Q-0077

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

在LHA-M板式空气传感器型外形尺寸表中，LHA0650系列M型的MB是多少？

### Standard Answer

答案为：40.5 mm。

### Scoring Standard

- P1 [100]: 正确给出：40.5 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 18
- Printed page: 516
- Section: 外形尺寸
- Local scope path: 外形尺寸 > MB > M型外形尺寸及安装部位加工尺寸表
- Evidence type: TABLE
- Evidence: 表名：M型外形尺寸及安装部位加工尺寸表；行：MB；列：LHA0650；原值：40.5 mm。

## LHA-Q-0080

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

在LHA-N外配管空气传感器型外形尺寸表中，LHA0650系列N型的NC是多少？

### Standard Answer

答案为：11 mm。

### Scoring Standard

- P1 [100]: 正确给出：11 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 20
- Printed page: 518
- Section: 外形尺寸
- Local scope path: 外形尺寸 > NC > N型外形尺寸及安装部位加工尺寸表
- Evidence type: TABLE
- Evidence: 表名：N型外形尺寸及安装部位加工尺寸表；行：NC；列：LHA0650；原值：11 mm。

## LHA-Q-0083

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

在LHA-A快换压板型外形尺寸表中，LHA0650系列A型的SA是多少？

### Standard Answer

答案为：40 mm。

### Scoring Standard

- P1 [100]: 正确给出：40 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 22
- Printed page: 520
- Section: 外形尺寸
- Local scope path: 外形尺寸 > SA > A型外形尺寸及安装部位加工尺寸表
- Evidence type: TABLE
- Evidence: 表名：A型外形尺寸及安装部位加工尺寸表；行：SA；列：LHA0650；原值：40 mm。

## LHA-Q-0086

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

在LHA-F快换压板型外形尺寸表中，LHA0650系列F型的FA是多少？

### Standard Answer

答案为：26 mm。

### Scoring Standard

- P1 [100]: 正确给出：26 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 24
- Printed page: 522
- Section: 外形尺寸
- Local scope path: 外形尺寸 > FA > F型外形尺寸及安装部位加工尺寸表
- Evidence type: TABLE
- Evidence: 表名：F型外形尺寸及安装部位加工尺寸表；行：FA；列：LHA0650；原值：26 mm。

## LHA-Q-0089

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

在LHA-P双压臂型外形尺寸表中，LHA0650系列P型的PB是多少？

### Standard Answer

答案为：28 mm。

### Scoring Standard

- P1 [100]: 正确给出：28 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 26
- Printed page: 524
- Section: 外形尺寸
- Local scope path: 外形尺寸 > PB > P型外形尺寸及安装部位加工尺寸表
- Evidence type: TABLE
- Evidence: 表名：P型外形尺寸及安装部位加工尺寸表；行：PB；列：LHA0650；原值：28 mm。

## LHA-Q-0092

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0360

### Question

在LHA-Q行程加长型外形尺寸表中，LHA0360系列选择Q35时的重量是多少？

### Standard Answer

答案为：1.1 kg。

### Scoring Standard

- P1 [100]: 正确给出：1.1 kg

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 30
- Printed page: 528
- Section: 外形尺寸
- Local scope path: 外形尺寸 > 重量 > Q型外形尺寸及安装部位加工尺寸表
- Evidence type: TABLE
- Evidence: 表名：Q型外形尺寸及安装部位加工尺寸表；行：重量；列：LHA0360；原值：1.1 kg。

## LHA-Q-0095

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0480

### Question

在LHA-Y特殊转角型外形尺寸表中，LHA0480系列选择Y45时的旋转行程是多少？

### Standard Answer

答案为：5 mm。

### Scoring Standard

- P1 [100]: 正确给出：5 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 32
- Printed page: 530
- Section: 外形尺寸
- Local scope path: 外形尺寸 > 旋转行程 > Y型外形尺寸及安装部位加工尺寸表
- Evidence type: TABLE
- Evidence: 表名：Y型外形尺寸及安装部位加工尺寸表；行：旋转行程；列：LHA0480；原值：5 mm。

## LHA-Q-0098

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0550-Q

### Question

LHA0550-Q型可选择的夹紧行程范围是多少？

### Standard Answer

答案为：Q15～Q50 mm。

### Scoring Standard

- P1 [100]: 正确给出：Q15～Q50 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 506
- Section: Q型夹紧行程范围
- Local scope path: Q型夹紧行程范围 > LHA0550
- Evidence type: TABLE
- Evidence: 表名：Q型夹紧行程范围；行：夹紧行程；列：LHA0550-Q；原值：Q15～Q50 mm。

## LHA-Q-0100

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: M/N

### Question

PDF推荐的SMC空气传感器型号是什么？

### Standard Answer

答案为：ISA3-G。

### Scoring Standard

- P1 [100]: 正确给出：ISA3-G

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 531
- Section: 推荐空气传感器
- Local scope path: 推荐空气传感器 > SMC空气传感器
- Evidence type: TABLE
- Evidence: 表名：推荐空气传感器；行：空气传感器；列：SMC；原值：ISA3-G。

## LHA-Q-0101

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: M/N

### Question

PDF推荐的CKD间隙开关型号是什么？

### Standard Answer

答案为：GPS3-E。

### Scoring Standard

- P1 [100]: 正确给出：GPS3-E

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 531
- Section: 推荐空气传感器
- Local scope path: 推荐空气传感器 > CKD间隙开关
- Evidence type: TABLE
- Evidence: 表名：推荐空气传感器；行：间隙开关；列：CKD；原值：GPS3-E。

## LHA-Q-0103

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

在F型压板设计尺寸中，LHA0650系列F型的A是多少？

### Standard Answer

答案为：40 mm。

### Scoring Standard

- P1 [100]: 正确给出：40 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 36
- Printed page: 534
- Section: F型压板设计尺寸
- Local scope path: F型压板设计尺寸 > LHA0650-F > 快换压板F型的设计尺寸
- Evidence type: TABLE
- Evidence: 表名：快换压板F型的设计尺寸；行：A；列：LHA0650；原值：40 mm。

## LHA-Q-0105

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: P

### Question

LHA-P双压臂型的压板由谁设计？

### Standard Answer

由用户自行设计。

### Scoring Standard

- P1 [100]: 由用户自行设计

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 35
- Printed page: 533
- Section: 压板设计尺寸
- Local scope path: 压板设计尺寸 > P型双压臂设计责任
- Evidence type: TEXT
- Evidence: -P型（双压臂型）压板时，由用户自行设计、配备。

## LHA-Q-0109

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LZH-T（LHA 资料内附件或关联产品）
- Model / Scope: LZH0650-T

### Question

在LZH-T附件表中，LZH0650-T的A是多少？

### Standard Answer

答案为：175 mm。

### Scoring Standard

- P1 [100]: 正确给出：175 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 37
- Printed page: 535
- Section: LZH-T附件表
- Local scope path: LZH-T附件表 > LZH0650-T > 锥形压板毛坯尺寸
- Evidence type: TABLE
- Evidence: 表名：锥形压板毛坯尺寸；行：A；列：LZH0650-T；原值：175 mm。

## LHA-Q-0112

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LZH-A（LHA 资料内附件或关联产品）
- Model / Scope: LZH0650-A

### Question

在LZH-A附件表中，LZH0650-A的A是多少？

### Standard Answer

答案为：175 mm。

### Scoring Standard

- P1 [100]: 正确给出：175 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 37
- Printed page: 535
- Section: LZH-A附件表
- Local scope path: LZH-A附件表 > LZH0650-A > 快换压板A型毛坯尺寸
- Evidence type: TABLE
- Evidence: 表名：快换压板A型毛坯尺寸；行：A；列：LZH0650-A；原值：175 mm。

## LHA-Q-0115

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LZH-F（LHA 资料内附件或关联产品）
- Model / Scope: LZH0650-F

### Question

在LZH-F附件表中，LZH0650-F的A是多少？

### Standard Answer

答案为：40 mm。

### Scoring Standard

- P1 [100]: 正确给出：40 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 38
- Printed page: 536
- Section: LZH-F附件表
- Local scope path: LZH-F附件表 > LZH0650-F > 快换压板F型毛坯尺寸
- Evidence type: TABLE
- Evidence: 表名：快换压板F型毛坯尺寸；行：A；列：LZH0650-F；原值：40 mm。

## LHA-Q-0117

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LZH-W/LZH-B（LHA 资料内附件或关联产品）
- Model / Scope: LZH-W/LZH-B :: 压板附件

### Question

LZH-W快换A型压板紧固组件由哪些零件组成？

### Standard Answer

楔块1、楔块2和紧固螺栓。

### Scoring Standard

- P1 [34]: 组件包含楔块1
- P2 [33]: 组件包含楔块2
- P3 [33]: 组件包含紧固螺栓

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 37
- Printed page: 535
- Section: 其他压板附件表
- Local scope path: 其他压板附件表 > LZH-W
- Evidence type: TABLE
- Evidence: 快换压板A型用紧固套件（LZH□-W）为另售品；紧固件内容为楔形块1、楔形块2和紧固螺栓。

## LHA-Q-0118

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LZH-W/LZH-B（LHA 资料内附件或关联产品）
- Model / Scope: LZH-W/LZH-B :: 压板附件

### Question

LZH-B在LHA附件中属于什么产品？

### Standard Answer

快换F型压板安装用螺栓。

### Scoring Standard

- P1 [100]: 快换F型压板安装用螺栓

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 38
- Printed page: 536
- Section: LHA附件：快换压板F型用安装螺栓
- Local scope path: LHA附件 > 快换压板F型用安装螺栓 > LZH-B
- Evidence type: TABLE
- Evidence: 附件：快换压板F型用安装螺栓；型号LZH□-B。快换压板F型用固定螺栓由用户另行购买。

## LHA-Q-0120

**Type: TABLE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 表面粗糙度标示对照

### Question

新版表面粗糙度标示中，Rz 25对应的Ra值是多少？

### Standard Answer

答案为：Ra 6.3。

### Scoring Standard

- P1 [100]: 正确给出：Ra 6.3

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 47
- Printed page: 1729
- Section: 表面粗糙度标示对照
- Local scope path: 表面粗糙度标示对照 > Rz 25 > 表面粗糙度标示更改
- Evidence type: TABLE
- Evidence: 表名：表面粗糙度标示更改；行：Rz 25；列：新标示；原值：Ra 6.3。

## LHA-Q-0123

**Type: TABLE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: O形密封圈新旧标示

### Question

新标示OR NBR-70-1 P7-N对应的旧标示是什么？

### Standard Answer

答案为：1AP7。

### Scoring Standard

- P1 [100]: 正确给出：1AP7

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 48
- Printed page: 1730
- Section: O形密封圈新旧标示
- Local scope path: O形密封圈新旧标示 > OR NBR-70-1 P7-N
- Evidence type: TABLE
- Evidence: 表名：O形密封圈新旧标示；行：新标示 OR NBR-70-1 P7-N；列：旧标示；原值：1AP7。

## LHA-Q-0126

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK BZL（LHA 资料内附件或关联产品）
- Model / Scope: BZL0201

### Question

在BZL规格表中，BZL0201的推荐紧固力矩是多少？

### Standard Answer

答案为：25 N·m。

### Scoring Standard

- P1 [100]: 正确给出：25 N·m

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 51
- Printed page: 1259
- Section: BZL规格表
- Local scope path: BZL规格表 > BZL0201 > BZL规格
- Evidence type: TABLE
- Evidence: 表名：BZL规格；行：紧固力矩；列：BZL0201；原值：25 N·m。

## LHA-Q-0129

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK BZL（LHA 资料内附件或关联产品）
- Model / Scope: BZL0201

### Question

在BZL外形尺寸表中，BZL0201的A是多少？

### Standard Answer

答案为：18 mm。

### Scoring Standard

- P1 [100]: 正确给出：18 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 54
- Printed page: 1262
- Section: BZL外形尺寸表
- Local scope path: BZL外形尺寸表 > BZL0201 > BZL外形尺寸
- Evidence type: TABLE
- Evidence: 表名：BZL外形尺寸；行：A；列：BZL0201；原值：18 mm。

## LHA-Q-0131

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK BZT（LHA 资料内附件或关联产品）
- Model / Scope: BZT :: 高压速度控制阀

### Question

BZT在直装控制阀对应表中属于哪类产品？

### Standard Answer

高压用速度控制阀。

### Scoring Standard

- P1 [100]: 高压用速度控制阀

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 50
- Printed page: 1258
- Section: 直装控制阀对应表
- Local scope path: 直装控制阀对应表 > 速度控制阀（高压用） > Model BZT
- Evidence type: TABLE
- Evidence: 直装控制阀对应表将Model BZT标为速度控制阀（高压用），最高使用压力为35 MPa以下。

## LHA-Q-0133

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK BZX（LHA 资料内附件或关联产品）
- Model / Scope: BZX020

### Question

在BZX规格表中，BZX020的推荐紧固力矩是多少？

### Standard Answer

答案为：25 N·m。

### Scoring Standard

- P1 [100]: 正确给出：25 N·m

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 55
- Printed page: 1265
- Section: BZX规格表
- Local scope path: BZX规格表 > BZX020 > BZX规格
- Evidence type: TABLE
- Evidence: 表名：BZX规格；行：紧固力矩；列：BZX020；原值：25 N·m。

## LHA-Q-0136

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK BZX（LHA 资料内附件或关联产品）
- Model / Scope: BZX020

### Question

在BZX外形尺寸表中，BZX020的A是多少？

### Standard Answer

答案为：18 mm。

### Scoring Standard

- P1 [100]: 正确给出：18 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 56
- Printed page: 1266
- Section: BZX外形尺寸表
- Local scope path: BZX外形尺寸表 > BZX020 > BZX外形尺寸
- Evidence type: TABLE
- Evidence: 表名：BZX外形尺寸；行：A；列：BZX020；原值：18 mm。

## LHA-Q-0139

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK JZG（LHA 资料内附件或关联产品）
- Model / Scope: JZG020

### Question

在JZG规格表中，JZG020的铝材推荐紧固力矩是多少？

### Standard Answer

答案为：20 N·m。

### Scoring Standard

- P1 [100]: 正确给出：20 N·m

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 57
- Printed page: 1267
- Section: JZG规格表
- Local scope path: JZG规格表 > JZG020 > JZG规格
- Evidence type: TABLE
- Evidence: 表名：JZG规格；行：紧固力矩；列：JZG020；原值：20 N·m。

## LHA-Q-0142

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK JZG（LHA 资料内附件或关联产品）
- Model / Scope: JZG020

### Question

在JZG外形尺寸表中，JZG020的A是多少？

### Standard Answer

答案为：18 mm。

### Scoring Standard

- P1 [100]: 正确给出：18 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 58
- Printed page: 1268
- Section: JZG外形尺寸表
- Local scope path: JZG外形尺寸表 > JZG020 > JZG外形尺寸
- Evidence type: TABLE
- Evidence: 表名：JZG外形尺寸；行：A；列：JZG020；原值：18 mm。

## LHA-Q-0145

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK BZS（LHA 资料内附件或关联产品）
- Model / Scope: BZS0200

### Question

在BZS规格表中，BZS0200的P1→P2最小通路面积是多少？

### Standard Answer

答案为：5.7 mm²。

### Scoring Standard

- P1 [100]: 正确给出：5.7 mm²

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 59
- Printed page: 1269
- Section: BZS规格表
- Local scope path: BZS规格表 > BZS0200 > BZS规格
- Evidence type: TABLE
- Evidence: 表名：BZS规格；行：最小通路面积；列：BZS0200；原值：5.7 mm²。

## LHA-Q-0148

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK BZS（LHA 资料内附件或关联产品）
- Model / Scope: BZS0200

### Question

在BZS外形尺寸表中，BZS0200的A是多少？

### Standard Answer

答案为：22 mm。

### Scoring Standard

- P1 [100]: 正确给出：22 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 61
- Printed page: 1271
- Section: BZS外形尺寸表
- Local scope path: BZS外形尺寸表 > BZS0200 > BZS外形尺寸
- Evidence type: TABLE
- Evidence: 表名：BZS外形尺寸；行：A；列：BZS0200；原值：22 mm。

## LHA-Q-0151

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LZ-MS（LHA 资料内附件或关联产品）
- Model / Scope: LZ0650-MS

### Question

在LZ-MS尺寸重量表中，LZ0650-MS的A是多少？

### Standard Answer

答案为：82 mm。

### Scoring Standard

- P1 [100]: 正确给出：82 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 66
- Printed page: 1700
- Section: LZ-MS尺寸重量表
- Local scope path: LZ-MS尺寸重量表 > LZ0650-MS > LZ-MS外形尺寸
- Evidence type: TABLE
- Evidence: LZ-MS尺寸重量表；行A；列LZ0650-MS；交叉值82 mm。

## LHA-Q-0154

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LZ-MP（LHA 资料内附件或关联产品）
- Model / Scope: LZ0550-MP

### Question

在LZ-MP尺寸重量表中，LZ0550-MP的A是多少？

### Standard Answer

答案为：30 mm。

### Scoring Standard

- P1 [100]: 正确给出：30 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 66
- Printed page: 1700
- Section: LZ-MP尺寸重量表
- Local scope path: LZ-MP尺寸重量表 > LZ0550-MP > LZ-MP外形尺寸
- Evidence type: TABLE
- Evidence: LZ-MP尺寸重量表；行A；列LZ0550-MP；交叉值30 mm。

## LHA-Q-0156

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LZ-C（LHA 资料内附件或关联产品）
- Model / Scope: LZ-C :: 板式安装座

### Question

LZ-C板式安装座适用于哪种机器型号？

### Standard Answer

答案为：LD。

### Scoring Standard

- P1 [100]: 正确给出：LD

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 64
- Printed page: 1698
- Section: 板式安装座适用型号表
- Local scope path: 板式安装座适用型号表 > LZ-C > 板式安装座适用型号
- Evidence type: TABLE
- Evidence: 表名：板式安装座适用型号；行：适用机器型号；列：LZ-C；原值：LD。

## LHA-Q-0157

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LZ-CQ（LHA 资料内附件或关联产品）
- Model / Scope: LZ-CQ :: 板式安装座

### Question

LZ-CQ板式安装座适用于哪种机器型号？

### Standard Answer

答案为：LD-Q。

### Scoring Standard

- P1 [100]: 正确给出：LD-Q

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 64
- Printed page: 1698
- Section: 板式安装座适用型号表
- Local scope path: 板式安装座适用型号表 > LZ-CQ > 板式安装座适用型号
- Evidence type: TABLE
- Evidence: 表名：板式安装座适用型号；行：适用机器型号；列：LZ-CQ；原值：LD-Q。

## LHA-Q-0158

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK TMZ（LHA 资料内附件或关联产品）
- Model / Scope: TMZ :: 板式安装座

### Question

TMZ-1MB板式安装座适用于哪种机器型号？

### Standard Answer

答案为：TMA-1。

### Scoring Standard

- P1 [100]: 正确给出：TMA-1

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 64
- Printed page: 1698
- Section: 板式安装座适用型号表
- Local scope path: 板式安装座适用型号表 > TMZ-1MB > 板式安装座适用型号
- Evidence type: TABLE
- Evidence: 表名：板式安装座适用型号；行：适用机器型号；列：TMZ-1MB；原值：TMA-1。

## LHA-Q-0167

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA-M 系列

### Question

安装LHA-M型检测用O形密封圈时，应涂布什么、用量不当可能造成什么问题？

### Standard Answer

安装时应在空气传感器O形密封圈部涂布适量甘油。干燥安装容易导致O形密封圈扭曲或损坏；润滑油涂抹过多可能溢出并堵塞检测口，导致空气传感器误动作。

### Scoring Standard

- P1 [25]: 安装时涂布适量甘油
- P2 [25]: 干燥安装会导致O形密封圈扭曲或损坏
- P3 [25]: 润滑油过多会溢出并堵塞检测口
- P4 [25]: 检测口堵塞会导致空气传感器误动作

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 531
- Section: 注意事项
- Local scope path: 注意事项 > 检测用O形密封圈润滑
- Evidence type: TEXT
- Evidence: LHA-M安装时应在空气传感器O形密封圈部涂布适量甘油；干燥安装容易使O形密封圈扭曲或损坏，润滑油过多会溢出并堵塞检测口，导致空气传感器误动作。

## LHA-Q-0169

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

在焊接夹具中使用LHA时，应如何保护活塞杆滑动面，焊渣附着会有什么后果？

### Standard Answer

应保护活塞杆滑动面，避免焊渣附着；焊渣附着会导致动作异常或漏油。

### Scoring Standard

- P1 [25]: 保护活塞杆滑动面
- P2 [25]: 避免焊渣附着
- P3 [25]: 焊渣会导致动作异常
- P4 [25]: 焊渣会导致漏油

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 745
- Section: LHA专项注意事项
- Local scope path: LHA专项注意事项 > 设计方面 > 用于焊接夹具
- Evidence type: TEXT
- Evidence: LHA设计注意事项：用于焊接夹具时应保护活塞杆滑动面；滑动面沾上焊渣会导致动作不正常、漏油等故障。

## LHA-Q-0170

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

在倾斜面上夹紧工件时，工件夹紧面与夹紧器安装面应满足什么位置关系？

### Standard Answer

两者应保持平行。

### Scoring Standard

- P1 [100]: 两者应保持平行

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 745
- Section: 注意事项
- Local scope path: 注意事项 > 倾斜面夹紧
- Evidence type: TEXT
- Evidence: ● 惯性力矩过大会导致压板的停止精度恶化，以及油压旋转夹紧器破损等 旋转式 L 夹 H 紧 A 器 复动 故障。另外，有时会因供给油压或压板安装姿势导致夹紧器无法旋转。 LHC 5) 需要夹紧工件的倾斜面时 单动 ● 请在设计时使工件的夹紧面与夹紧器安装面保持平行。 杠杆式 L 夹 K 紧 A 器 复动

## LHA-Q-0171

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

安装LHA本体时应怎样使用安装孔和螺栓，紧固力矩过大会有什么后果？

### Standard Answer

安装本体时应使用全部安装螺栓孔，使用强度等级12.9的内六角螺栓并按表中推荐力矩紧固。紧固力矩过大会导致基座塌陷和螺栓热粘等故障。

### Scoring Standard

- P1 [20]: 使用全部安装螺栓孔
- P2 [20]: 使用强度等级12.9的内六角螺栓
- P3 [20]: 按表中推荐力矩紧固
- P4 [20]: 过大力矩会导致基座塌陷
- P5 [20]: 过大力矩会导致螺栓热粘

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 39
- Printed page: 745
- Section: 注意事项
- Local scope path: 注意事项 > 本体安装
- Evidence type: TEXT
- Evidence: ● 在设计油压回路时，请认真阅读“夹紧器的速度控制回路和注意事项”， ● 安装本体时应用足所有的安装螺栓孔，并按下表所示力矩紧固 | 内六角螺栓(强度等级12.9)。 | 紧固力矩过大会导致基座塌陷和螺栓热粘等故障。 | 设计适当的油压回路。回路设计错误会导致机械设备误动作、破损等 | 事故。(请参照第1726页) | 2) 回路设计时的注意事项 | 安装螺栓标称 紧固力矩(N･m)

## LHA-Q-0172

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

安装LHA旋转压板时，紧固力矩应遵循什么要求，超过推荐力矩会有什么后果？

### Standard Answer

应按对应型号表的推荐力矩紧固；超过推荐力矩会造成螺栓胶着或压板紧固机构损坏。

### Scoring Standard

- P1 [34]: 按型号表推荐力矩紧固
- P2 [33]: 超过推荐力矩会导致螺栓胶着
- P3 [33]: 超过推荐力矩会损坏压板紧固机构

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 40
- Printed page: 746
- Section: 注意事项
- Local scope path: 注意事项 > 压板紧固力矩
- Evidence type: TEXT
- Evidence: 安装LHA旋转压板时必须按对应型号表的推荐力矩紧固螺栓；超过推荐力矩会导致螺栓胶着或压板紧固机构破损。

## LHA-Q-0173

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

安装LHA压板前应如何处理压板、锥套和活塞杆连接部，未清洁会有什么后果？

### Standard Answer

应充分脱脂并清洗；残留油污或异物可能导致压板松动。

### Scoring Standard

- P1 [25]: 安装前脱脂
- P2 [25]: 安装前清洗
- P3 [25]: 油污可能导致压板松动
- P4 [25]: 异物可能导致压板松动

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 40
- Printed page: 746
- Section: 注意事项
- Local scope path: 注意事项 > 压板安装
- Evidence type: TEXT
- Evidence: LHA-F/LHS-F/LG-F/LT-F：快换压板F型、TLA-2/TLB-2/TLA-1/TLV-2：标准 | 如果紧固力矩超出推荐力矩，会导致螺栓的胶着，压板紧固机构 | ● 如果压板、锥套、活塞杆的连接部位沾有油污或异物，就可能会 | 导致压板松动。应充分进行脱脂、清洗，去除油污或异物。 | M14×1.5 21 〜 25 | M10×1.25 | M20×1.5 54 〜 65

## LHA-Q-0174

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA 系列

### Question

拆卸LHA锥形压板时应按什么步骤操作？

### Standard Answer

先将旋转夹紧器固定在夹具或虎钳等工具上；用扳手卡住活塞杆顶端六角孔；将活塞杆转到旋转角度的中间位置；然后旋松压板固定螺母；将螺母旋松2至3圈；在不给活塞杆施加旋转力矩的情况下，用齿轮拔出器等工具拔出压板。

### Scoring Standard

- P1 [15]: 将夹紧器固定在夹具或虎钳上
- P2 [15]: 用扳手卡住活塞杆顶端六角孔
- P3 [14]: 将活塞杆转到旋转角度中间位置
- P4 [14]: 旋松压板固定螺母
- P5 [14]: 将螺母旋松2至3圈
- P6 [14]: 不给活塞杆施加旋转力矩
- P7 [14]: 用齿轮拔出器拔出压板

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 41
- Printed page: 747
- Section: 注意事项
- Local scope path: 注意事项 > 锥形压板拆卸
- Evidence type: TEXT + PROCEDURE
- Evidence: 将旋转夹紧器固定在夹具或虎钳等工具上，用扳手卡住活塞杆顶端六角孔，将活塞杆旋转到旋转角度的中间位置，然后旋松压板固定螺母。将螺母旋松2至3圈，在不给活塞杆施加旋转力矩的前提下，用齿轮拔出器等工具拔出压板。

## LHA-Q-0175

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA-D 系列

### Question

安装探头时应如何防止LHA活塞杆转动？

### Standard Answer

用扳手固定四方形活塞杆前端后再安装探头。

### Scoring Standard

- P1 [100]: 用扳手固定四方形活塞杆前端后再安装探头

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 42
- Printed page: 748
- Section: 注意事项
- Local scope path: 注意事项 > 探头安装
- Evidence type: TEXT
- Evidence: ● 安装探头时请固定活塞杆，不要让它转动。用扳手固定住四方形的 | 活塞前端后，然后安装探头。螺纹零部件的夹紧力矩如下图所示。 | 6) 关于探头安装用双出杆型(-D)夹紧器的注意事项 | 3.2 | LHA0360-□□D | TMA-2 复动 | TLV-2

## LHA-Q-0178

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

缠绕液压配管接头的密封胶带时应留出多少螺纹牙，胶带残留进入回路会有什么后果？

### Standard Answer

接头顶部应留出1至2个螺纹牙；胶带残留进入回路会导致漏油或动作异常。

### Scoring Standard

- P1 [34]: 接头顶部留出1至2个螺纹牙
- P2 [33]: 胶带残留可能导致漏油
- P3 [33]: 胶带残留可能导致动作异常

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 43
- Printed page: 1725
- Section: 注意事项
- Local scope path: 注意事项 > 密封胶带
- Evidence type: TEXT
- Evidence: ● 缠绕时请留出接头顶部1 ~ 2个螺纹牙。 | ● 残留在回路内的密封胶带头会导致漏油或动作不正常等故障。 | ● 回路中的异物或切削屑等会导致漏油或动作不良。 | ISO 粘度等级ISO-VG-32 | Showa Shell Sekiyu Tellus S2 M 32 Morlina S2 B 32 | Idemitsu Kosan Daphne Hydraulic Fluid 32 Daphne Super Multi Oil 32 | JX Nippon Oil & Energy Super Hyrando 32 Super Mulpus DX 32

## LHA-Q-0179

**Type: FACT**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

哪些情况下需要对液压回路进行排气？

### Standard Answer

配管作业后，或因泵的油箱排空等原因使空气进入液压回路后，都需要排气。

### Scoring Standard

- P1 [50]: 配管作业后需要排气
- P2 [50]: 空气因油箱排空等原因进入回路后需要排气

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 43
- Printed page: 1725
- Section: 注意事项
- Local scope path: 注意事项 > 完整排气步骤
- Evidence type: TEXT
- Evidence: 进行配管作业后，或因泵油箱排空等原因使空气进入液压回路后，请进行排气。

## LHA-Q-0180

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

单动夹紧器的速度控制回路应如何设置，释放流量过小会有什么后果？

### Standard Answer

应使用内置单向阀的流量调整阀，原则上只控制锁紧动作流量；释放流量过小会导致释放脉动、停止或释放时间异常变长。

### Scoring Standard

- P1 [20]: 使用内置单向阀的流量调整阀
- P2 [20]: 原则上只控制锁紧动作流量
- P3 [20]: 释放流量过小会产生释放脉动
- P4 [20]: 释放流量过小会导致停止
- P5 [20]: 释放流量过小会延长释放时间

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 44
- Printed page: 1726
- Section: 注意事项
- Local scope path: 注意事项 > 单动夹紧器速度回路
- Evidence type: TEXT
- Evidence: 单动夹紧器应使用内置单向阀的流量调整阀，原则上只控制锁紧动作流量；释放流量过小会使释放动作脉动、停止或释放时间异常变长。

## LHA-Q-0181

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

对于LKE、LSE、TLA、TLB、TMA、TLV、TMV、TTA以外的复动夹紧器，夹紧侧和释放侧原则上应采用什么节流回路？

### Standard Answer

两侧均采用回油节流回路；采用进油节流容易受到回路中空气影响，难以稳定控制速度。

### Scoring Standard

- P1 [25]: 指定例外型号之外的复动夹紧器两侧采用回油节流
- P2 [25]: 例外型号为LKE、LSE、TLA、TLB、TMA、TLV、TMV、TTA
- P3 [25]: 进油节流容易受回路空气影响
- P4 [25]: 受空气影响时速度难以稳定控制

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 44
- Printed page: 1726
- Section: 注意事项
- Local scope path: 注意事项 > 复动夹紧器速度回路
- Evidence type: TEXT
- Evidence: LKE、LSE、TLA、TLB、TMA、TLV、TMV、TTA以外的复动夹紧器，夹紧侧和释放侧都使用回油节流回路。采用进油节流时，容易受到回路中空气的影响，速度控制会变得困难。

## LHA-Q-0182

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

对于LKE、LSE、TLA、TLB、TMA、TLV、TMV、TTA，夹紧侧和释放侧应采用什么节流回路？误用回油节流可能造成什么后果？

### Standard Answer

夹紧侧和释放侧均采用进油节流回路；误用回油节流会使回路产生异常高压，可能导致夹紧器漏油或损坏。

### Scoring Standard

- P1 [20]: 例外型号两侧采用进油节流
- P2 [20]: 例外型号为LKE、LSE、TLA、TLB、TMA、TLV、TMV、TTA
- P3 [20]: 误用回油节流会产生异常高压
- P4 [20]: 异常高压可能导致漏油
- P5 [20]: 异常高压可能导致损坏

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 44
- Printed page: 1726
- Section: 注意事项
- Local scope path: 注意事项 > 进油节流与回油节流
- Evidence type: TEXT
- Evidence: 产生异常高压导致 夹紧器漏油或损坏。 | 采用进油节流回路进行速度控制时，易受油压回路中混入空气的 | 请将夹紧侧和释放侧均设置为进油节流回路。

## LHA-Q-0183

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

拆卸液压产品前必须完成哪些安全确认？

### Standard Answer

切断压力源和电源，并确认油压与气压回路压力均为零。

### Scoring Standard

- P1 [25]: 切断压力源
- P2 [25]: 关闭电源
- P3 [25]: 确认油压回路压力为零
- P4 [25]: 确认气压回路压力为零

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 45
- Printed page: 1727
- Section: 注意事项
- Local scope path: 注意事项 > 拆卸前安全
- Evidence type: TEXT + PROCEDURE
- Evidence: ● 请指派具备丰富知识和经验的员工操作使用液压／气动装置的 ● 拆卸装置时，必须认真确认是否已对被驱动物体采取了防止坠 | 落措施和防止误动作等措施，同时应切断压力源和电源，确认 | 切断压力源和电源，确定油压•气压回路的压力为零后方可进行 | 1) 请指派具备丰富知识和专业经验的员工操作使用液压装置。 | 油压•气压回路的压力为零后方可进行拆卸作业。 | ① 对机械设备和装置进行检查、维护前，必须认真确认是否已对 | 1) 拆卸设备时必须切断压力源

## LHA-Q-0184

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

液压夹紧器动作过程中是否可以接触，违反要求可能造成什么后果？

### Standard Answer

严禁接触动作中的夹紧器，否则可能造成手指夹伤等人身伤害。

### Scoring Standard

- P1 [50]: 严禁接触动作中的夹紧器
- P2 [50]: 接触可能造成人身伤害

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 45
- Printed page: 1727
- Section: 注意事项
- Local scope path: 注意事项 > 防止夹伤
- Evidence type: TEXT
- Evidence: ② 拆卸机器设备时，应确认是否已落实了上述安全措施，同时应 ● 在表面附有污物的状态下使用会损伤密封材料，导致动作不正常、 | 2) 在安全措施尚未落实的情况下，严禁操作、拆卸机械设备。 | 3) 为防止造成人身伤害，严禁接触动作中的夹紧器。否则会导致手指夹 | ④ 重新启动机械装置前应认真确认螺栓等连接部位有无异常。 | ● 重新启动机械设备前应认真确认螺栓等连接部位有无异常现象。 | 5) 请定期检查配管•安装螺栓•螺母•固定环•夹紧器有无松动现象， | 2) 请定期对活塞杆、柱塞周围进行清扫。

## LHA-Q-0185

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

活塞杆和柱塞周围应如何维护，污物积聚会有什么后果？

### Standard Answer

应定期清扫；污物会损伤密封材料，造成动作异常或漏油。

### Scoring Standard

- P1 [25]: 定期清扫活塞杆周围
- P2 [25]: 定期清扫柱塞周围
- P3 [25]: 污物会损伤密封材料
- P4 [25]: 污物会导致动作异常或漏油

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 45
- Printed page: 1727
- Section: 液压通用注意事项
- Local scope path: 液压通用注意事项 > 保养、检查 > 活塞杆和柱塞周围清扫
- Evidence type: TEXT
- Evidence: 保养、检查要求定期清扫活塞杆和柱塞周围；表面附有污物会损伤密封材料，导致动作不正常、漏油等故障。

## LHA-Q-0186

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

PDF要求定期检查并紧固哪些部位？

### Standard Answer

应定期检查配管、安装螺栓、螺母、固定环和夹紧器，并对松动处及时紧固。

### Scoring Standard

- P1 [17]: 检查配管
- P2 [17]: 检查安装螺栓
- P3 [17]: 检查螺母
- P4 [17]: 检查固定环
- P5 [16]: 检查夹紧器
- P6 [16]: 及时紧固松动处

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 45
- Printed page: 1727
- Section: 注意事项
- Local scope path: 注意事项 > 松动检查
- Evidence type: TEXT
- Evidence: 回路中会混入空气，故请定期对回路进行排气处理。 5) 请定期检查配管•安装螺栓•螺母•固定环•夹紧器有无松动现象， 6) 请检查确认液压油是否存在老化现象。

## LHA-Q-0187

**Type: FACT**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

PDF规定的产品保修期如何计算？

### Standard Answer

从本厂发货后1年半或开始使用后1年内，以较短者为准。

### Scoring Standard

- P1 [34]: 本厂发货后保修1年半
- P2 [33]: 开始使用后保修1年
- P3 [33]: 以较短期限为准

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 46
- Printed page: 1728
- Section: 注意事项
- Local scope path: 注意事项 > 保修期
- Evidence type: TEXT
- Evidence: ● 产品的保修期是从本厂发货后1年半，或者开始使用后1年内 | ● 保修期间因本公司的责任发生的故障或不良现象，均由本公司 | 但是下记事项，因使用方管理不善而出现故障时，不属保修范 | 1728 | 2) 保修范围 | 1) 保修期 | ① 没有按规定条款进行定期检查及维护时。

## LHA-Q-0188

**Type: FACT**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

在保修期内，因本公司责任发生故障或不良时，保修范围是什么？

### Standard Answer

由本公司更换或修理发生故障的部分。

### Scoring Standard

- P1 [50]: 本公司更换故障部分
- P2 [50]: 本公司修理故障部分

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 46
- Printed page: 1728
- Section: 注意事项
- Local scope path: 注意事项 > 保修范围
- Evidence type: TEXT
- Evidence: ⑤ 自行进行改造、修理，或未经本公司同意擅自进行改造、修理 | ● 保修期间因本公司的责任发生的故障或不良现象，均由本公司 | ④ 非本公司产品质量方面的原因造成的故障。 | 负责进行故障部分的更换或修理。 | 1728 | 操作方面的注意事项 保养、检查 | 2) 保修范围

## LHA-Q-0189

**Type: FACT**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

PDF列出的不属于保修范围的七类情形是什么？

### Standard Answer

未定期检查维护；操作人员判断失误或使用不当；用户或第三方不当使用；非产品质量原因；未经同意改造或修理；自然灾害等非本公司责任；磨损老化备件及其更换费用。

### Scoring Standard

- P1 [15]: 未定期检查维护不保修
- P2 [15]: 操作人员判断失误或使用不当不保修
- P3 [14]: 用户或第三方不当使用不保修
- P4 [14]: 非产品质量原因不保修
- P5 [14]: 未经同意改造或修理不保修
- P6 [14]: 自然灾害等非本公司责任不保修
- P7 [14]: 磨损老化备件及更换费用不保修

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 46
- Printed page: 1728
- Section: 注意事项
- Local scope path: 注意事项 > 七类不保修情形
- Evidence type: TEXT
- Evidence: ⑦ 因磨损、老化发生的备件费用或更换费用。 | 负责进行故障部分的更换或修理。 | ① 没有按规定条款进行定期检查及维护时。

## LHA-Q-0190

**Type: FACT**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

产品故障造成的间接损失是否属于质保范围？

### Standard Answer

不属于质保范围。

### Scoring Standard

- P1 [100]: 不属于质保范围

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 46
- Printed page: 1728
- Section: 注意事项
- Local scope path: 注意事项 > 间接损失
- Evidence type: TEXT
- Evidence: ⑥ 其他非本公司的责任造成的故障，例如自然灾害等引起的故障。 | 另外，因本公司产品故障造成的间接损失不在质保范围之内。 | ② 因操作人员的判断失误、使用不当造成的故障。 | ④ 非本公司产品质量方面的原因造成的故障。 | ③ 因用户不适当使用和操作而造成故障时。 | 而造成的故障。 | 2) 保修范围

## LHA-Q-0191

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK BZS 直装式顺序阀
- Model / Scope: BZS0200

### Question

BZS0200的推荐紧固力矩是多少？

### Standard Answer

答案为：25 N·m。

### Scoring Standard

- P1 [100]: 正确给出：25 N·m

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 59
- Printed page: 1269
- Section: BZS规格
- Local scope path: BZS规格 > 紧固力矩 > BZS0200
- Evidence type: TABLE
- Evidence: 表名：BZS规格；行：紧固力矩；列：BZS0200；原值：25 N·m。

## LHA-Q-0192

**Type: MODEL**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 液压产品通用内容
- Model / Scope: LHA_R00_2023KW_C1N.pdf :: 注意事项

### Question

O形密封圈标示中，NBR-70-1、NBR-90、P和N分别表示什么？

### Standard Answer

NBR-70-1或旧代码1A表示一般用丁腈橡胶、A型硬度70；NBR-90或旧代码1B表示一般用丁腈橡胶、A型硬度90；P表示滑动用；N表示一般用。

### Scoring Standard

- P1 [25]: NBR-70-1表示一般用丁腈橡胶且A型硬度70
- P2 [25]: NBR-90表示一般用丁腈橡胶且A型硬度90
- P3 [25]: P表示滑动用
- P4 [25]: N表示一般用

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 48
- Printed page: 1730
- Section: 注意事项
- Local scope path: 注意事项 > O形密封圈材料代码
- Evidence type: MODEL + TABLE
- Evidence: NBR-70-1 / 1A：一般用丁腈橡胶，A型硬度70。NBR-90 / 1B：一般用丁腈橡胶，A型硬度90。P：滑动用。N：一般用。

## LHA-Q-0193

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LZ-MP 板式安装座
- Model / Scope: LZ-MP 系列

### Question

LZ-MP板式安装座适用于哪些机器型号？

### Standard Answer

LC和TC。

### Scoring Standard

- P1 [100]: LC和TC

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 64
- Printed page: 1698
- Section: 板式安装座适用型号
- Local scope path: 板式安装座适用型号 > LZ-MP > LC、TC
- Evidence type: TABLE
- Evidence: 表名：板式安装座适用型号；行：适用机器型号；列：LZ-MP；原值：LC和TC。

## LHA-Q-0194

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650-D 系列

### Question

LHA0650系列D型探头螺纹的紧固力矩是多少？

### Standard Answer

答案为：25 N·m。

### Scoring Standard

- P1 [100]: 正确给出：25 N·m

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号或其他版本文档数据
- 不得加入当前PDF无法支持的关键事实
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 42
- Printed page: 748
- Section: LHA专项注意事项
- Local scope path: LHA专项注意事项 > 探头安装用双出杆型（-D） > LHA0650-D
- Evidence type: TABLE
- Evidence: 表名：探头安装表；行：探头螺纹紧固力矩；列：LHA0650-D；原值：25 N·m。

## LHA-Q-0198

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA1050

### Question

在LHA夹紧力表中，当LHA1050的供给油压为2 MPa时，最大压板长度L是多少？

### Standard Answer

答案为：380 mm。

### Scoring Standard

- P1 [100]: 数值和单位同时正确：380 mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用其他型号、压板长度或压力条件
- 缺少单位不得获得100分
- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- 数值须精确匹配，单位为 mm。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 10
- Printed page: 508
- Section: 能力曲线
- Local scope path: 能力曲线 > 最大压板长度 > LHA1050夹紧力表
- Evidence type: TABLE
- Evidence: LHA夹紧力表：LHA1050在供给油压2 MPa时，最大压板长度L为380 mm。

## LHA-Q-0199

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0360

### Question

根据LHA0360夹紧力能力曲线图估读，当压板长度L=100 mm、供给油压P=2.25 MPa时，夹紧力F约为多少？

### Standard Answer

约0.5 kN。

### Scoring Standard

- P1 [75]: 数值在0.25至0.75 kN范围内
- P2 [25]: 图表估读值单位为kN

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用其他型号、压板长度或压力条件
- 缺少单位不得获得100分
- 使用EXACT容差属于校验失败
- 不得用公式计算值替代图表视觉读数，也不得混淆坐标轴、曲线系列或型号。

### Tolerance

- 图表读数允许误差：±0.25 kN。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 507
- Section: 能力曲线
- Local scope path: 能力曲线 > 夹紧力能力曲线估读 > LHA0360夹紧力能力曲线
- Evidence type: CHART
- Evidence: LHA0360夹紧力能力曲线图：L=100 mm、P=2.25 MPa时，视觉估读F约0.5 kN，图表读数容差为±0.25 kN。

## LHA-Q-0200

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0480

### Question

根据LHA0480夹紧力能力曲线图估读，当压板长度L=140 mm、供给油压P=4.25 MPa时，夹紧力F约为多少？

### Standard Answer

约2.1 kN。

### Scoring Standard

- P1 [75]: 数值在1.6至2.6 kN范围内
- P2 [25]: 图表估读值单位为kN

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用其他型号、压板长度或压力条件
- 缺少单位不得获得100分
- 使用EXACT容差属于校验失败
- 不得用公式计算值替代图表视觉读数，也不得混淆坐标轴、曲线系列或型号。

### Tolerance

- 图表读数允许误差：±0.5 kN。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 507
- Section: 能力曲线
- Local scope path: 能力曲线 > 夹紧力能力曲线估读 > LHA0480夹紧力能力曲线
- Evidence type: CHART
- Evidence: LHA0480夹紧力能力曲线图：L=140 mm、P=4.25 MPa时，视觉估读F约2.1 kN，图表读数容差为±0.25 kN。

## LHA-Q-0201

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0550

### Question

根据LHA0550夹紧力能力曲线图估读，当压板长度L=140 mm、供给油压P=6.25 MPa时，夹紧力F约为多少？

### Standard Answer

约4.6 kN。

### Scoring Standard

- P1 [75]: 数值在4.1至5.1 kN范围内
- P2 [25]: 图表估读值单位为kN

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用其他型号、压板长度或压力条件
- 缺少单位不得获得100分
- 使用EXACT容差属于校验失败
- 不得用公式计算值替代图表视觉读数，也不得混淆坐标轴、曲线系列或型号。

### Tolerance

- 图表读数允许误差：±0.5 kN。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 507
- Section: 能力曲线
- Local scope path: 能力曲线 > 夹紧力能力曲线估读 > LHA0550夹紧力能力曲线
- Evidence type: CHART
- Evidence: LHA0550夹紧力能力曲线图：L=140 mm、P=6.25 MPa时，视觉估读F约4.6 kN，图表读数容差为±0.25 kN。

## LHA-Q-0203

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0550

### Question

按PDF公式计算：LHA0550在供给油压P=4.5 MPa、压板长度L=140 mm时，夹紧力F是多少？结果用kN表示。

### Standard Answer

使用公式或指定算术关系：F=P×(1-0.0011×L)/(1.0039+0.0011×L) 代入：主体尺寸=055；供给压力=4.5 MPa；压板长度=140 mm。 Decimal完整精度计算：force=3.287848691596856377925554883841437 kN。 按ROUND_HALF_UP显示：force=3.288 kN。

### Scoring Standard

- P1 [20]: 使用LHA0550公式：F=P×(1-0.0011×L)/(1.0039+0.0011×L)
- P2 [20]: 将题目给定的P和L代入该公式
- P3 [45]: F数值为3.288且在容差内
- P4 [15]: F单位为kN

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- 数值输出允许相对误差：±0.5%。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 507
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > SINGLE_ARM_FORWARD > F=P×(1-0.0011×L)/(1.0039+0.0011×L)
- Evidence type: FORMULA + TABLE
- Evidence: LHA0550适用公式F=P×(1-0.0011×L)/(1.0039+0.0011×L)，其中F为夹紧力（kN）、P为供给油压（MPa）、L为压板长度（mm）。

## LHA-Q-0206

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0750

### Question

LHA0750采用压板长度L=160 mm。若目标夹紧力为9.987 kN，按PDF公式反求所需供给油压P，并与最高使用压力7.0 MPa比较，判断是否可实现。

### Standard Answer

使用公式或指定算术关系：F=P×(1-0.0007×L)/(0.5175+0.0006×L) 代入：主体尺寸=075；目标夹紧力=9.987 kN；压板长度=160 mm。 Decimal完整精度计算：所需压力=6.899802364864864864864864864864865 MPa；可行性结论为可行。 按ROUND_HALF_UP显示：所需压力=6.900 MPa；可行性结论为可行。

### Scoring Standard

- P1 [15]: 选择LHA0750原公式：F=P×(1-0.0007×L)/(0.5175+0.0006×L)
- P2 [20]: 正确变形为P=F×(b+dL)/(1-aL)
- P3 [10]: 正确代入题目给定的F和L
- P4 [30]: 所需压力数值为6.900
- P5 [10]: 所需压力单位为MPa
- P6 [15]: 可行性结论为可行

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- 所需压力：相对误差 ±0.5%。
- feasible：精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 8、10
- Printed page: 506、508
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > INVERSE_REQUIRED_PRESSURE > F=P×(1-0.0007×L)/(0.5175+0.0006×L)
- Evidence type: FORMULA + TABLE
- Evidence: LHA0750适用公式F=P×(1-0.0007×L)/(0.5175+0.0006×L)，其中F为夹紧力（kN）、P为供给油压（MPa）、L为压板长度（mm）；最高使用压力为7 MPa。

## LHA-Q-0209

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA1050

### Question

LHA1050在P=5.0 MPa时若需达到11.073 kN夹紧力，按PDF公式反求压板长度L，并与该条件下最大允许长度380 mm比较，判断是否满足限制。

### Standard Answer

使用公式或指定算术关系：F=P×(1-0.0008×L)/(0.2495+0.0002×L) 代入：主体尺寸=105；供给压力=5.0 MPa；目标夹紧力=11.073 kN。 Decimal完整精度计算：所需压板长度=360.0049077977665497377144144434075 mm；可行性结论为可行。 按ROUND_HALF_UP显示：所需压板长度=360.005 mm；可行性结论为可行。

### Scoring Standard

- P1 [15]: 选择LHA1050原公式：F=P×(1-0.0008×L)/(0.2495+0.0002×L)
- P2 [20]: 正确变形为L=(P-Fb)/(Fd+Pa)
- P3 [10]: 正确代入题目给定的P和F
- P4 [30]: 所需压板长度数值为360.005
- P5 [10]: 所需压板长度单位为mm
- P6 [15]: 可行性结论为可行

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- 所需压板长度：相对误差 ±0.5%。
- feasible：精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 10
- Printed page: 508
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > INVERSE_REQUIRED_ARM_LENGTH > F=P×(1-0.0008×L)/(0.2495+0.0002×L)
- Evidence type: FORMULA + TABLE
- Evidence: LHA1050适用公式F=P×(1-0.0008×L)/(0.2495+0.0002×L)，其中F为夹紧力（kN）、P为供给油压（MPa）、L为压板长度（mm）；P=5 MPa时最大压板长度为380 mm。

## LHA-Q-0212

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0750-P

### Question

按PDF P型双压臂公式计算：LHA0750-P在P=4.5 MPa、L1=55 mm、L2=95 mm、L3=150 mm时，F1和F2分别是多少？

### Standard Answer

使用公式或指定算术关系：F1=(L2/L3)×2.03×P；F2=(L1/L3)×2.03×P 代入：主体尺寸=075；供给压力=4.5 MPa；L1=55 mm；L2=95 mm；L3=150 mm。 Decimal完整精度计算：F1=5.785500000000000000000000000000002 kN；F2=3.349500000000000000000000000000000 kN。 按ROUND_HALF_UP显示：F1=5.786 kN；F2=3.350 kN。

### Scoring Standard

- P1 [15]: 使用正确F1公式：F1=(L2/L3)×2.03×P
- P2 [15]: 使用正确F2公式：F2=(L1/L3)×2.03×P
- P3 [10]: 正确代入P、L1、L2和L3
- P4 [20]: F1数值为5.786
- P5 [5]: F1单位为kN
- P6 [20]: F2数值为3.350
- P7 [5]: F2单位为kN
- P8 [10]: F1和F2与各自公式的对应关系未颠倒

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- F1：相对误差 ±0.5%。
- F2：相对误差 ±0.5%。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 506
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > DOUBLE_ARM_F1_F2 > F1=(L2/L3)×2.03×P；F2=(L1/L3)×2.03×P
- Evidence type: FORMULA + TABLE
- Evidence: LHA0750-P双压臂型适用公式F1=(L2/L3)×2.03×P、F2=(L1/L3)×2.03×P；F1、F2单位为kN，P单位为MPa，L1、L2、L3单位为mm。

## LHA-Q-0214

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0480-P

### Question

LHA0480-P在P=5.5 MPa、L1=45 mm、L2=75 mm、L3=120 mm时，先按PDF公式求F1、F2，再计算两侧夹紧力绝对差值。

### Standard Answer

使用公式或指定算术关系：F1=(L2/L3)×0.695×P；F2=(L1/L3)×0.695×P 代入：主体尺寸=048；供给压力=5.5 MPa；L1=45 mm；L2=75 mm；L3=120 mm。 Decimal完整精度计算：F1=2.3890625 kN；F2=1.4334375 kN；差值=0.9556250 kN。 按ROUND_HALF_UP显示：F1=2.389 kN；F2=1.433 kN；差值=0.956 kN。

### Scoring Standard

- P1 [10]: F1公式为F1=(L2/L3)×0.695×P
- P2 [10]: F2公式为F2=(L1/L3)×0.695×P
- P3 [15]: F1数值为2.389
- P4 [5]: F1单位为kN
- P5 [15]: F2数值为1.433
- P6 [5]: F2单位为kN
- P7 [15]: 使用绝对差值关系|F1-F2|
- P8 [20]: 差值数值为0.956
- P9 [5]: 差值单位为kN

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- F1：相对误差 ±0.5%。
- F2：相对误差 ±0.5%。
- 差值：相对误差 ±0.5%。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 506
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > DOUBLE_ARM_COMPARISON > F1=(L2/L3)×0.695×P；F2=(L1/L3)×0.695×P
- Evidence type: FORMULA + TABLE
- Evidence: LHA0480-P双压臂型适用公式F1=(L2/L3)×0.695×P、F2=(L1/L3)×0.695×P；F1、F2单位为kN，P单位为MPa，L1、L2、L3单位为mm。

## LHA-Q-0217

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA :: LHA1050

### Question

在相同P=2.5 MPa、L=120 mm条件下，分别按PDF公式计算LHA0650和LHA1050的夹紧力，并求后者与前者的比值。

### Standard Answer

使用公式或指定算术关系：F=P×(1-0.0009×L)/(0.7822+0.0010×L)；F=P×(1-0.0008×L)/(0.2495+0.0002×L) 代入：主体尺寸=105；主体尺寸1=065；主体尺寸2=105；供给压力=2.5 MPa；压板长度=120 mm。 Decimal完整精度计算：夹紧力1=2.471735757038350698293061405453336 kN；夹紧力2=8.263254113345521023765996343692870 kN；ratio_2_to_1=3.343097695542748460825866323443815。 按ROUND_HALF_UP显示：夹紧力1=2.472 kN；夹紧力2=8.263 kN；ratio_2_to_1=3.343。

### Scoring Standard

- P1 [20]: 第一个基础夹紧力夹紧力1数值为2.472
- P2 [5]: 第一个基础夹紧力夹紧力1单位为kN
- P3 [20]: 第二个基础夹紧力夹紧力2数值为8.263
- P4 [5]: 第二个基础夹紧力夹紧力2单位为kN
- P5 [15]: 使用派生关系夹紧力2/夹紧力1
- P6 [25]: 派生输出ratio_2_to_1数值为3.343
- P7 [10]: 派生输出ratio_2_to_1的单位属性为无量纲

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- 夹紧力1：相对误差 ±0.5%。
- 夹紧力2：相对误差 ±0.5%。
- ratio_2_to_1：相对误差 ±0.5%。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 10
- Printed page: 508
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > MODEL_SIZE_COMPARISON > F=P×(1-0.0009×L)/(0.7822+0.0010×L)；F=P×(1-0.0008×L)/(0.2495+0.0002×L)
- Evidence type: FORMULA + TABLE
- Evidence: LHA0650适用公式F=P×(1-0.0009×L)/(0.7822+0.0010×L)；LHA1050适用公式F=P×(1-0.0008×L)/(0.2495+0.0002×L)。F单位为kN，P单位为MPa，L单位为mm。

## LHA-Q-0221

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA1050

### Question

固定LHA1050压板长度L=200 mm，供给油压由1.5 MPa变为6.5 MPa。按PDF公式分别计算夹紧力，并求每增加1 MPa对应的夹紧力变化。

### Standard Answer

使用公式或指定算术关系：F=P×(1-0.0008×L)/(0.2495+0.0002×L) 代入：主体尺寸=105；供给压力1=1.5 MPa；供给压力2=6.5 MPa；压板长度=200 mm。 Decimal完整精度计算：夹紧力1=4.352331606217616580310880829015544 kN；夹紧力2=18.86010362694300518134715025906736 kN；每MPa夹紧力变化=2.901554404145077720207253886010364 kN/MPa。 按ROUND_HALF_UP显示：夹紧力1=4.352 kN；夹紧力2=18.860 kN；每MPa夹紧力变化=2.902 kN/MPa。

### Scoring Standard

- P1 [20]: 第一个基础夹紧力夹紧力1数值为4.352
- P2 [5]: 第一个基础夹紧力夹紧力1单位为kN
- P3 [20]: 第二个基础夹紧力夹紧力2数值为18.860
- P4 [5]: 第二个基础夹紧力夹紧力2单位为kN
- P5 [15]: 使用派生关系(夹紧力2-夹紧力1)/(P2-P1)
- P6 [25]: 派生输出每MPa夹紧力变化数值为2.902
- P7 [10]: 派生输出每MPa夹紧力变化的单位属性为kN/MPa

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- 夹紧力1：相对误差 ±0.5%。
- 夹紧力2：相对误差 ±0.5%。
- 每MPa夹紧力变化：相对误差 ±0.5%。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 10
- Printed page: 508
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > PRESSURE_SENSITIVITY > F=P×(1-0.0008×L)/(0.2495+0.0002×L)
- Evidence type: FORMULA + TABLE
- Evidence: LHA1050适用公式F=P×(1-0.0008×L)/(0.2495+0.0002×L)，其中F为夹紧力（kN）、P为供给油压（MPa）、L为压板长度（mm）。

## LHA-Q-0223

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0900

### Question

固定LHA0900供给油压P=5.5 MPa，将压板长度从100 mm增至250 mm。按PDF公式分别计算夹紧力，并求相对短压板夹紧力的下降百分比。

### Standard Answer

使用公式或指定算术关系：F=P×(1-0.0009×L)/(0.3547+0.0004×L) 代入：主体尺寸=090；供给压力=5.5 MPa；压板长度1=100 mm；压板长度2=250 mm。 Decimal完整精度计算：短压板夹紧力=12.68051684823916898910564986065366 kN；长压板夹紧力=9.374312733670552012315812623707939 kN；下降百分比=26.07310217822643597880017497347605 %。 按ROUND_HALF_UP显示：短压板夹紧力=12.681 kN；长压板夹紧力=9.374 kN；下降百分比=26.1 %。

### Scoring Standard

- P1 [20]: 第一个基础夹紧力短压板夹紧力数值为12.681
- P2 [5]: 第一个基础夹紧力短压板夹紧力单位为kN
- P3 [20]: 第二个基础夹紧力长压板夹紧力数值为9.374
- P4 [5]: 第二个基础夹紧力长压板夹紧力单位为kN
- P5 [15]: 使用派生关系(短压板夹紧力-长压板夹紧力)/短压板夹紧力×100%
- P6 [25]: 派生输出下降百分比数值为26.1
- P7 [10]: 派生输出下降百分比的单位属性为%

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- 短压板夹紧力：相对误差 ±0.5%。
- 长压板夹紧力：相对误差 ±0.5%。
- 下降百分比：精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 10
- Printed page: 508
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > ARM_LENGTH_SENSITIVITY > F=P×(1-0.0009×L)/(0.3547+0.0004×L)
- Evidence type: FORMULA + TABLE
- Evidence: LHA0900适用公式F=P×(1-0.0009×L)/(0.3547+0.0004×L)，其中F为夹紧力（kN）、P为供给油压（MPa）、L为压板长度（mm）。

## LHA-Q-0225

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

PDF夹紧力表给出LHA0650在P=5.0 MPa时最大压板长度为187 mm。若设计长度为170 mm，计算该长度占最大允许长度的百分比。

### Standard Answer

使用公式或指定算术关系：PDF表格值的题目指定算术关系 代入：主体尺寸=065；供给压力=5.0 MPa；压板长度=170 mm；最大压板长度=187.0 mm。 Decimal完整精度计算：长度占比=90.90909090909090909090909090909091 %。 按ROUND_HALF_UP显示：长度占比=90.9 %。

### Scoring Standard

- P1 [30]: 使用170/187×100%的占比关系
- P2 [50]: 长度占比数值为90.9
- P3 [20]: 长度占比使用百分比表示

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- N/A

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 10
- Printed page: 508
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > MAXIMUM_ARM_LENGTH_MARGIN > PDF表格值的题目指定算术关系
- Evidence type: FORMULA + TABLE
- Evidence: LHA夹紧力表：LHA0650在供给油压5 MPa时，最大压板长度L为187 mm。

## LHA-Q-0228

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0650

### Question

PDF规格表中LHA0650（选择无符号/A/F/P时）的全行程为20.0 mm、旋转行程为10.0 mm。计算两者差值。

### Standard Answer

使用公式或指定算术关系：PDF表格值的题目指定算术关系 代入：主体尺寸=065；full_stroke=20.0 mm；rotation_stroke=10.0 mm。 Decimal完整精度计算：行程差值=10.0 mm。 按ROUND_HALF_UP显示：行程差值=10.0 mm。

### Scoring Standard

- P1 [30]: 使用正确减法关系：全行程-旋转行程
- P2 [50]: 行程差值数值为10.0
- P3 [20]: 行程差值单位为mm

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- 数值须精确匹配，单位为 mm。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 506
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > TABLE_DERIVED_SPECIFICATION > PDF表格值的题目指定算术关系
- Evidence type: FORMULA + TABLE
- Evidence: LHA规格表：LHA0650在无符号、A、F或P选配时，全行程为20.0 mm，旋转行程为10.0 mm。

## LHA-Q-0230

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0900

### Question

LHA0900在压板长度L=250 mm时若要求夹紧力达到12.272 kN，反求所需压力并与PDF最高使用压力7.0 MPa比较，给出可行性结论。

### Standard Answer

使用公式或指定算术关系：F=P×(1-0.0009×L)/(0.3547+0.0004×L) 代入：主体尺寸=090；目标夹紧力=12.272 kN；压板长度=250 mm。 Decimal完整精度计算：所需压力=7.200101161290322580645161290322581 MPa；可行性结论为不可行。 按ROUND_HALF_UP显示：所需压力=7.200 MPa；可行性结论为不可行。

### Scoring Standard

- P1 [15]: 选择LHA0900原公式：F=P×(1-0.0009×L)/(0.3547+0.0004×L)
- P2 [20]: 正确变形为P=F×(b+dL)/(1-aL)
- P3 [10]: 正确代入题目给定的F和L
- P4 [30]: 所需压力数值为7.200
- P5 [10]: 所需压力单位为MPa
- P6 [15]: 可行性结论为不可行

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- 所需压力：相对误差 ±0.5%。
- feasible：精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 8、10
- Printed page: 506、508
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > BOUNDARY_FEASIBILITY > F=P×(1-0.0009×L)/(0.3547+0.0004×L)
- Evidence type: FORMULA + TABLE
- Evidence: LHA0900适用公式F=P×(1-0.0009×L)/(0.3547+0.0004×L)，其中F为夹紧力（kN）、P为供给油压（MPa）、L为压板长度（mm）；最高使用压力为7 MPa。

## LHA-Q-0231

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHA 油压复动旋转式夹紧器
- Model / Scope: LHA0360

### Question

对LHA0360在P=2.25 MPa、L=100 mm这一条件，请先从PDF能力曲线估读夹紧力，再用PDF公式计算同条件夹紧力，求两者绝对差值，并按±0.25 kN图表估读容差判断是否一致。

### Standard Answer

名义示例答案（不是动态差值的唯一合法答案）： 使用公式或指定算术关系：F=P×(1-0.0021×L)/(2.9379+0.0052×L) 代入：主体尺寸=036；供给压力=2.25 MPa；压板长度=100 mm。 Decimal完整精度计算：图表估读值=0.500 kN；公式计算值=0.5140403134850631886405043523525839 kN；绝对差值=0.0140403134850631886405043523525839 kN；一致性结论为一致。 按ROUND_HALF_UP显示：图表估读值=0.500 kN；公式计算值=0.514 kN；绝对差值=0.014 kN；一致性结论为一致。 评分时差值必须按回答者自身两个候选值动态计算，并与±0.250 kN比较。

### Scoring Standard

- P1 [20]: 曲线估读数值在允许范围内
- P2 [5]: 图表估读值单位为kN
- P3 [15]: 使用正确型号公式：F=P×(1-0.0021×L)/(2.9379+0.0052×L)
- P4 [20]: 公式计算值数值在0.514的±0.5%范围内
- P5 [5]: 公式计算值单位为kN
- P6 [10]: 使用绝对差值关系|图表估读值-公式计算值|
- P7 [10]: 绝对差值与候选两值的动态差值在0.01 kN内一致
- P8 [5]: 绝对差值单位为kN
- P9 [10]: 容差内或容差外结论与候选动态差值一致

### Accepted Variants

- 图表估读值可在 Tolerance 规定范围内变化；差值和一致性结论必须由回答者给出的图表值与公式值动态计算。

### Forbidden Errors

- 不得混用其他型号公式
- 不得遗漏单位
- 不得使用图表宽容差替代公式容差
- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较、反算或可行性结论。

### Tolerance

- 图表估读值：±0.25 kN。
- 公式计算值：相对误差 ±0.5%。
- 绝对差值：与回答者自身数值计算结果相差不超过 0.01 kN。
- within_chart_tolerance：精确匹配。

### Source

- PDF: LHA_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 507
- Section: 夹紧力与规格计算
- Local scope path: 夹紧力与规格计算 > CHART_FORMULA_CROSS_VALIDATION > F=P×(1-0.0021×L)/(2.9379+0.0052×L) > R6-TRUTH-0004
- Evidence type: CHART + FORMULA
- Evidence: LHA0360夹紧力能力曲线在L=100 mm、P=2.25 MPa时视觉估读F约0.5 kN；对应公式为F=P×(1-0.0021×L)/(2.9379+0.0052×L)，图表读数容差为±0.25 kN。
