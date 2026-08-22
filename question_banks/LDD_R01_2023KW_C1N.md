---
schema_version: will-ai-question-bank/v1
source_pdf: LDD_R01_2023KW_C1N.pdf
source_sha256: a3a4a51f350d73b263e50739578582b69fa9f4f42a69163fb9a8b07aa40f732e
source_pages: 36
question_bank_version: V1
product_scope: LDD
---

# LDD_R01_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LDD_R01_2023KW_C1N.pdf`
- SHA-256: `a3a4a51f350d73b263e50739578582b69fa9f4f42a69163fb9a8b07aa40f732e`
- 物理页数: 36
- Product: KOSMEK LDD 双动式油压支撑器
- 产品及对照印刷页: 959-960, 1091-1118
- 收录的通用参考印刷页: 1725-1730
- 来源证据原则: PDF 页面及其结构化表格、图表和文字为 Source Truth；OCR 仅可用于导航。

## 2. Scope

### 2.1 产品与文档范围

本题库覆盖 LDD 双动式油压支撑器的用途、产品特点、动作原理、型号表示、
规格、支撑力与接触力计算、特性曲线、外形与安装尺寸、设计与安装注意事项、
液压回路、空气传感器、维护，以及本 PDF 收录的通用液压参考内容。

销售地址、销售网络等非技术信息不作为产品能力题；相同表格中仅数值或型号不同、
但判定能力相同的内容采用代表性问题覆盖。

### 2.2 型号语法

基本型号由 `LDD`、主体尺寸、设计编号和可选后缀组成。主体尺寸为 `030`、`036`
或 `045`，本资料的设计编号为 `3`。柱塞弹簧力代码 `L` 表示弱弹簧，`H` 表示强弹簧；
`M` 表示带空气传感器连接，`Q` 表示液压上升长行程规格。组合后缀按资料顺序写为
`M-Q`，不得写为 `Q-M`。合法示例包括 `LDD0303-H`、`LDD0303-HM`、
`LDD0303-L`、`LDD0303-LM`、`LDD0303-Q` 和 `LDD0303-M-Q`。

### 2.3 来源覆盖索引

下表按物理页汇总实际问题覆盖。每道题的精确局部范围、证据类型和证据摘要见题目内 Source。

| 物理页 | 印刷页 | 局部范围 | 题目覆盖 |
|---|---|---|---|
| 1 | 959 | 产品概览 | `LDD-Q-0001` |
| 2 | 960 | 产品概览 | `LDD-Q-0002` |
| 3 | 1091 | 产品特点 | `LDD-Q-0003`-`LDD-Q-0005` |
| 4 | 1092 | 产品特点 | `LDD-Q-0006`-`LDD-Q-0007` |
| 5 | 1093 | 产品特点 | `LDD-Q-0008`-`LDD-Q-0011` |
| 6 | 1094 | 动作原理 | `LDD-Q-0012`-`LDD-Q-0014` |
| 7 | 1095 | 型号表示 | `LDD-Q-0015`-`LDD-Q-0024` |
| 8 | 1096 | 规格、计算公式 | `LDD-Q-0025`-`LDD-Q-0042`、`LDD-Q-0108`、`LDD-Q-0112`-`LDD-Q-0115`、`LDD-Q-0119`-`LDD-Q-0120` |
| 9 | 1097 | 能力曲线 | `LDD-Q-0046`-`LDD-Q-0047` |
| 10 | 1098 | 能力曲线 | `LDD-Q-0049` |
| 13 | 1101 | 外形尺寸 | `LDD-Q-0064`、`LDD-Q-0122` |
| 14 | 1102 | 外形尺寸、安装施工 | `LDD-Q-0050`-`LDD-Q-0052`、`LDD-Q-0062`、`LDD-Q-0121` |
| 15 | 1103 | 外形尺寸 | `LDD-Q-0122` |
| 16 | 1104 | 外形尺寸、安装施工 | `LDD-Q-0053`-`LDD-Q-0055`、`LDD-Q-0121` |
| 18 | 1106 | 外形尺寸、空气传感器 | `LDD-Q-0048`、`LDD-Q-0056`-`LDD-Q-0058`、`LDD-Q-0063`、`LDD-Q-0110` |
| 20 | 1108 | 外形尺寸 | `LDD-Q-0059`-`LDD-Q-0061`、`LDD-Q-0126` |
| 21 | 1109 | 空气传感器、计算公式 | `LDD-Q-0043`、`LDD-Q-0065`-`LDD-Q-0067`、`LDD-Q-0111`、`LDD-Q-0116`-`LDD-Q-0117` |
| 22 | 1110 | 空气传感器 | `LDD-Q-0068`-`LDD-Q-0072`、`LDD-Q-0123` |
| 23 | 1111 | 喷气清洁 | `LDD-Q-0073`-`LDD-Q-0076` |
| 24 | 1112 | 柱塞弹簧设计尺寸 | `LDD-Q-0077`-`LDD-Q-0078` |
| 25 | 1115 | 油压支撑器注意事项、注意事项、计算公式、设计注意事项 | `LDD-Q-0044`、`LDD-Q-0079`-`LDD-Q-0086`、`LDD-Q-0098`、`LDD-Q-0118`、`LDD-Q-0127` |
| 26 | 1116 | 注意事项、设计注意事项 | `LDD-Q-0045`、`LDD-Q-0087`-`LDD-Q-0089`、`LDD-Q-0109` |
| 27 | 1117 | 注意事项 | `LDD-Q-0090` |
| 28 | 1118 | 安装施工、安装施工方面的注意事项 | `LDD-Q-0091`-`LDD-Q-0093`、`LDD-Q-0099` |
| 29 | 1725 | 通用安装 | `LDD-Q-0094`-`LDD-Q-0097` |
| 31 | 1727 | 保养检查、操作注意事项 | `LDD-Q-0100`-`LDD-Q-0103` |
| 32 | 1728 | 质量保证 | `LDD-Q-0104`-`LDD-Q-0105` |
| 33 | 1729 | 标示更改 | `LDD-Q-0106` |
| 34 | 1730 | 标示更改 | `LDD-Q-0107` |

## 3. Question Statistics

- Total: 125
- FACT: 17
- SPEC_LOOKUP: 17
- MODEL: 10
- TABLE: 22
- CALCULATION: 15
- CHART: 4
- PROCEDURE: 9
- CAUTION: 31

## 4. Questions

## LDD-Q-0001

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD支撑器在手册中用于防止哪两类工件问题？

### Standard Answer

用于防止加工振动以及夹紧导致的工件变形。

### Scoring Standard

- P1 [50]: 支撑器用于防止加工振动。
- P2 [50]: 支撑器用于防止夹紧导致的工件变形。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 1
- Printed page: 959
- Section: 产品概览
- Local scope path: 产品概览 > 物理页 1, 印刷页 959
- Evidence type: TEXT
- Evidence: 支撑器用于防止加工振动；支撑器用于防止夹紧导致的工件变形。

## LDD-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列在支撑器系列表中的驱动方式、安装形式和使用压力范围是什么？

### Standard Answer

低压复动、外螺纹型，使用压力范围2.5～7MPa。

### Scoring Standard

- P1 [25]: LDD属于低压系列。
- P2 [25]: LDD采用复动驱动方式。
- P3 [25]: LDD采用外螺纹安装形式。
- P4 [25]: LDD使用压力范围为2.5～7MPa。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 2
- Printed page: 960
- Section: 产品概览
- Local scope path: 产品概览 > 物理页 2, 印刷页 960
- Evidence type: TEXT
- Evidence: LDD属于低压系列；LDD采用复动驱动方式；LDD采用外螺纹安装形式；LDD使用压力范围为2.5～7MPa。

## LDD-Q-0003

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD如何避免背压影响释放动作？

### Standard Answer

通过油压强制释放。

### Scoring Standard

- P1 [100]: 通过油压强制释放。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 3
- Printed page: 1091
- Section: 产品特点
- Local scope path: 产品特点 > 物理页 3, 印刷页 1091
- Evidence type: TEXT
- Evidence: 通过油压强制释放。

## LDD-Q-0004

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列的本体尺寸设计相对传统单动式支撑器有何特点？

### Standard Answer

尺寸同样紧凑。

### Scoring Standard

- P1 [100]: 尺寸同样紧凑。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 3
- Printed page: 1091
- Section: 产品特点
- Local scope path: 产品特点 > 物理页 3, 印刷页 1091
- Evidence type: TEXT
- Evidence: 尺寸同样紧凑。

## LDD-Q-0005

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列在柱塞行程方面提供哪两类标准化产品阵容？

### Standard Answer

标准行程型与行程加长型。

### Scoring Standard

- P1 [50]: LDD提供标准行程型。
- P2 [50]: LDD提供行程加长型。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 3
- Printed page: 1091
- Section: 产品特点
- Local scope path: 产品特点 > 物理页 3, 印刷页 1091
- Evidence type: TEXT
- Evidence: LDD提供标准行程型；LDD提供行程加长型。

## LDD-Q-0006

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD如何间接确认释放动作，相关器件是否内置？

### Standard Answer

可通过油压压力开关间接确认；压力开关需另行配置。

### Scoring Standard

- P1 [50]: LDD可通过油压压力开关间接确认释放动作。
- P2 [50]: 油压压力开关需另行配置。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 4
- Printed page: 1092
- Section: 产品特点
- Local scope path: 产品特点 > 物理页 4, 印刷页 1092
- Evidence type: TEXT
- Evidence: LDD可通过油压压力开关间接确认释放动作；油压压力开关需另行配置。

## LDD-Q-0007

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD释放油压的供给位置及方向适应性是什么？

### Standard Answer

从本体侧面供给，可应对全方位油压供给。

### Scoring Standard

- P1 [50]: 释放油压从LDD本体侧面供给。
- P2 [50]: 该供给布置可应对全方位油压供给。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 4
- Printed page: 1092
- Section: 产品特点
- Local scope path: 产品特点 > 物理页 4, 印刷页 1092
- Evidence type: TEXT
- Evidence: 释放油压从LDD本体侧面供给；该供给布置可应对全方位油压供给。

## LDD-Q-0008

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD通过什么结构与效应获得强大抱紧力？

### Standard Answer

采用筒夹方式并利用楔型效果。

### Scoring Standard

- P1 [100]: 采用筒夹方式并利用楔型效果。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 1093
- Section: 产品特点
- Local scope path: 产品特点 > 物理页 5, 印刷页 1093
- Evidence type: TEXT
- Evidence: 采用筒夹方式并利用楔型效果。

## LDD-Q-0009

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

在普通LDD的基本动作说明中，不考虑空气传感器或喷气清洁附加供气时，与工件接触的基本接触力由什么提供？

### Standard Answer

由柱塞弹簧力提供。

### Scoring Standard

- P1 [100]: 在不使用空气传感器或喷气清洁附加供气的基本动作条件下，接触力由柱塞弹簧力提供。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得声称该结论适用于启用空气传感器或喷气清洁供气后的全部LDD工况。
- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 1093
- Section: 产品特点
- Local scope path: 产品特点 > 物理页 5, 印刷页 1093
- Evidence type: TEXT
- Evidence: 在不使用空气传感器或喷气清洁附加供气的基本动作条件下，接触力由柱塞弹簧力提供。

## LDD-Q-0010

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD在一个油压回路中的动作顺序是什么？

### Standard Answer

柱塞上升→接触工件→锁定。

### Scoring Standard

- P1 [100]: 柱塞上升→接触工件→锁定。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 1093
- Section: 产品特点
- Local scope path: 产品特点 > 物理页 5, 印刷页 1093
- Evidence type: TEXT
- Evidence: 柱塞上升→接触工件→锁定。

## LDD-Q-0011

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD为应对切粉异物堆积和长时间放置造成的粘连，分别采用了什么结构？

### Standard Answer

采用防堆积形状的专用防尘密封圈，以及可解除长时间放置粘连现象的顶出机构。

### Scoring Standard

- P1 [50]: 切粉异物堆积对应防堆积形状的专用防尘密封圈。
- P2 [50]: 长时间放置造成的粘连对应顶出机构。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 1093
- Section: 产品特点
- Local scope path: 产品特点 > 物理页 5, 印刷页 1093
- Evidence type: TEXT
- Evidence: 专用防尘密封圈采用防止切粉异物等堆积的形状；顶出机构可解除长时间放置导致的粘连现象。

## LDD-Q-0012

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD处于释放状态时两路油压与柱塞位置是什么？

### Standard Answer

释放油压ON、抱紧油压OFF，柱塞下降。

### Scoring Standard

- P1 [34]: 释放状态下释放油压为ON。
- P2 [33]: 释放状态下抱紧油压为OFF。
- P3 [33]: 释放状态下柱塞下降。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 1094
- Section: 动作原理
- Local scope path: 动作原理 > 物理页 6, 印刷页 1094
- Evidence type: TEXT + PROCEDURE
- Evidence: 释放状态下释放油压为ON；释放状态下抱紧油压为OFF；释放状态下柱塞下降。

## LDD-Q-0013

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD从释放转入柱塞上升并接触工件时，两路油压如何切换？

### Standard Answer

释放油压OFF、抱紧油压ON；柱塞上升并接触工件后停止。

### Scoring Standard

- P1 [25]: 上升阶段释放油压切换为OFF。
- P2 [25]: 上升阶段抱紧油压切换为ON。
- P3 [25]: 柱塞随后上升。
- P4 [25]: 柱塞接触工件后停止。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 1094
- Section: 动作原理
- Local scope path: 动作原理 > 物理页 6, 印刷页 1094
- Evidence type: TEXT + PROCEDURE
- Evidence: 上升阶段释放油压切换为OFF；上升阶段抱紧油压切换为ON；柱塞随后上升；柱塞接触工件后停止。

## LDD-Q-0014

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD完成抱紧后，为什么从上面压柱塞也不会下降？

### Standard Answer

抱紧油压保持ON，楔形筒夹抱紧柱塞。

### Scoring Standard

- P1 [100]: 抱紧油压保持ON，楔形筒夹抱紧柱塞。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 6
- Printed page: 1094
- Section: 动作原理
- Local scope path: 动作原理 > 物理页 6, 印刷页 1094
- Evidence type: TEXT + PROCEDURE
- Evidence: 抱紧油压保持ON，楔形筒夹抱紧柱塞。

## LDD-Q-0015

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□

### Question

在LDD0303-□标准型型号族中，主体尺寸代码030表示什么φC尺寸和外径螺纹？

### Standard Answer

φC=30mm，外径螺纹M32×1.5。

### Scoring Standard

- P1 [50]: 主体尺寸代码030表示φC=30mm。
- P2 [50]: 主体尺寸代码030表示外径螺纹M32×1.5。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: 主体尺寸代码030表示φC=30mm；主体尺寸代码030表示外径螺纹M32×1.5。

## LDD-Q-0016

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-□

### Question

在LDD0363-□标准型型号族中，主体尺寸代码036表示什么φC尺寸和外径螺纹？

### Standard Answer

φC=36mm，外径螺纹M38×1.5。

### Scoring Standard

- P1 [50]: 主体尺寸代码036表示φC=36mm。
- P2 [50]: 主体尺寸代码036表示外径螺纹M38×1.5。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: 主体尺寸代码036表示φC=36mm；主体尺寸代码036表示外径螺纹M38×1.5。

## LDD-Q-0017

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0453-□

### Question

在LDD0453-□标准型型号族中，主体尺寸代码045表示什么φC尺寸和外径螺纹？

### Standard Answer

φC=45mm，外径螺纹M48×1.5。

### Scoring Standard

- P1 [50]: 主体尺寸代码045表示φC=45mm。
- P2 [50]: 主体尺寸代码045表示外径螺纹M48×1.5。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: 主体尺寸代码045表示φC=45mm；主体尺寸代码045表示外径螺纹M48×1.5。

## LDD-Q-0018

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

在LDD系列的型号表示中，设计编号3表示什么？

### Standard Answer

表示产品的版本信息。

### Scoring Standard

- P1 [100]: 表示产品的版本信息。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: 表示产品的版本信息。

## LDD-Q-0019

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

在LDD系列的型号表示中，柱塞弹簧代码L和H分别表示什么？

### Standard Answer

L为弱弹簧型，H为强弹簧型。

### Scoring Standard

- P1 [50]: 代码L表示弱弹簧型。
- P2 [50]: 代码H表示强弹簧型。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: 代码L表示弱弹簧型；代码H表示强弹簧型。

## LDD-Q-0020

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

在LDD系列的型号表示中，动作确认代码M表示什么？无符号又表示什么？

### Standard Answer

M表示空气传感器连接型；无符号表示无动作确认。

### Scoring Standard

- P1 [50]: 代码M表示空气传感器连接型。
- P2 [50]: 无符号表示无动作确认。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: 代码M表示空气传感器连接型；无符号表示无动作确认。

## LDD-Q-0021

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

在LDD系列的选配项中，无符号表示哪种型式？

### Standard Answer

油压上升标准型。

### Scoring Standard

- P1 [100]: 油压上升标准型。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: 油压上升标准型。

## LDD-Q-0022

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

在LDD系列的选配项中，Q表示哪种型式？

### Standard Answer

油压上升行程加长型。

### Scoring Standard

- P1 [100]: 油压上升行程加长型。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: 油压上升行程加长型。

## LDD-Q-0023

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

在LDD系列的型号表示中，需要油压上升、空气传感器连接并采用行程加长型时，选配组合应写成什么？

### Standard Answer

答案为：M-Q。

### Scoring Standard

- P1 [100]: 正确给出：M-Q。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: M-Q。

## LDD-Q-0024

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

型号写法LDD0363-Q-M是否符合PDF的正式组合规则？

### Standard Answer

不符合；应写作LDD0363-M-Q。

### Scoring Standard

- P1 [50]: LDD0363-Q-M不符合正式组合顺序。
- P2 [50]: 正式组合应写作LDD0363-M-Q。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号字段含义、字段顺序、合法组合或适用型号范围。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1095
- Section: 型号表示
- Local scope path: 型号表示 > 物理页 7, 印刷页 1095
- Evidence type: MODEL + TABLE
- Evidence: LDD0363-Q-M不符合正式组合顺序；正式组合应写作LDD0363-M-Q。

## LDD-Q-0025

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

供给油压7MPa时，标准型LDD0303-□、LDD0363-□和LDD0453-□的支撑力分别是多少？

### Standard Answer

依次为4.0kN、5.5kN、10.0kN。

### Scoring Standard

- P1 [34]: LDD0303为4.0kN。
- P2 [33]: LDD0363为5.5kN。
- P3 [33]: LDD0453为10.0kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 支撑力(油压7MPa时) > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303为4.0kN；LDD0363为5.5kN；LDD0453为10.0kN。

## LDD-Q-0026

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

标准型LDD0303-□、LDD0363-□、LDD0453-□的柱塞行程分别是多少？

### Standard Answer

依次为8mm、8mm、10mm。

### Scoring Standard

- P1 [34]: LDD0303为8mm。
- P2 [33]: LDD0363为8mm。
- P3 [33]: LDD0453为10mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 柱塞行程 > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303为8mm；LDD0363为8mm；LDD0453为10mm。

## LDD-Q-0027

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

标准型LDD0303-□、LDD0363-□、LDD0453-□的有效行程分别是多少？

### Standard Answer

依次为7.5mm、7.5mm、9.5mm。

### Scoring Standard

- P1 [34]: LDD0303为7.5mm。
- P2 [33]: LDD0363为7.5mm。
- P3 [33]: LDD0453为9.5mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 有效行程 > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303为7.5mm；LDD0363为7.5mm；LDD0453为9.5mm。

## LDD-Q-0028

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

标准型LDD0303-□、LDD0363-□、LDD0453-□上升・抱紧时的容量分别是多少？

### Standard Answer

依次为0.9cm³、1.3cm³、2.0cm³。

### Scoring Standard

- P1 [34]: LDD0303为0.9cm³。
- P2 [33]: LDD0363为1.3cm³。
- P3 [33]: LDD0453为2.0cm³。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 支撑器容量-上升抱紧 > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303为0.9cm³；LDD0363为1.3cm³；LDD0453为2.0cm³。

## LDD-Q-0029

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

标准型LDD0303-□、LDD0363-□、LDD0453-□下降时的容量分别是多少？

### Standard Answer

依次为0.2cm³、0.3cm³、0.4cm³。

### Scoring Standard

- P1 [34]: LDD0303为0.2cm³。
- P2 [33]: LDD0363为0.3cm³。
- P3 [33]: LDD0453为0.4cm³。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 支撑器容量-下降 > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303为0.2cm³；LDD0363为0.3cm³；LDD0453为0.4cm³。

## LDD-Q-0030

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

LDD0303-Q、LDD0363-Q、LDD0453-Q的柱塞行程分别是多少？

### Standard Answer

依次为16mm、16mm、20mm。

### Scoring Standard

- P1 [34]: LDD0303-Q为16mm。
- P2 [33]: LDD0363-Q为16mm。
- P3 [33]: LDD0453-Q为20mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 柱塞行程 > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303-Q为16mm；LDD0363-Q为16mm；LDD0453-Q为20mm。

## LDD-Q-0031

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

LDD0303-Q、LDD0363-Q、LDD0453-Q的有效行程分别是多少？

### Standard Answer

依次为15.5mm、15.5mm、19.5mm。

### Scoring Standard

- P1 [34]: LDD0303-Q为15.5mm。
- P2 [33]: LDD0363-Q为15.5mm。
- P3 [33]: LDD0453-Q为19.5mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 有效行程 > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303-Q为15.5mm；LDD0363-Q为15.5mm；LDD0453-Q为19.5mm。

## LDD-Q-0032

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

LDD0303-Q、LDD0363-Q、LDD0453-Q上升・抱紧时的容量分别是多少？

### Standard Answer

依次为1.3cm³、1.9cm³、2.8cm³。

### Scoring Standard

- P1 [34]: LDD0303-Q为1.3cm³。
- P2 [33]: LDD0363-Q为1.9cm³。
- P3 [33]: LDD0453-Q为2.8cm³。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 支撑器容量-上升抱紧 > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303-Q为1.3cm³；LDD0363-Q为1.9cm³；LDD0453-Q为2.8cm³。

## LDD-Q-0033

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

标准型LDD0303-□、LDD0363-□、LDD0453-□的质量分别是多少？

### Standard Answer

依次为0.30kg、0.30kg、0.85kg。

### Scoring Standard

- P1 [34]: LDD0303为0.30kg。
- P2 [33]: LDD0363为0.30kg。
- P3 [33]: LDD0453为0.85kg。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 质量 > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303为0.30kg；LDD0363为0.30kg；LDD0453为0.85kg。

## LDD-Q-0034

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

LDD0303-Q、LDD0363-Q、LDD0453-Q的质量分别是多少？

### Standard Answer

依次为0.35kg、0.35kg、0.90kg。

### Scoring Standard

- P1 [34]: LDD0303-Q为0.35kg。
- P2 [33]: LDD0363-Q为0.35kg。
- P3 [33]: LDD0453-Q为0.90kg。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD规格表 > 质量 > LDD0303 | LDD0363 | LDD0453 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: LDD0303-Q为0.35kg；LDD0363-Q为0.35kg；LDD0453-Q为0.90kg。

## LDD-Q-0035

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列共通的最高使用压力、最低动作压力和耐压分别是多少？

### Standard Answer

依次为7.0MPa、2.5MPa、10.5MPa。

### Scoring Standard

- P1 [34]: 最高使用压力为7.0MPa。
- P2 [33]: 最低动作压力为2.5MPa。
- P3 [33]: 耐压为10.5MPa。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: 最高使用压力为7.0MPa；最低动作压力为2.5MPa；耐压为10.5MPa。

## LDD-Q-0036

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列共通的允许使用温度范围是什么？

### Standard Answer

答案为：0～70℃。

### Scoring Standard

- P1 [100]: 正确给出：0～70℃。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: 0～70℃。

## LDD-Q-0037

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列共通规定使用什么流体？

### Standard Answer

相当于ISO粘度等级ISO-VG-32的一般作动油。

### Scoring Standard

- P1 [100]: 相当于ISO粘度等级ISO-VG-32的一般作动油。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > 物理页 8, 印刷页 1096
- Evidence type: TEXT
- Evidence: 相当于ISO粘度等级ISO-VG-32的一般作动油。

## LDD-Q-0038

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-L、LDD0363-H

### Question

LDD0363-L和LDD0363-H的柱塞弹簧设计力范围分别是多少？

### Standard Answer

弱弹簧4.7～7.8N；强弹簧6.2～11.0N。

### Scoring Standard

- P1 [50]: 该输出为4.7～7.8N。
- P2 [50]: 该输出为6.2～11.0N。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD标准型规格表 > 柱塞弹簧力-弱弹簧 | 柱塞弹簧力-强弹簧 > LDD0363 > 物理页 8, 印刷页 1096
- Evidence type: TABLE
- Evidence: 该输出为4.7～7.8N；该输出为6.2～11.0N。

## LDD-Q-0039

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0453-Q

### Question

LDD0453-Q的柱塞弹簧力范围是多少？

### Standard Answer

答案为：7.8～20.4N。

### Scoring Standard

- P1 [100]: 正确给出：7.8～20.4N。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD Q型规格表 > 柱塞弹簧力 > LDD0453-Q > 物理页 8, 印刷页 1096
- Evidence type: TABLE
- Evidence: 7.8～20.4N。

## LDD-Q-0040

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□

### Question

按PDF公式计算标准型LDD0303-□在供给油压5.0MPa时的支撑力，结果保留2位小数。

### Standard Answer

答案为：2.59kN。 计算依据：LDD0303支撑力：F=0.70×P-0.91。 输入为P=5.0，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [50]: 结果的计算数值为2.59。
- P2 [50]: 结果单位正确使用kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 8, 印刷页 1096
- Evidence type: FORMULA + TABLE
- Evidence: LDD0303支撑力：F=0.70*P-0.91。

## LDD-Q-0041

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-□

### Question

按PDF公式计算标准型LDD0363-□在供给油压6.2MPa时的支撑力，结果保留2位小数。

### Standard Answer

答案为：4.70kN。 计算依据：LDD0363支撑力：F=0.96×P-1.25。 输入为P=6.2，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [50]: 结果的计算数值为4.70。
- P2 [50]: 结果单位正确使用kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 8, 印刷页 1096
- Evidence type: FORMULA + TABLE
- Evidence: LDD0363支撑力：F=0.96*P-1.25。

## LDD-Q-0042

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0453-□

### Question

按PDF公式，标准型LDD0453-□要达到6.47kN支撑力，需要多少供给油压？保留2位小数，并回代核验。

### Standard Answer

需要5.00MPa；回代1.75×5.00-2.28=6.47kN。 计算依据：LDD0453反求供给压力：P=(F+2.28)/1.75。 输入为F=6.47，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [20]: 正确列出或变形反求关系。
- P2 [35]: 供给油压数值为5.00。
- P3 [10]: 供给油压单位为MPa。
- P4 [20]: 执行回代核验。
- P5 [15]: 回代结果为6.47kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 8, 印刷页 1096
- Evidence type: FORMULA + TABLE
- Evidence: LDD0453反求供给压力：P=(F+2.28)/1.75。

## LDD-Q-0043

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-HM

### Question

按PDF工件接触力公式计算LDD0363-HM在柱塞弹簧力8.6N、供气压力0.10MPa、U=15mm条件下的工件接触力，结果保留2位小数。

### Standard Answer

答案为：26.27N。 计算依据：空气传感/喷气清洁工件接触力：Fc=Fs+Pa×U^2×π/4。 输入为Fs=8.6、Pa=0.10、U=15，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [50]: 结果的计算数值为26.27。
- P2 [50]: 结果单位正确使用N。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 21
- Printed page: 1109
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 21, 印刷页 1109
- Evidence type: FORMULA + TABLE
- Evidence: 空气传感/喷气清洁工件接触力：Fc=Fs+Pa*U**2*PI/4。

## LDD-Q-0044

**Type: CALCULATION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列中，夹紧力为2.8kN且支撑器与夹紧器对向使用时，按PDF共通规则支撑力至少应为多少？

### Standard Answer

至少4.2kN。 计算依据：对向支撑力下限：Fs_min=1.5×Fc。 输入为Fc=2.8，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [50]: 结果的计算数值为4.2。
- P2 [50]: 结果单位正确使用kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 设计注意事项
- Local scope path: 设计注意事项 > 物理页 25, 印刷页 1115
- Evidence type: FORMULA + TABLE
- Evidence: 对向支撑力下限：Fs_min=1.5*Fc。

## LDD-Q-0045

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-L

### Question

对LDD0303-L，若柱塞最小弹簧力为3.6N，按PDF的30%规则与9.807换算，接触螺栓最大质量约为多少kg？保留2位小数。

### Standard Answer

约0.11kg。 计算依据：接触螺栓最大质量：m=Fspring_min×0.3/9.807。 输入为Fspring_min=3.6，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [50]: 结果的计算数值为0.11。
- P2 [50]: 结果单位正确使用kg。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 26
- Printed page: 1116
- Section: 设计注意事项
- Local scope path: 设计注意事项 > 物理页 26, 印刷页 1116
- Evidence type: FORMULA + TABLE
- Evidence: 接触螺栓最大质量：m=Fspring_min*0.3/9.807。

## LDD-Q-0046

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-□

### Question

从标准型支撑力曲线估读：LDD0363-□在供给油压5.25MPa时的支撑力约为多少？

### Standard Answer

约3.8kN。

### Scoring Standard

- P1 [75]: 曲线视觉估读值约为3.8kN。
- P2 [25]: 单位为kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得用公式计算值替代图表视觉读数，也不得混淆坐标轴、曲线系列或型号。

### Tolerance

- 图表读数允许误差：±0.25 kN。
- 容差依据：物理第9页支撑力曲线纵向主网格约2kN；5.25MPa位于5.0与5.5MPa之间，结合曲线线宽按约八分之一主网格设置。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 1097
- Section: 能力曲线
- Local scope path: 能力曲线 > LDD0363-□
- Evidence type: CHART
- Evidence: 标准型支撑力曲线中，LDD0363在5.25MPa处视觉估读约为3.8kN。

## LDD-Q-0047

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□

### Question

从7MPa条件下的标准型载荷/变位曲线估读：LDD0303-□承受1.0kN静载荷时变位量约为多少？

### Standard Answer

约8μm。

### Scoring Standard

- P1 [100]: 约8μm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得用公式计算值替代图表视觉读数，也不得混淆坐标轴、曲线系列或型号。

### Tolerance

- 图表读数允许误差：±2 μm。
- 容差依据：纵向主网格5μm，按小于半格并考虑曲线线宽设置

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 1097
- Section: 能力曲线
- Local scope path: 能力曲线 > LDD0303-□
- Evidence type: CHART
- Evidence: 约8μm。

## LDD-Q-0048

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-HM

### Question

从工件接触力曲线估读：LDD0363-HM在供给气压0.10MPa时的工件接触力约为多少？

### Standard Answer

约26N。

### Scoring Standard

- P1 [100]: 约26N。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得用公式计算值替代图表视觉读数，也不得混淆坐标轴、曲线系列或型号。

### Tolerance

- 图表读数允许误差：±2 N。
- 容差依据：纵向主网格5N，按约0.4格设置

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 18
- Printed page: 1106
- Section: 空气传感器
- Local scope path: 空气传感器 > LDD0363-HM > 印刷页 1106, LDD0363-HM 曲线，横坐标=0.10MPa
- Evidence type: CHART
- Evidence: 约26N。

## LDD-Q-0049

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□、LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

PDF对LDD0303-□、LDD0363-□、LDD0453-□标准型与对应LDD0303-Q、LDD0363-Q、LDD0453-Q行程加长型的变位程度如何比较？

### Standard Answer

LDD-Q行程加长型的变位程度更大。

### Scoring Standard

- P1 [100]: LDD-Q行程加长型的变位程度更大。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得用公式计算值替代图表视觉读数，也不得混淆坐标轴、曲线系列或型号。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 10
- Printed page: 1098
- Section: 能力曲线
- Local scope path: 能力曲线 > 物理页 10, 印刷页 1098
- Evidence type: CHART
- Evidence: LDD-Q行程加长型的变位程度更大。

## LDD-Q-0050

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

在LDD标准型外形及安装尺寸表中，LDD0303-□、LDD0363-□、LDD0453-□的A分别是多少（单位：mm）？

### Standard Answer

依次为79mm、74.5mm、89mm。

### Scoring Standard

- P1 [34]: LDD0303-□为79mm。
- P2 [33]: LDD0363-□为74.5mm。
- P3 [33]: LDD0453-□为89mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 14
- Printed page: 1102
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD标准型外形及安装尺寸表 > A > LDD0303-□ | LDD0363-□ | LDD0453-□ > 印刷页 1102, LDD标准型外形及安装尺寸表, row A, column LDD0303-□ | 印刷页 1102, LDD标准型外形及安装尺寸表, row A, column LDD0363-□ | 印刷页 1102, LDD标准型外形及安装尺寸表, row A, column LDD0453-□
- Evidence type: TABLE
- Evidence: LDD0303-□为79mm；LDD0363-□为74.5mm；LDD0453-□为89mm。

## LDD-Q-0051

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

在LDD标准型外形及安装尺寸表中，LDD0303-□、LDD0363-□、LDD0453-□的D分别是多少？

### Standard Answer

依次为M32×1.5、M38×1.5、M48×1.5。

### Scoring Standard

- P1 [34]: LDD0303-□为M32×1.5。
- P2 [33]: LDD0363-□为M38×1.5。
- P3 [33]: LDD0453-□为M48×1.5。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 14
- Printed page: 1102
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD标准型外形及安装尺寸表 > D > LDD0303-□ | LDD0363-□ | LDD0453-□ > 印刷页 1102, LDD标准型外形及安装尺寸表, row D, column LDD0303-□ | 印刷页 1102, LDD标准型外形及安装尺寸表, row D, column LDD0363-□ | 印刷页 1102, LDD标准型外形及安装尺寸表, row D, column LDD0453-□
- Evidence type: TABLE
- Evidence: LDD0303-□为M32×1.5；LDD0363-□为M38×1.5；LDD0453-□为M48×1.5。

## LDD-Q-0052

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

在LDD标准型外形及安装尺寸表中，LDD0303-□、LDD0363-□、LDD0453-□的本体推荐安装力矩分别是多少（单位：N·m）？

### Standard Answer

依次为50N·m、63N·m、80N·m。

### Scoring Standard

- P1 [34]: LDD0303-□为50N·m。
- P2 [33]: LDD0363-□为63N·m。
- P3 [33]: LDD0453-□为80N·m。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 14
- Printed page: 1102
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD标准型外形及安装尺寸表 > 本体推荐安装力矩 > LDD0303-□ | LDD0363-□ | LDD0453-□ > 印刷页 1102, LDD标准型外形及安装尺寸表, row 本体推荐安装力矩, column LDD0303-□ | 印刷页 1102, LDD标准型外形及安装尺寸表, row 本体推荐安装力矩, column LDD0363-□ | 印刷页 1102, LDD标准型外形及安装尺寸表, row 本体推荐安装力矩, column LDD0453-□
- Evidence type: TABLE
- Evidence: LDD0303-□为50N·m；LDD0363-□为63N·m；LDD0453-□为80N·m。

## LDD-Q-0053

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

在LDD-Q外形及安装尺寸表中，LDD0303-Q、LDD0363-Q、LDD0453-Q的A分别是多少（单位：mm）？

### Standard Answer

依次为95mm、89mm、106.5mm。

### Scoring Standard

- P1 [34]: LDD0303-Q为95mm。
- P2 [33]: LDD0363-Q为89mm。
- P3 [33]: LDD0453-Q为106.5mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 16
- Printed page: 1104
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD-Q外形及安装尺寸表 > A > LDD0303-Q | LDD0363-Q | LDD0453-Q > 印刷页 1104, LDD-Q外形及安装尺寸表, row A, column LDD0303-Q | 印刷页 1104, LDD-Q外形及安装尺寸表, row A, column LDD0363-Q | 印刷页 1104, LDD-Q外形及安装尺寸表, row A, column LDD0453-Q
- Evidence type: TABLE
- Evidence: LDD0303-Q为95mm；LDD0363-Q为89mm；LDD0453-Q为106.5mm。

## LDD-Q-0054

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

在LDD-Q外形及安装尺寸表中，LDD0303-Q、LDD0363-Q、LDD0453-Q的P分别是多少（单位：mm）？

### Standard Answer

依次为22mm、23mm、27mm。

### Scoring Standard

- P1 [34]: LDD0303-Q为22mm。
- P2 [33]: LDD0363-Q为23mm。
- P3 [33]: LDD0453-Q为27mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 16
- Printed page: 1104
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD-Q外形及安装尺寸表 > P > LDD0303-Q | LDD0363-Q | LDD0453-Q > 印刷页 1104, LDD-Q外形及安装尺寸表, row P, column LDD0303-Q | 印刷页 1104, LDD-Q外形及安装尺寸表, row P, column LDD0363-Q | 印刷页 1104, LDD-Q外形及安装尺寸表, row P, column LDD0453-Q
- Evidence type: TABLE
- Evidence: LDD0303-Q为22mm；LDD0363-Q为23mm；LDD0453-Q为27mm。

## LDD-Q-0055

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

在LDD-Q外形及安装尺寸表中，LDD0303-Q、LDD0363-Q、LDD0453-Q的CL分别是多少（单位：mm）？

### Standard Answer

依次为6mm、6mm、10mm。

### Scoring Standard

- P1 [34]: LDD0303-Q为6mm。
- P2 [33]: LDD0363-Q为6mm。
- P3 [33]: LDD0453-Q为10mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 16
- Printed page: 1104
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD-Q外形及安装尺寸表 > CL > LDD0303-Q | LDD0363-Q | LDD0453-Q > 物理页 16, row CL, three Q-model columns
- Evidence type: TABLE
- Evidence: LDD0303-Q为6mm；LDD0363-Q为6mm；LDD0453-Q为10mm。

## LDD-Q-0056

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M

### Question

在LDD-M外形及安装尺寸表中，LDD0303-□M、LDD0363-□M、LDD0453-□M的A分别是多少（单位：mm）？

### Standard Answer

依次为83mm、78.5mm、93mm。

### Scoring Standard

- P1 [34]: LDD0303-□M为83mm。
- P2 [33]: LDD0363-□M为78.5mm。
- P3 [33]: LDD0453-□M为93mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 18
- Printed page: 1106
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD-M外形及安装尺寸表 > A > LDD0303-□M | LDD0363-□M | LDD0453-□M > 印刷页 1106, LDD-M外形及安装尺寸表, row A, column LDD0303-□M | 印刷页 1106, LDD-M外形及安装尺寸表, row A, column LDD0363-□M | 印刷页 1106, LDD-M外形及安装尺寸表, row A, column LDD0453-□M
- Evidence type: TABLE
- Evidence: LDD0303-□M为83mm；LDD0363-□M为78.5mm；LDD0453-□M为93mm。

## LDD-Q-0057

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M

### Question

在LDD-M外形及安装尺寸表中，LDD0303-□M、LDD0363-□M、LDD0453-□M的销钉(直径×长度)分别是多少？

### Standard Answer

依次为φ1×5.8、φ1×7.8、φ1×7.8。

### Scoring Standard

- P1 [34]: LDD0303-□M为φ1×5.8。
- P2 [33]: LDD0363-□M为φ1×7.8。
- P3 [33]: LDD0453-□M为φ1×7.8。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 18
- Printed page: 1106
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD-M外形及安装尺寸表 > 销钉(直径×长度) > LDD0303-□M | LDD0363-□M | LDD0453-□M > 印刷页 1106, LDD-M外形及安装尺寸表, row 销钉(直径×长度), column LDD0303-□M | 印刷页 1106, LDD-M外形及安装尺寸表, row 销钉(直径×长度), column LDD0363-□M | 印刷页 1106, LDD-M外形及安装尺寸表, row 销钉(直径×长度), column LDD0453-□M
- Evidence type: TABLE
- Evidence: LDD0303-□M为φ1×5.8；LDD0363-□M为φ1×7.8；LDD0453-□M为φ1×7.8。

## LDD-Q-0058

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M

### Question

在LDD-M外形及安装尺寸表中，LDD0303-□M、LDD0363-□M、LDD0453-□M的传感器衬垫EC分别是多少（单位：mm）？

### Standard Answer

依次为7.5mm、8.5mm、8.5mm。

### Scoring Standard

- P1 [34]: LDD0303-□M为7.5mm。
- P2 [33]: LDD0363-□M为8.5mm。
- P3 [33]: LDD0453-□M为8.5mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 18
- Printed page: 1106
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD-M外形及安装尺寸表 > 传感器衬垫EC > LDD0303-□M | LDD0363-□M | LDD0453-□M > 印刷页 1106, LDD-M外形及安装尺寸表, row 传感器衬垫EC, column LDD0303-□M | 印刷页 1106, LDD-M外形及安装尺寸表, row 传感器衬垫EC, column LDD0363-□M | 印刷页 1106, LDD-M外形及安装尺寸表, row 传感器衬垫EC, column LDD0453-□M
- Evidence type: TABLE
- Evidence: LDD0303-□M为7.5mm；LDD0363-□M为8.5mm；LDD0453-□M为8.5mm。

## LDD-Q-0059

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

在LDD-M-Q外形及安装尺寸表中，LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q的A分别是多少（单位：mm）？

### Standard Answer

依次为99mm、93mm、110.5mm。

### Scoring Standard

- P1 [34]: LDD0303-M-Q为99mm。
- P2 [33]: LDD0363-M-Q为93mm。
- P3 [33]: LDD0453-M-Q为110.5mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 20
- Printed page: 1108
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD-M-Q外形及安装尺寸表 > A > LDD0303-M-Q | LDD0363-M-Q | LDD0453-M-Q > 印刷页 1108, LDD-M-Q外形及安装尺寸表, row A, column LDD0303-M-Q | 印刷页 1108, LDD-M-Q外形及安装尺寸表, row A, column LDD0363-M-Q | 印刷页 1108, LDD-M-Q外形及安装尺寸表, row A, column LDD0453-M-Q
- Evidence type: TABLE
- Evidence: LDD0303-M-Q为99mm；LDD0363-M-Q为93mm；LDD0453-M-Q为110.5mm。

## LDD-Q-0060

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

在LDD-M-Q外形及安装尺寸表中，LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q的BA分别是多少（单位：mm）？

### Standard Answer

依次为9.5mm、10.5mm、10.5mm。

### Scoring Standard

- P1 [34]: LDD0303-M-Q为9.5mm。
- P2 [33]: LDD0363-M-Q为10.5mm。
- P3 [33]: LDD0453-M-Q为10.5mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 20
- Printed page: 1108
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD-M-Q外形及安装尺寸表 > BA > LDD0303-M-Q | LDD0363-M-Q | LDD0453-M-Q > 物理页 20, row BA, three M-Q model columns
- Evidence type: TABLE
- Evidence: LDD0303-M-Q为9.5mm；LDD0363-M-Q为10.5mm；LDD0453-M-Q为10.5mm。

## LDD-Q-0061

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

在LDD-M-Q外形及安装尺寸表中，LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q的传感器衬垫EG分别是多少（单位：mm）？

### Standard Answer

依次为2.1mm、3.2mm、3.2mm。

### Scoring Standard

- P1 [34]: LDD0303-M-Q为2.1mm。
- P2 [33]: LDD0363-M-Q为3.2mm。
- P3 [33]: LDD0453-M-Q为3.2mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 20
- Printed page: 1108
- Section: 外形尺寸
- Local scope path: 外形尺寸 > LDD-M-Q外形及安装尺寸表 > 传感器衬垫EG > LDD0303-M-Q | LDD0363-M-Q | LDD0453-M-Q > 印刷页 1108, LDD-M-Q外形及安装尺寸表, row 传感器衬垫EG, column LDD0303-M-Q | 印刷页 1108, LDD-M-Q外形及安装尺寸表, row 传感器衬垫EG, column LDD0363-M-Q | 印刷页 1108, LDD-M-Q外形及安装尺寸表, row 传感器衬垫EG, column LDD0453-M-Q
- Evidence type: TABLE
- Evidence: LDD0303-M-Q为2.1mm；LDD0363-M-Q为3.2mm；LDD0453-M-Q为3.2mm。

## LDD-Q-0062

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-□

### Question

标准型LDD0363-□自制接触螺栓的EX螺纹、拧紧力矩和参考材质是什么？

### Standard Answer

EX为M10，拧紧力矩16N·m，参考材质S45C。

### Scoring Standard

- P1 [34]: LDD0363标准型自制接触螺栓EX螺纹为M10。
- P2 [33]: 其拧紧力矩为16N·m。
- P3 [33]: 参考材质为S45C。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 14
- Printed page: 1102
- Section: 外形尺寸
- Local scope path: 外形尺寸 > 接触螺栓设计制作尺寸表 > EX | 拧紧力矩 | 材质 > LDD0363-□ > 物理页 14, 印刷页 1102
- Evidence type: TABLE
- Evidence: LDD0363标准型自制接触螺栓EX螺纹为M10；其拧紧力矩为16N·m；参考材质为S45C。

## LDD-Q-0063

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M

### Question

在普通空气传感器连接型LDD0303-□M、LDD0363-□M和LDD0453-□M的接触螺栓套装表中，M8和M10接触螺栓的套装型号分别是什么？

### Standard Answer

M8为XLD-M8SP，M10为XLC-M10SP。

### Scoring Standard

- P1 [50]: M8空气传感接触螺栓套装型号为XLD-M8SP。
- P2 [50]: M10空气传感接触螺栓套装型号为XLC-M10SP。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 18
- Printed page: 1106
- Section: 外形尺寸
- Local scope path: 外形尺寸 > 接触螺栓适配设计尺寸表 > 接触螺栓套装 > M10 | M8 > 物理页 18, 印刷页 1106
- Evidence type: TABLE
- Evidence: M8空气传感接触螺栓套装型号为XLD-M8SP；M10空气传感接触螺栓套装型号为XLC-M10SP。

## LDD-Q-0064

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD产品页要求呼吸口满足哪两项基本防护要求？

### Standard Answer

向大气开放；防止冷却液、切屑粉尘等侵入支撑器内部。

### Scoring Standard

- P1 [50]: LDD呼吸口必须向大气开放。
- P2 [50]: LDD呼吸口应防止冷却液、切屑粉尘等侵入支撑器内部。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 1101
- Section: 外形尺寸
- Local scope path: 外形尺寸 > 物理页 13, 印刷页 1101
- Evidence type: TEXT
- Evidence: LDD呼吸口必须向大气开放；LDD呼吸口应防止冷却液、切屑粉尘等侵入支撑器内部。

## LDD-Q-0065

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M、LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

LDD空气传感器连接型，包括LDD0303-□M、LDD0363-□M、LDD0453-□M及对应LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q，通过检测什么量来确认柱塞动作？

### Standard Answer

检测P1与P2的压差。

### Scoring Standard

- P1 [100]: 检测P1与P2的压差。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 21
- Printed page: 1109
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 21, 印刷页 1109
- Evidence type: TEXT
- Evidence: 检测P1与P2的压差。

## LDD-Q-0066

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M、LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

LDD空气传感器连接型，包括LDD0303-□M、LDD0363-□M、LDD0453-□M及对应LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q，共通推荐供气压力范围是多少？

### Standard Answer

答案为：0.05～0.15MPa。

### Scoring Standard

- P1 [100]: 正确给出：0.05～0.15MPa。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 21
- Printed page: 1109
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 21, 印刷页 1109
- Evidence type: TEXT
- Evidence: 0.05～0.15MPa。

## LDD-Q-0067

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M、LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

LDD空气传感器连接型，包括LDD0303-□M、LDD0363-□M、LDD0453-□M及对应LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q，推荐的SMC和CKD空气传感器型号分别是什么？

### Standard Answer

答案为：SMC ISA3-G；CKD GPS3-E。

### Scoring Standard

- P1 [50]: 推荐的SMC空气传感器型号为ISA3-G。
- P2 [50]: 推荐的CKD空气传感器型号为GPS3-E。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 21
- Printed page: 1109
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 21, 印刷页 1109
- Evidence type: TEXT
- Evidence: 推荐的SMC空气传感器型号为ISA3-G；推荐的CKD空气传感器型号为GPS3-E。

## LDD-Q-0068

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M、LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

对于LDD空气传感器连接型，包括LDD0303-□M、LDD0363-□M、LDD0453-□M及对应LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q，一台空气传感器允许连接多少台LDD支撑器？连接台数过多会有什么后果？

### Standard Answer

1～4台；连接过多会导致检测动作不稳定。

### Scoring Standard

- P1 [50]: 1～4台。
- P2 [50]: 连接过多会导致检测动作不稳定。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 22
- Printed page: 1110
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 22, 空气传感器 local paragraph
- Evidence type: TEXT
- Evidence: 1～4台；空气传感器连接的支撑器台数过多会导致检测动作不稳定。

## LDD-Q-0069

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M、LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

LDD空气传感器连接型，包括LDD0303-□M、LDD0363-□M、LDD0453-□M及对应LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q，能否仅凭空气传感确认工件密着性？

### Standard Answer

不能；它用于确认柱塞动作，确认工件密着性还需对向夹紧装置。

### Scoring Standard

- P1 [34]: 空气传感规格不能单独确认工件密着性。
- P2 [33]: 空气传感规格用于确认支撑器内柱塞动作。
- P3 [33]: 确认工件密着性还需要对向夹紧装置。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 22
- Printed page: 1110
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 22, 印刷页 1110
- Evidence type: TEXT
- Evidence: 空气传感规格不能单独确认工件密着性；空气传感规格用于确认支撑器内柱塞动作；确认工件密着性还需要对向夹紧装置。

## LDD-Q-0070

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M、LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

LDD空气传感器连接型，包括LDD0303-□M、LDD0363-□M、LDD0453-□M及对应LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q，其柱塞动作时间、流量调整方式和投入使用前检查要求是什么？速度过快可能造成哪些后果？

### Standard Answer

将柱塞动作时间调整至约0.5～1秒，使用带单向阀的流量调整阀（进油节流），投入使用前确认柱塞与工件之间无间隙。速度过快可能发生反弹、在柱塞与工件之间形成间隙，严重时导致内部零部件破损。

### Scoring Standard

- P1 [17]: 柱塞动作时间调整至约0.5～1秒。
- P2 [17]: 使用带单向阀的流量调整阀（进油节流）。
- P3 [17]: 投入使用前确认柱塞与工件之间无间隙。
- P4 [17]: 速度过快可能发生反弹。
- P5 [16]: 速度过快可能在柱塞与工件之间形成间隙。
- P6 [16]: 严重时可能导致内部零部件破损。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 22
- Printed page: 1110
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 22, 空气传感器 local paragraph
- Evidence type: TEXT
- Evidence: 柱塞动作时间应调整至约0.5～1秒；应使用带单向阀的流量调整阀（进油节流）；投入使用前应确认柱塞与工件之间无间隙；柱塞上升速度过快时，接触工件可能发生反弹；柱塞上升速度过快可能在柱塞与工件之间产生间隙；柱塞上升速度过快严重时可能导致内部零部件破损。

## LDD-Q-0071

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M、LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

使用LDD空气传感器连接型，包括LDD0303-□M、LDD0363-□M、LDD0453-□M及对应LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q时，对传感器呼吸口有什么供气要求？如果切断气压使用可能造成什么后果？

### Standard Answer

保持常时供气。切断气压时，冷却液或切削屑可能从检测部侵入支撑器内部，并可能导致支撑器动作不良或空气传感器破损。

### Scoring Standard

- P1 [25]: 保持常时供气。
- P2 [25]: 切断气压时冷却液或切削屑可能从检测部侵入支撑器内部。
- P3 [25]: 可能导致支撑器动作不良。
- P4 [25]: 可能导致空气传感器破损。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 22
- Printed page: 1110
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 22, 空气传感器 local paragraph
- Evidence type: TEXT
- Evidence: 保持常时供气；切断传感器呼吸口气压使用时，冷却液或切削屑可能从检测部侵入支撑器内部；切断传感器呼吸口气压使用可能导致支撑器动作不良；切断传感器呼吸口气压使用可能导致空气传感器破损。

## LDD-Q-0072

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□、LDD0303-□M、LDD0363-□M、LDD0453-□M

### Question

只把LDD0303-□、LDD0363-□或LDD0453-□标准型的接触螺栓换成空气传感器专用型，能否作为对应的LDD0303-□M、LDD0363-□M或LDD0453-□M空气传感器连接型使用？

### Standard Answer

不能；还需更换内部零部件。

### Scoring Standard

- P1 [50]: 不能。
- P2 [50]: 还需更换内部零部件。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 22
- Printed page: 1110
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 22, 印刷页 1110
- Evidence type: TEXT
- Evidence: 不能；还需更换内部零部件。

## LDD-Q-0073

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD在恶劣环境下如何增设喷气清洁功能？

### Standard Answer

在呼吸口按图示施工回路。

### Scoring Standard

- P1 [50]: 防尘密封圈部启开压力约为0.1MPa。
- P2 [50]: 供气压力过低时空气可能无法喷出。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 23
- Printed page: 1111
- Section: 喷气清洁
- Local scope path: 喷气清洁 > 物理页 23, 印刷页 1111
- Evidence type: TEXT
- Evidence: 防尘密封圈部启开压力约为0.1MPa；供气压力过低时空气可能无法喷出。

## LDD-Q-0074

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列喷气清洁功能的共通推荐供气压力范围是多少？

### Standard Answer

答案为：0.2～0.3MPa。

### Scoring Standard

- P1 [100]: 正确给出：0.2～0.3MPa。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 23
- Printed page: 1111
- Section: 喷气清洁
- Local scope path: 喷气清洁 > 物理页 23, 印刷页 1111
- Evidence type: TEXT
- Evidence: 0.2～0.3MPa。

## LDD-Q-0075

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

对LDD系列常时保持喷气清洁供气时，使用油压至少应为多少？

### Standard Answer

2.5MPa以上。

### Scoring Standard

- P1 [100]: 2.5MPa以上。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 23
- Printed page: 1111
- Section: 喷气清洁
- Local scope path: 喷气清洁 > 物理页 23, 印刷页 1111
- Evidence type: TEXT
- Evidence: 2.5MPa以上。

## LDD-Q-0076

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列喷气清洁防尘密封圈部的启开压力约为多少？供气过低会怎样？

### Standard Answer

约0.1MPa；空气可能无法喷出。

### Scoring Standard

- P1 [50]: 约0.1MPa。
- P2 [50]: 空气可能无法喷出。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 23
- Printed page: 1111
- Section: 喷气清洁
- Local scope path: 喷气清洁 > 物理页 23, 印刷页 1111
- Evidence type: TEXT
- Evidence: 约0.1MPa；空气可能无法喷出。

## LDD-Q-0077

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

标准型LDD0303-□、LDD0363-□、LDD0453-□的FF/FG尺寸分别是多少？

### Standard Answer

答案为：LDD0303：24.6/16.6mm；LDD0363：17.6/9.6mm；LDD0453：19.6/9.6mm。

### Scoring Standard

- P1 [34]: 正确给出：LDD0303：24.6/16.6mm。
- P2 [33]: 正确给出：LDD0363：17.6/9.6mm。
- P3 [33]: 正确给出：LDD0453：19.6/9.6mm。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 24
- Printed page: 1112
- Section: 柱塞弹簧设计尺寸
- Local scope path: 柱塞弹簧设计尺寸 > 柱塞弹簧设计尺寸表 > FF/FG > LDD0303-□ | LDD0363-□ | LDD0453-□ > 物理页 24, 印刷页 1112
- Evidence type: TABLE
- Evidence: LDD0303：24.6/16.6mm；LDD0363：17.6/9.6mm；LDD0453：19.6/9.6mm。

## LDD-Q-0078

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

为LDD系列自行设计柱塞弹簧时，FF与FG分别控制什么？

### Standard Answer

设定长度为FF；完全压缩后长度为FG以下。

### Scoring Standard

- P1 [50]: 弹簧设定长度应为FF尺寸。
- P2 [50]: 弹簧完全压缩后的长度应为FG尺寸以下。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 24
- Printed page: 1112
- Section: 柱塞弹簧设计尺寸
- Local scope path: 柱塞弹簧设计尺寸 > 物理页 24, 印刷页 1112
- Evidence type: TEXT
- Evidence: 弹簧设定长度应为FF尺寸；弹簧完全压缩后的长度应为FG尺寸以下。

## LDD-Q-0079

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

轻型工件使用多个LDD支撑器时，为何可能需要临时固定？

### Standard Answer

柱塞弹簧力可能超过工件重量并顶起工件。

### Scoring Standard

- P1 [100]: 柱塞弹簧力可能超过工件重量并顶起工件。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 25, 印刷页 1115
- Evidence type: TEXT
- Evidence: 柱塞弹簧力可能超过工件重量并顶起工件。

## LDD-Q-0080

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD能否在未安装接触螺栓时投入使用？为什么？

### Standard Answer

不能；接触螺栓用于固定柱塞弹簧，否则柱塞无法上升。

### Scoring Standard

- P1 [34]: LDD不能在未安装接触螺栓时投入使用。
- P2 [33]: 接触螺栓用于固定柱塞弹簧。
- P3 [33]: 未固定柱塞弹簧时柱塞无法上升。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 25, 印刷页 1115
- Evidence type: TEXT
- Evidence: LDD不能在未安装接触螺栓时投入使用；接触螺栓用于固定柱塞弹簧；未固定柱塞弹簧时柱塞无法上升。

## LDD-Q-0081

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD接触螺栓上的O形密封圈是否必须安装？漏装可能导致什么？

### Standard Answer

必须；漏装可能使异物侵入并导致动作不良。

### Scoring Standard

- P1 [34]: 接触螺栓必须安装O形密封圈。
- P2 [33]: 漏装时异物可能侵入。
- P3 [33]: 异物侵入可能导致动作不良。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 25, 印刷页 1115
- Evidence type: TEXT
- Evidence: 接触螺栓必须安装O形密封圈；接触螺栓漏装O形密封圈时，冷却液等异物会侵入夹紧器内部；异物侵入可能导致动作不良。

## LDD-Q-0082

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD用于焊接夹具时应保护哪个部位，避免什么问题？

### Standard Answer

保护柱塞表面，避免喷溅导致滑动不良。

### Scoring Standard

- P1 [50]: 焊接夹具使用时应保护柱塞表面。
- P2 [50]: 保护目的是避免喷溅导致柱塞滑动不良。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 25, 印刷页 1115
- Evidence type: TEXT
- Evidence: 焊接夹具使用时应保护柱塞表面；保护目的是避免喷溅导致柱塞滑动不良。

## LDD-Q-0083

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

是否允许高压清洗液直接冲击LDD柱塞？

### Standard Answer

不允许；可能侵入内部或损坏机器。

### Scoring Standard

- P1 [34]: 不允许高压清洗液直接冲击柱塞。
- P2 [33]: 直接冲击可能使清洗液侵入内部。
- P3 [33]: 直接冲击可能造成机器损坏。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 25, 印刷页 1115
- Evidence type: TEXT
- Evidence: 不允许高压清洗液直接冲击柱塞；直接冲击可能使清洗液侵入内部；直接冲击可能造成机器损坏。

## LDD-Q-0084

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

车床或高速转台产生离心力时，LDD系列应保持什么状态？

### Standard Answer

保持锁紧状态。

### Scoring Standard

- P1 [100]: 保持锁紧状态。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 25, 印刷页 1115
- Evidence type: TEXT
- Evidence: 保持锁紧状态。

## LDD-Q-0085

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列标准全行程动作时间及推荐流量控制方式是什么？

### Standard Answer

约0.5～1秒；使用带单向阀的流量调整阀进行进油节流。

### Scoring Standard

- P1 [34]: 标准全行程动作时间约为0.5～1秒。
- P2 [33]: 应使用带单向阀的流量调整阀。
- P3 [33]: LDD速度控制采用进油节流。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 25, 印刷页 1115
- Evidence type: TEXT
- Evidence: 标准全行程动作时间约为0.5～1秒；应使用带单向阀的流量调整阀；LDD速度控制采用进油节流。

## LDD-Q-0086

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列使用的流量调整阀，其启开压力上限是多少？过高会怎样？

### Standard Answer

0.1MPa以下；过高会使释放时柱塞无法复位。

### Scoring Standard

- P1 [50]: 流量调整阀启开压力应为0.1MPa以下。
- P2 [50]: 启开压力过高可能使释放时柱塞无法复位。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 25, 印刷页 1115
- Evidence type: TEXT
- Evidence: 流量调整阀启开压力应为0.1MPa以下；启开压力过高可能使释放时柱塞无法复位。

## LDD-Q-0087

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列承受偏心载荷或分力会带来什么后果？

### Standard Answer

变位量增加；载荷过大时可能损坏内部零部件。

### Scoring Standard

- P1 [50]: 偏心载荷或分力会增加变位量。
- P2 [50]: 载荷过大时可能损坏内部零部件。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 26
- Printed page: 1116
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 26, 印刷页 1116
- Evidence type: TEXT
- Evidence: 偏心载荷或分力会增加变位量；载荷过大时可能损坏内部零部件。

## LDD-Q-0088

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列接触螺栓重量应控制在柱塞弹簧力的多少以下？

### Standard Answer

30%以下。

### Scoring Standard

- P1 [100]: 30%以下。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 26
- Printed page: 1116
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 26, 印刷页 1116
- Evidence type: TEXT
- Evidence: 30%以下。

## LDD-Q-0089

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列的自制接触螺栓若螺纹尺寸不匹配，会有什么影响？

### Standard Answer

会改变弹簧力和有效行程，并可能导致动作不良或损坏。

### Scoring Standard

- P1 [25]: 接触螺栓螺纹尺寸不匹配会改变弹簧力。
- P2 [25]: 螺纹尺寸不匹配会改变有效行程。
- P3 [25]: 螺纹尺寸不匹配可能导致动作不良。
- P4 [25]: 螺纹尺寸不匹配可能造成损坏。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 26
- Printed page: 1116
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 26, 印刷页 1116
- Evidence type: TEXT
- Evidence: 接触螺栓螺纹尺寸不匹配会改变弹簧力；螺纹尺寸不匹配会改变有效行程；螺纹尺寸不匹配可能导致动作不良；螺纹尺寸不匹配可能造成损坏。

## LDD-Q-0090

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD外螺纹型安装时，本体底面必须满足什么要求？

### Standard Answer

与安装孔底面水平密接，并由底面承受载荷。

### Scoring Standard

- P1 [50]: LDD本体底面应与安装孔底面水平密接。
- P2 [50]: 安装载荷应由本体底面承受。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 27
- Printed page: 1117
- Section: 注意事项
- Local scope path: 注意事项 > 物理页 27, 印刷页 1117
- Evidence type: TEXT
- Evidence: LDD本体底面应与安装孔底面水平密接；安装载荷应由本体底面承受。

## LDD-Q-0091

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

标准型LDD0303-□、LDD0363-□、LDD0453-□本体的螺纹尺寸和紧固力矩分别是什么？

### Standard Answer

依次为M32×1.5/50N·m、M38×1.5/63N·m、M48×1.5/80N·m。

### Scoring Standard

- P1 [17]: LDD0303本体螺纹为M32×1.5。
- P2 [17]: LDD0303本体紧固力矩为50N·m。
- P3 [17]: LDD0363本体螺纹为M38×1.5。
- P4 [17]: LDD0363本体紧固力矩为63N·m。
- P5 [16]: LDD0453本体螺纹为M48×1.5。
- P6 [16]: LDD0453本体紧固力矩为80N·m。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 28
- Printed page: 1118
- Section: 安装施工
- Local scope path: 安装施工 > 螺纹连接型本体安装力矩表 > 本体外螺纹 | 紧固力矩 > LDD0303 | LDD0363 | LDD0453 > 物理页 28, 印刷页 1118
- Evidence type: TABLE
- Evidence: LDD0303本体螺纹为M32×1.5；LDD0303本体紧固力矩为50N·m；LDD0363本体螺纹为M38×1.5；LDD0363本体紧固力矩为63N·m；LDD0453本体螺纹为M48×1.5；LDD0453本体紧固力矩为80N·m。

## LDD-Q-0092

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

标准型LDD0303-□、LDD0363-□、LDD0453-□接触螺栓的顶端螺纹与紧固力矩分别是什么？

### Standard Answer

依次为M8×1.25/10N·m、M10×1.5/16N·m、M10×1.5/16N·m。

### Scoring Standard

- P1 [17]: LDD0303接触螺栓顶端螺纹为M8×1.25。
- P2 [17]: LDD0303接触螺栓紧固力矩为10N·m。
- P3 [17]: LDD0363接触螺栓顶端螺纹为M10×1.5。
- P4 [17]: LDD0363接触螺栓紧固力矩为16N·m。
- P5 [16]: LDD0453接触螺栓顶端螺纹为M10×1.5。
- P6 [16]: LDD0453接触螺栓紧固力矩为16N·m。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 28
- Printed page: 1118
- Section: 安装施工
- Local scope path: 安装施工 > 接触螺栓紧固力矩表 > 紧固力矩 | 顶端螺纹 > LDD0303 | LDD0363 | LDD0453 > 物理页 28, 印刷页 1118
- Evidence type: TABLE
- Evidence: LDD0303接触螺栓顶端螺纹为M8×1.25；LDD0303接触螺栓紧固力矩为10N·m；LDD0363接触螺栓顶端螺纹为M10×1.5；LDD0363接触螺栓紧固力矩为16N·m；LDD0453接触螺栓顶端螺纹为M10×1.5；LDD0453接触螺栓紧固力矩为16N·m。

## LDD-Q-0093

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

安装LDD底面密封用O形密封圈前应涂什么？不涂可能怎样？

### Standard Answer

涂适量甘油；不涂可能导致O形密封圈扭曲或缺损。

### Scoring Standard

- P1 [50]: 安装底面密封O形密封圈前应涂适量甘油。
- P2 [50]: 未涂甘油可能导致O形密封圈扭曲或缺损。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 28
- Printed page: 1118
- Section: 安装施工
- Local scope path: 安装施工 > 物理页 28, 印刷页 1118
- Evidence type: TEXT
- Evidence: 安装底面密封O形密封圈前应涂适量甘油；未涂甘油可能导致O形密封圈扭曲或缺损。

## LDD-Q-0094

**Type: SPEC_LOOKUP**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 通用安装

### Question

根据《LDD_R01_2023KW_C1N.pdf》的液压系列通用事项，LDD适用哪一ISO粘度等级的液压油？

### Standard Answer

答案为：ISO-VG-32。

### Scoring Standard

- P1 [100]: 正确给出：ISO-VG-32。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆型号、规格项目、数值或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 29
- Printed page: 1725
- Section: 通用安装
- Local scope path: 通用安装 > 液压油一览表 > ISO粘度等级 > 通用 > 物理页 29, 印刷页 1725
- Evidence type: TEXT
- Evidence: ISO-VG-32。

## LDD-Q-0095

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 通用安装

### Question

根据《LDD_R01_2023KW_C1N.pdf》的液压系列通用安装事项，LDD液压配管投入使用前，配管、管接头和配件油孔应如何处理？回路异物或切削屑可能造成什么后果？

### Standard Answer

必须彻底清洁干净；异物或切削屑可能导致漏油或动作不良。

### Scoring Standard

- P1 [50]: 配管等投入使用前必须彻底清洁干净。
- P2 [50]: 回路异物或切削屑可能导致漏油或动作不良。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 29
- Printed page: 1725
- Section: 通用安装
- Local scope path: 通用安装 > 物理页 29, 通用安装 local paragraph
- Evidence type: TEXT + PROCEDURE
- Evidence: 必须彻底清洁干净；回路中的异物或切削屑等会导致漏油或动作不良。

## LDD-Q-0096

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 通用安装

### Question

根据《LDD_R01_2023KW_C1N.pdf》的液压系列通用安装事项，为LDD液压配管接头缠绕密封胶带时，应从接头顶部留出多少个螺纹牙？残留在回路内的胶带头可能造成什么后果？

### Standard Answer

留出1～2个螺纹牙；残留胶带头可能导致漏油或动作不正常。

### Scoring Standard

- P1 [50]: 留出1～2个螺纹牙。
- P2 [50]: 残留胶带头可能导致漏油或动作不正常。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 29
- Printed page: 1725
- Section: 通用安装
- Local scope path: 通用安装 > 物理页 29, 通用安装 local paragraph
- Evidence type: TEXT + PROCEDURE
- Evidence: 1～2个螺纹牙；残留在回路内的密封胶带头会导致漏油或动作不正常。

## LDD-Q-0097

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 通用安装

### Question

根据《LDD_R01_2023KW_C1N.pdf》的液压系列通用安装事项，按顺序列出LDD液压回路排气的五个步骤。

### Standard Answer

1)供油压力调到2MPa以下；2)最近接头螺母松一圈；3)摇动配管排出含气液压油；4)排净后拧紧螺母；5)优先在最上端及最末端排气，板式配管在最上端设排气阀。

### Scoring Standard

- P1 [20]: 排气前将供油压力调至2MPa以下。
- P2 [20]: 将最近的配管接头螺母再旋松一圈。
- P3 [20]: 摇动配管排出混入空气的液压油。
- P4 [20]: 空气排净后拧紧接头螺母。
- P5 [20]: 优先在回路最上端及最末端排气，板式配管在最上端设置排气阀。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 29
- Printed page: 1725
- Section: 通用安装
- Local scope path: 通用安装 > 物理页 29, 印刷页 1725
- Evidence type: TEXT + PROCEDURE
- Evidence: 排气前将供油压力调至2MPa以下；将最近的配管接头螺母再旋松一圈；摇动配管排出混入空气的液压油；空气排净后拧紧接头螺母；优先在回路最上端及最末端排气，板式配管在最上端设置排气阀。

## LDD-Q-0098

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD呼吸口应采用什么配管方式，并移至什么位置进行呼吸？

### Standard Answer

采用外配管方式，并移至不受切粉和冷却液影响的位置。

### Scoring Standard

- P1 [50]: LDD呼吸口应采用外配管方式。
- P2 [50]: LDD呼吸位置应移至不受切粉和冷却液影响的位置。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 油压支撑器注意事项
- Local scope path: 油压支撑器注意事项
- Evidence type: TEXT
- Evidence: LDD呼吸口应采用外配管方式；LDD呼吸位置应移至不受切粉和冷却液影响的位置。

## LDD-Q-0099

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

按PDF说明，更换LDD接触螺栓时，拆卸和安装分别要执行哪些关键要求？

### Standard Answer

拆卸时注意柱塞弹簧弹落；安装时用扳手固定柱塞顶端二面巾，防止柱塞转动，并按规定力矩紧固。

### Scoring Standard

- P1 [25]: 卸下接触螺栓时应防止柱塞弹簧弹落。
- P2 [25]: 安装时应用扳手固定柱塞顶端二面巾。
- P3 [25]: 固定二面巾是为了防止柱塞转动。
- P4 [25]: 接触螺栓应按规定力矩紧固。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 28
- Printed page: 1118
- Section: 安装施工方面的注意事项
- Local scope path: 安装施工方面的注意事项 > 物理页 28, 接触螺栓的更换
- Evidence type: TEXT + PROCEDURE
- Evidence: 卸下接触螺栓时应防止柱塞弹簧弹落；安装时应用扳手固定柱塞顶端二面巾；固定二面巾是为了防止柱塞转动；接触螺栓应按规定力矩紧固。

## LDD-Q-0100

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 操作注意事项

### Question

根据《LDD_R01_2023KW_C1N.pdf》的液压/气动装置通用操作注意事项，对LDD及相关液压/气动装置应由什么人员操作和维护？

### Standard Answer

具备丰富知识和经验的员工。

### Scoring Standard

- P1 [100]: 具备丰富知识和经验的员工。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 31
- Printed page: 1727
- Section: 操作注意事项
- Local scope path: 操作注意事项 > 物理页 31, 印刷页 1727
- Evidence type: TEXT
- Evidence: 具备丰富知识和经验的员工。

## LDD-Q-0101

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 操作注意事项

### Question

根据《LDD_R01_2023KW_C1N.pdf》的液压系列通用操作注意事项，拆卸LDD及相关液压装置前必须完成哪些安全条件？

### Standard Answer

采取防坠落和防误动作措施；切断压力源与电源；确认回路压力为零。

### Scoring Standard

- P1 [25]: 拆卸前应采取防坠落措施。
- P2 [25]: 拆卸前应采取防误动作措施。
- P3 [25]: 拆卸前应切断压力源和电源。
- P4 [25]: 拆卸前应确认回路压力为零。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 31
- Printed page: 1727
- Section: 操作注意事项
- Local scope path: 操作注意事项 > 物理页 31, 印刷页 1727
- Evidence type: TEXT
- Evidence: 拆卸前应采取防坠落措施；拆卸前应采取防误动作措施；拆卸前应切断压力源和电源；拆卸前应确认回路压力为零。

## LDD-Q-0102

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 保养检查

### Question

根据《LDD_R01_2023KW_C1N.pdf》的保养检查通用事项，为什么要定期清扫LDD柱塞周围？

### Standard Answer

污物会损伤密封材料，并导致动作不正常或漏油。

### Scoring Standard

- P1 [34]: 应定期清扫柱塞周围。
- P2 [33]: 污物会损伤密封材料。
- P3 [33]: 污物可能导致动作不正常或漏油。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 31
- Printed page: 1727
- Section: 保养检查
- Local scope path: 保养检查 > 物理页 31, 印刷页 1727
- Evidence type: TEXT + PROCEDURE
- Evidence: 应定期清扫柱塞周围；污物会损伤密封材料；污物可能导致动作不正常或漏油。

## LDD-Q-0103

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 保养检查

### Question

根据《LDD_R01_2023KW_C1N.pdf》的保养检查通用事项，应对LDD定期检查哪四类状态？

### Standard Answer

松动、液压油老化、异音、动作是否正常顺畅。

### Scoring Standard

- P1 [25]: 定期检查松动。
- P2 [25]: 定期检查液压油老化。
- P3 [25]: 定期检查异音。
- P4 [25]: 定期检查动作是否正常顺畅。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得遗漏必要步骤、颠倒有先后约束的步骤或改变操作条件。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 31
- Printed page: 1727
- Section: 保养检查
- Local scope path: 保养检查 > 物理页 31, 印刷页 1727
- Evidence type: TEXT + PROCEDURE
- Evidence: 定期检查松动；定期检查液压油老化；定期检查异音；定期检查动作是否正常顺畅。

## LDD-Q-0104

**Type: FACT**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 质量保证

### Question

根据《LDD_R01_2023KW_C1N.pdf》的质量保证规定，LDD产品保修期如何计算？

### Standard Answer

发货后1年半或开始使用后1年，以较短者为准。

### Scoring Standard

- P1 [34]: 保修期可按发货后1年半计算。
- P2 [33]: 保修期也可按开始使用后1年计算。
- P3 [33]: 两种期间取较短者。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 32
- Printed page: 1728
- Section: 质量保证
- Local scope path: 质量保证 > 物理页 32, 印刷页 1728
- Evidence type: TEXT
- Evidence: 保修期可按发货后1年半计算；保修期也可按开始使用后1年计算；两种期间取较短者。

## LDD-Q-0105

**Type: FACT**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 质量保证

### Question

根据《LDD_R01_2023KW_C1N.pdf》的质量保证规定，对LDD自行改造或未经同意修理造成的故障是否在保修范围内？

### Standard Answer

不在保修范围内。

### Scoring Standard

- P1 [100]: 不在保修范围内。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 32
- Printed page: 1728
- Section: 质量保证
- Local scope path: 质量保证 > 物理页 32, 印刷页 1728
- Evidence type: TEXT
- Evidence: 不在保修范围内。

## LDD-Q-0106

**Type: TABLE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 标示更改

### Question

在《LDD_R01_2023KW_C1N.pdf》的表面粗糙度新旧标示对照表中，新标示Rz25对应的旧标示范围是什么？

### Standard Answer

答案为：12.5S～25S。

### Scoring Standard

- P1 [100]: 正确给出：12.5S～25S。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 1729
- Section: 标示更改
- Local scope path: 标示更改 > 表面粗糙度新旧标示表 > Rz25 > 旧标示 > 物理页 33, 印刷页 1729
- Evidence type: TABLE
- Evidence: 12.5S～25S。

## LDD-Q-0107

**Type: TABLE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD_R01_2023KW_C1N.pdf :: 标示更改

### Question

在《LDD_R01_2023KW_C1N.pdf》的O形密封圈新旧标示对照表中，新标示OR NBR-90 P10-N对应的旧标示是什么？

### Standard Answer

答案为：1BP10。

### Scoring Standard

- P1 [100]: 正确给出：1BP10。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 34
- Printed page: 1730
- Section: 标示更改
- Local scope path: 标示更改 > O形密封圈新旧标示表 > OR NBR-90 P10-N > 旧标示 > 物理页 34, 印刷页 1730
- Evidence type: TABLE
- Evidence: 1BP10。

## LDD-Q-0108

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

LDD0303-Q、LDD0363-Q、LDD0453-Q下降时的支撑器容量分别是多少？

### Standard Answer

依次为0.4cm³、0.6cm³、0.8cm³。

### Scoring Standard

- P1 [34]: LDD0303-Q为0.4cm³。
- P2 [33]: LDD0363-Q为0.6cm³。
- P3 [33]: LDD0453-Q为0.8cm³。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混淆表格行列、型号、尺寸代号或单位。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 规格
- Local scope path: 规格 > LDD Q/M-Q型规格表 > 支撑器容量-下降时 > LDD0303-Q | LDD0363-Q | LDD0453-Q > 物理页 8, Q specification table, descending capacity row
- Evidence type: TABLE
- Evidence: LDD0303-Q为0.4cm³；LDD0363-Q为0.6cm³；LDD0453-Q为0.8cm³。

## LDD-Q-0109

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

对于LDD系列，无论柱塞动作方向是水平还是垂直，负载率应设定在多少以下？

### Standard Answer

均应设定在30%以下。

### Scoring Standard

- P1 [50]: 柱塞动作方向无论水平还是垂直均适用该负载率规则。
- P2 [50]: 负载率应设定在30%以下。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 26
- Printed page: 1116
- Section: 设计注意事项
- Local scope path: 设计注意事项
- Evidence type: TEXT
- Evidence: 柱塞动作方向无论水平还是垂直均适用该负载率规则；负载率应设定在30%以下。

## LDD-Q-0110

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M

### Question

对于普通空气传感器连接型LDD0303-□M、LDD0363-□M和LDD0453-□M，自制传感器衬垫长度超过推荐最大长度时可能产生什么影响？

### Standard Answer

可能导致传感灵敏度下降。

### Scoring Standard

- P1 [100]: 可能导致传感灵敏度下降。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 18
- Printed page: 1106
- Section: 空气传感器
- Local scope path: 空气传感器 > 传感器衬垫设计尺寸表 > 推荐最大长度※3 > 空气传感型 > 物理页 18, note 3 below sensor-pad table
- Evidence type: TEXT
- Evidence: 可能导致传感灵敏度下降。

## LDD-Q-0111

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M、LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

与直接探测工件表面的探头行程开关式方法相比，LDD空气传感器连接型（LDD0303-□M、LDD0363-□M、LDD0453-□M及对应LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q）的空气传感检测方法具有哪些明确说明的优势？请列出全部四项。

### Standard Answer

不直接检测工件表面；铸铁或黑皮等凹凸表面也能检测动作；检测精度更高；冷却液更难从检测部侵入。

### Scoring Standard

- P1 [25]: 空气传感器不直接检测工件表面。
- P2 [25]: 铸铁或黑皮等凹凸表面也能检测动作。
- P3 [25]: 检测精度高于探头行程开关式方法。
- P4 [25]: 冷却液更难从检测部侵入支撑器内部。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得混入其他产品、型号或文档范围的结论。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 21
- Printed page: 1109
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 21, 柱塞的动作确认：选择M时
- Evidence type: TEXT
- Evidence: 空气传感器不直接检测工件表面；铸铁或黑皮等凹凸表面也能检测动作；检测精度高于探头行程开关式方法；冷却液更难从检测部侵入支撑器内部。

## LDD-Q-0112

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□

### Question

按PDF公式，标准型LDD0303-□要达到2.59kN支撑力，需要多少供给油压？保留2位小数并回代核验。

### Standard Answer

需要5.00MPa；回代0.70×5.00-0.91=2.59kN。 计算依据：LDD0303反求供给压力：P=(F+0.91)/0.70。 输入为F=2.59，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [20]: 正确列出或变形反求关系。
- P2 [35]: 供给油压数值为5.00。
- P3 [10]: 供给油压单位为MPa。
- P4 [20]: 执行回代核验。
- P5 [15]: 回代结果为2.59kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 8
- Evidence type: FORMULA + TABLE
- Evidence: LDD0303反求供给压力：P=(F+0.91)/0.70。

## LDD-Q-0113

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-□

### Question

按PDF公式，标准型LDD0363-□要达到4.51kN支撑力，需要多少供给油压？保留2位小数并回代核验。

### Standard Answer

需要6.00MPa；回代0.96×6.00-1.25=4.51kN。 计算依据：LDD0363反求供给压力：P=(F+1.25)/0.96。 输入为F=4.51，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [20]: 正确列出或变形反求关系。
- P2 [35]: 供给油压数值为6.00。
- P3 [10]: 供给油压单位为MPa。
- P4 [20]: 执行回代核验。
- P5 [15]: 回代结果为4.51kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 8
- Evidence type: FORMULA + TABLE
- Evidence: LDD0363反求供给压力：P=(F+1.25)/0.96。

## LDD-Q-0114

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□

### Question

供给油压同为6.0MPa时，按PDF公式分别计算标准型LDD0303-□、LDD0363-□、LDD0453-□的支撑力，指出最大者，并计算最大值与LDD0303-□的差值。结果保留2位小数。

### Standard Answer

依次为3.29kN、4.51kN、8.22kN；LDD0453最大；比LDD0303大4.93kN。 计算依据：LDD0303支撑力：F=0.70×P-0.91；LDD0363支撑力：F=0.96×P-1.25；LDD0453支撑力：F=1.75×P-2.28；表格数值差：Difference=V2-V1。 输入为P=6.0、V1=3.29、V2=8.22，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [17]: LDD0303的计算数值为3.29。
- P2 [17]: LDD0363的计算数值为4.51。
- P3 [17]: LDD0453的计算数值为8.22。
- P4 [17]: 最大值与LDD0303差值的计算数值为4.93。
- P5 [16]: 结果单位正确使用kN。
- P6 [16]: 最大者判断正确。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 8 | 物理页 8 | 物理页 8 | 物理页 8
- Evidence type: FORMULA + TABLE
- Evidence: LDD0303支撑力：F=0.70*P-0.91；LDD0363支撑力：F=0.96*P-1.25；LDD0453支撑力：F=1.75*P-2.28；表格数值差：Difference=V2-V1。

## LDD-Q-0115

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-□

### Question

标准型LDD0363-□供给油压从3.0MPa升至6.5MPa时，按PDF支撑力公式计算支撑力增加量。结果保留2位小数。

### Standard Answer

增加3.36kN。 计算依据：LDD0363压力变化引起的支撑力变化：DELTA_F=0.96×(P2-P1)。 输入为P1=3.0、P2=6.5，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [50]: 结果的计算数值为3.36。
- P2 [50]: 结果单位正确使用kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 8
- Evidence type: FORMULA + TABLE
- Evidence: LDD0363压力变化引起的支撑力变化：DELTA_F=0.96*(P2-P1)。

## LDD-Q-0116

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-HM

### Question

按PDF工件接触力公式，LDD0363-HM的目标接触力为26.27N、柱塞弹簧力为8.6N、U=15mm时，反求供气压力。保留2位小数并确认是否在0.05～0.15MPa推荐范围内。

### Standard Answer

供气压力为0.10MPa，处于0.05～0.15MPa推荐范围内。 计算依据：反求空气传感供气压力：Pa=(Fc-Fs)×4/(U^2×π)。 输入为Fc=26.27、Fs=8.6、U=15，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [34]: 结果的计算数值为0.10。
- P2 [33]: 结果单位正确使用MPa。
- P3 [33]: 推荐范围判断正确。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 21
- Printed page: 1109
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 21
- Evidence type: FORMULA + TABLE
- Evidence: 反求空气传感供气压力：Pa=(Fc-Fs)*4/(U**2*PI)。

## LDD-Q-0117

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-LM、LDD0363-LM、LDD0453-LM

### Question

供气压力同为0.10MPa时，按PDF公式分别计算LDD0303-LM（U=12mm）、LDD0363-LM（U=15mm）和LDD0453-LM（U=16mm）中由供气产生的附加接触力，并指出最大者。结果保留2位小数。

### Standard Answer

依次为11.31N、17.67N、20.11N；U=16mm时最大。 计算依据：气压附加接触力：F_air=Pa×U^2×π/4。 输入为Pa=0.10、U=12、U=15、U=16，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [20]: U=12mm的计算数值为11.31。
- P2 [20]: U=15mm的计算数值为17.67。
- P3 [20]: U=16mm的计算数值为20.11。
- P4 [20]: 结果单位正确使用N。
- P5 [20]: 最大者判断正确。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 21
- Printed page: 1109
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 21 | 物理页 21 | 物理页 21
- Evidence type: FORMULA + TABLE
- Evidence: 气压附加接触力：F_air=Pa*U**2*PI/4。

## LDD-Q-0118

**Type: CALCULATION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列中，支撑器与夹紧器对向使用且可用支撑力为6.0kN时，按PDF共通的1.5倍规则计算最大允许夹紧力，结果保留2位小数。

### Standard Answer

最大允许夹紧力为4.00kN。 计算依据：由可用支撑力反求最大夹紧力：Fc_max=Fs/1.5。 输入为Fs=6.0，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [50]: 结果的计算数值为4.00。
- P2 [50]: 结果单位正确使用kN。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 25
- Evidence type: FORMULA + TABLE
- Evidence: 由可用支撑力反求最大夹紧力：Fc_max=Fs/1.5。

## LDD-Q-0119

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0363-□、LDD0363-Q

### Question

由PDF规格表数值计算LDD0363-□标准型与LDD0363-Q行程加长型一次上升抱紧加一次下降的容量合计，并计算Q型增加量。结果保留2位小数。

### Standard Answer

标准型合计1.60cm³；Q型合计2.50cm³；Q型增加0.90cm³。 计算依据：循环容量合计：Vtotal=Vrise+Vdesc；表格数值差：Difference=V2-V1。 输入为Vrise=1.3、Vdesc=0.3、Vrise=1.9、Vdesc=0.6、V1=1.60、V2=2.50，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [25]: 标准型合计的计算数值为1.60。
- P2 [25]: Q型合计的计算数值为2.50。
- P3 [25]: Q型增加量的计算数值为0.90。
- P4 [25]: 结果单位正确使用cm³。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 8 | 物理页 8 | 物理页 8
- Evidence type: FORMULA + TABLE
- Evidence: 循环容量合计：Vtotal=Vrise+Vdesc；表格数值差：Difference=V2-V1。

## LDD-Q-0120

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0453-Q、LDD0453-□

### Question

由PDF规格表数值计算LDD0453-Q相对LDD0453-□标准型增加的质量。结果保留2位小数。

### Standard Answer

增加0.05kg。 计算依据：表格数值差：Difference=V2-V1。 输入为V1=0.85、V2=0.90，各输入量采用题干所列单位；计算结果采用 ROUND_HALF_UP 四舍五入并保留 2 位小数。

### Scoring Standard

- P1 [50]: 结果的计算数值为0.05。
- P2 [50]: 结果单位正确使用kg。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得使用错误公式、输入值、单位或舍入规则，也不得遗漏题目要求的比较或反算结论。

### Tolerance

- 计算结果保留 2 位小数，采用四舍五入（ROUND_HALF_UP）。

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 8
- Printed page: 1096
- Section: 计算公式
- Local scope path: 计算公式 > 物理页 8
- Evidence type: FORMULA + TABLE
- Evidence: 表格数值差：Difference=V2-V1。

## LDD-Q-0121

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列的本体安装力矩高于和低于PDF推荐值时，分别可能造成什么后果？

### Standard Answer

高于推荐力矩：可能导致主体变形、无法正常动作。低于推荐力矩：可能导致支撑器松动、O形密封圈破损并漏油。

### Scoring Standard

- P1 [20]: 高于推荐力矩可能导致主体变形。
- P2 [20]: 高于推荐力矩可能导致无法正常动作。
- P3 [20]: 低于推荐力矩可能导致支撑器松动。
- P4 [20]: 低于推荐力矩可能导致O形密封圈破损。
- P5 [20]: 低于推荐力矩可能导致漏油。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 14、16
- Printed page: 1102、1104
- Section: 安装施工
- Local scope path: 安装施工 > 物理页s 14 and 16, LDD body-installation torque caution
- Evidence type: TEXT
- Evidence: 高于推荐本体安装力矩可能导致主体变形；高于推荐本体安装力矩可能导致无法正常动作；低于推荐本体安装力矩可能导致支撑器松动；低于推荐本体安装力矩可能导致O形密封圈破损；低于推荐本体安装力矩可能导致漏油。

## LDD-Q-0122

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□、LDD0363-□、LDD0453-□、LDD0303-Q、LDD0363-Q、LDD0453-Q

### Question

对标准型LDD0303-□、LDD0363-□、LDD0453-□及对应LDD0303-Q、LDD0363-Q、LDD0453-Q，在柱塞行程0.5mm以下接触工件时有什么特殊风险，PDF要求如何使用？

### Standard Answer

工件接触力会大于柱塞弹簧力；应在有效行程范围内使用。

### Scoring Standard

- P1 [50]: 工件接触力会大于柱塞弹簧力。
- P2 [50]: 应在有效行程范围内使用。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 13、15
- Printed page: 1101、1103
- Section: 外形尺寸
- Local scope path: 外形尺寸 > 物理页 13, 外形尺寸 local paragraph
- Evidence type: TEXT
- Evidence: 在柱塞行程0.5mm以下接触工件时，工件接触力会大于柱塞弹簧力；超短行程条件下应在有效行程范围内使用。

## LDD-Q-0123

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-□M、LDD0363-□M、LDD0453-□M、LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

LDD空气传感器连接型，包括LDD0303-□M、LDD0363-□M、LDD0453-□M及对应LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q，长期使用后如果检出压差值变小，PDF建议如何处理？

### Standard Answer

长期使用有时会出现检出压差值变小；发生时应委托本公司对产品进行解体大修。

### Scoring Standard

- P1 [50]: 长期使用有时会出现检出压差值变小。
- P2 [50]: 发生时应委托本公司对产品进行解体大修。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 22
- Printed page: 1110
- Section: 空气传感器
- Local scope path: 空气传感器 > 物理页 22, 空气传感器 local paragraph
- Evidence type: TEXT
- Evidence: 因使用环境等因素，长期使用有时会导致检出压差值变小；检出压差值变小时，应委托本公司对产品进行解体大修。

## LDD-Q-0126

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD0303-M-Q、LDD0363-M-Q、LDD0453-M-Q

### Question

对于行程加长空气传感器连接型LDD0303-M-Q、LDD0363-M-Q和LDD0453-M-Q，采用过长的传感器衬垫时可能造成什么影响？

### Standard Answer

有时会导致传感灵敏度下降。

### Scoring Standard

- P1 [100]: 有时会导致传感灵敏度下降。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 20
- Printed page: 1108
- Section: 外形尺寸
- Local scope path: 外形尺寸 > 物理页 20, 外形尺寸 local paragraph
- Evidence type: TEXT
- Evidence: 传感衬垫的长度过大时有时会导致传感灵敏度下降。

## LDD-Q-0127

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LDD 双动式油压支撑器
- Model / Scope: LDD 系列

### Question

LDD系列的油压回路设计有什么要求，回路设计错误可能造成什么后果？

### Standard Answer

应设计适当的油压回路；设计错误可能导致机械设备误动作或破损。

### Scoring Standard

- P1 [50]: 应设计适当的油压回路。
- P2 [50]: 设计错误可能导致机械设备误动作或破损。

### Accepted Variants

- 允许不改变技术含义的同义中文表述；型号、单位、条件和结论必须与标准答案一致，数值须满足 Tolerance。

### Forbidden Errors

- 不得反转适用条件、遗漏禁止事项或省略资料明确说明的后果。

### Tolerance

- N/A

### Source

- PDF: LDD_R01_2023KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 设计注意事项
- Local scope path: 设计注意事项 > 物理页 25, 设计注意事项 local paragraph
- Evidence type: TEXT
- Evidence: 应设计适当的油压回路；油压回路设计错误会导致机械设备误动作或破损。
