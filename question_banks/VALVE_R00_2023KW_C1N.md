---
schema_version: will-ai-question-bank/v1
source_pdf: VALVE_R00_2023KW_C1N.pdf
source_sha256: aa85a41bd6a3d29a7a1a0544426d4f1140aa496a99f2e41287f82f49531a3961
source_pages: 88
question_bank_version: V1
product_scope: VALVE / BK / BEQ / BLS / BLG / BMA / BMG / JSS / AU / BU / BH / BC
---

# VALVE_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `VALVE_R00_2023KW_C1N.pdf`
- SHA-256: `aa85a41bd6a3d29a7a1a0544426d4f1140aa496a99f2e41287f82f49531a3961`
- Physical pages: 88
- Product scope: 液压阀及相关液压单元，重点覆盖 BK、BEQ、BLS、BLG、BMA、BMG，并覆盖 PDF 内直接相关的 JSS、AU、BU、BH、BC、安装、操作和维护要求

## 2. Scope

本题库以一个 PDF 对应一个 canonical Markdown 的方式覆盖液压阀产品导航、无泄漏保压、顺序控制、减压、蓄能和增压、手动与电气无泄漏阀组，以及直接适用于这些产品的安装、操作和维护要求。BLG、BLS、BMA、BMG 仅作为同一来源中的产品范围，不拆分为独立题库。公司介绍、销售网点、纯联系信息和无耐久技术价值的重复页不作为考核对象。

### 2.1 覆盖原则

- `HIGH`：BK、BEQ、BLS、BLG、BMA、BMG 的型号、规格、动作和关键选型边界均映射到题目。
- `MEDIUM`：JSS、AU、BU、BH、BC 及文档共通安装、安全和维护要求映射到代表题。
- `LOW/EXCLUDED`：纯目录导航、公司信息、销售网点和重复说明保留处置理由，不单独出题。

### 2.2 图表与计算边界

- `CHART` 题只依据 PDF 图形中的坐标、标注或曲线进行视觉读取，并使用与图像分辨率相符的公差。
- `CALCULATION` 题使用 PDF 明示的温度—压力关系和题目给定输入；最终结果采用十进制 `ROUND_HALF_UP`。
- 离散型号规格按 `TABLE` 或 `SPEC_LOOKUP` 判定，不把离散表伪装成连续曲线。

### 2.3 来源清单

| Coverage ID | 物理页 | 局部范围 | Evidence type | 可测试对象 / 范围决定 | Priority / Disposition |
|---|---:|---|---|---|---|
| VALVE-SI-001 | 1-2 | 液压阀产品导航 | TEXT + TABLE | 产品类别与用途；清单保留 | LOW：导航页，不单独出题 |
| VALVE-SI-002 | 3-6 | 单动与复动夹具示例回路 | CIRCUIT + TEXT | 保压、卸压和安全回路；`VALVE-Q-0006` | MEDIUM：已映射 |
| VALVE-SI-003 | 7-10 | 无泄漏可靠性、安全与局部增压/减压 | CHART + FORMULA + CIRCUIT | 断压保压、可靠性图、温压换算；`VALVE-Q-0006`-`0008` | HIGH：已映射 |
| VALVE-SI-004 | 11-14 | BK 单动无泄漏阀 | MODEL + TABLE + DRAWING | 型号、规格和配管限制；`VALVE-Q-0001`、`0009` | HIGH：已映射 |
| VALVE-SI-005 | 15-18 | BEQ 复动无泄漏阀 | MODEL + TABLE + DRAWING | 型号、规格和先导压力；`VALVE-Q-0002`、`0010` | HIGH：已映射 |
| VALVE-SI-006 | 19-20 | 无泄漏截止阀 | TEXT + CIRCUIT | 截止与保压用途；由 `VALVE-Q-0006` 代表覆盖 | MEDIUM：已映射 |
| VALVE-SI-007 | 21-26 | BLS / BLG 顺序阀 | MODEL + TABLE + CIRCUIT | 型号、压力档、动作、安装和设定差；`VALVE-Q-0003`、`0011`-`0013` | HIGH：已映射 |
| VALVE-SI-008 | 27-30 | 压力平衡阀 | TEXT + CIRCUIT | 平衡释放和回路用途；`VALVE-Q-0012` | MEDIUM：已映射 |
| VALVE-SI-009 | 31-40 | JSS 弹簧蓄能器 | MODEL + TABLE + DRAWING | 型号语法、容量、安装和配管；`VALVE-Q-0005`、`0016` | MEDIUM：已映射 |
| VALVE-SI-010 | 41-44 | 压力指示器 | TABLE + DRAWING | 压力确认用途；清单保留 | LOW：非核心产品，未单独出题 |
| VALVE-SI-011 | 45-50 | BMA / BMG 减压阀 | MODEL + TABLE + DRAWING | 型号、压力档、压差和配管边界；`VALVE-Q-0004`、`0014`-`0015` | HIGH：已映射 |
| VALVE-SI-012 | 51-58 | AU 连续输出增压器 | TEXT + CIRCUIT + CAUTION | 动作顺序、泄漏、脉动和回路限制；`VALVE-Q-0019`-`0020` | MEDIUM：已映射 |
| VALVE-SI-013 | 59-64 | BU 单次输出增压器 | MODEL + TABLE + CHART | 型号、规格和增压曲线；`VALVE-Q-0005`、`0017`-`0018` | MEDIUM：已映射 |
| VALVE-SI-014 | 65-70 | 先导减压与自动排气 | CIRCUIT + PROCEDURE | 先导控制和空气排放；由 `VALVE-Q-0023` 代表覆盖 | MEDIUM：已映射 |
| VALVE-SI-015 | 71-80 | 先导止回、BH、BC 无泄漏阀组 | TEXT + CIRCUIT + PROCEDURE | 保压、手动防误操作、电气/气动控制；`VALVE-Q-0021`-`0022` | MEDIUM：已映射 |
| VALVE-SI-016 | 81-86 | 共通安装、操作和维护 | PROCEDURE + CAUTION | 清洁、密封带、排气、安全和检查；`VALVE-Q-0023`-`0024` | MEDIUM：已映射 |
| VALVE-SI-017 | 87-88 | 公司与销售网点 | TEXT | 公司和联系信息 | EXCLUDED：非耐久技术知识 |

## 3. Question Statistics

- Total: 24
- Direct core valve: 15
- Supporting hydraulic unit: 5
- Document Common: 4
- MODEL: 5
- SPEC_LOOKUP: 5
- TABLE: 2
- CALCULATION: 1
- CHART: 2
- PROCEDURE: 4
- CAUTION: 5

## 4. Questions

## VALVE-Q-0001

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: BK 单动无泄漏阀
- Model / Scope: BK 型号表示与配管方式

### Question

说明 BK 型号字段中油口尺寸、压力范围、手柄方向和配管方式的含义，并列出 `GA`、`GB`、`GC`、`GS` 的安装边界。

### Standard Answer

油口尺寸代码 `2` 为 Rc1/4、`3` 为 Rc3/8；压力代码 `2` 为 2.0～7.0 MPa、`5` 为 7.0～30.0 MPa；手柄代码 `1` 为右手柄标准型、`2` 为左手柄型。配管无标记为 Rc 外配管；`GA` 为板式左侧面连接且仅适用于右手柄；`GB` 为板式底面连接；`GC` 为板式右侧面连接且仅适用于左手柄；`GS` 用于 BLS/BLB/BM 连接。

### Scoring Standard

- P1 [8]: 油口代码 `2` 为 Rc1/4。
- P2 [8]: 油口代码 `3` 为 Rc3/8。
- P3 [8]: 压力代码 `2` 为 2.0～7.0 MPa。
- P4 [8]: 压力代码 `5` 为 7.0～30.0 MPa。
- P5 [8]: 手柄代码 `1` 为右手柄标准型。
- P6 [8]: 手柄代码 `2` 为左手柄型。
- P7 [8]: 配管无标记为 Rc 外配管。
- P8 [8]: `GA` 为板式左侧面连接。
- P9 [8]: `GA` 仅适用于右手柄。
- P10 [7]: `GB` 为板式底面连接。
- P11 [7]: `GC` 为板式右侧面连接。
- P12 [7]: `GC` 仅适用于左手柄。
- P13 [7]: `GS` 用于 BLS/BLB/BM 连接。

### Accepted Variants

- `Rc 1/4`、`Rc1/4` 等空格差异等价。

### Forbidden Errors

- 交换 GA 与 GC 的连接侧或手柄限制。

### Tolerance

- 型号字段和压力范围按表中值精确判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 1575
- Section: BK 型号表示
- Local scope path: BK > 型号表示 > 油口、压力、手柄、配管
- Evidence type: MODEL
- Evidence: 型号表示表逐项定义代码 2/3、2/5、1/2 以及无标记、GA、GB、GC、GS。

## VALVE-Q-0002

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: BEQ 复动无泄漏阀
- Model / Scope: BEQ 型号表示与配管方式

### Question

解释 `BEQ0220-0G` 中压力代码、设计编号和配管代码，并说明无标记、`GA`、`GB` 的含义。

### Standard Answer

压力代码 `2` 表示 2.0～7.0 MPa，代码 `5` 表示 7.0～30.0 MPa；设计编号为 `0`。配管无标记表示 Rc 外配管，`GA` 表示板式后面连接，`GB` 表示板式底面连接。

### Scoring Standard

- P1 [17]: 压力代码 `2` 正确解释为 2.0～7.0 MPa。
- P2 [17]: 压力代码 `5` 正确解释为 7.0～30.0 MPa。
- P3 [17]: 设计编号正确写为 `0`。
- P4 [17]: 无标记正确解释为 Rc 外配管。
- P5 [16]: `GA` 为板式后面连接。
- P6 [16]: `GB` 为板式底面连接。

### Accepted Variants

- “后侧连接”可等同于“后面连接”。

### Forbidden Errors

- 将 GA 解释为底面连接或省略高压代码范围。

### Tolerance

- 压力范围按表中值精确判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 17
- Printed page: 1579
- Section: BEQ 型号表示
- Local scope path: BEQ > 型号表示 > 压力、设计、配管
- Evidence type: MODEL
- Evidence: 型号表示区给出压力代码 2/5、设计编号 0 和三种配管表示。

## VALVE-Q-0003

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: BLS / BLG 顺序阀
- Model / Scope: BLS 与 BLG 型号及连接边界

### Question

分别说明 BLS 与 BLG 的压力调整代码、配管方式及设定压力写法，并指出需要外配管接头时应选择哪一系列。

### Standard Answer

BLS 调整代码 `3` 为 1～4 MPa、`5` 为 3～8 MPa、`7` 为 8～20 MPa；配管可为无标记 Rc 外配管、`G` 板式、`K` BK 连接或 `W` BK/BLB 连接。BLG 调整代码 `3` 为 1～6 MPa、`6` 为 5～18 MPa，只提供 `G` 板式连接；需要外配管接头时选择 BLS。两者均在型号末尾括号内以明确单位写设定压力，例如 `(5.0MPa)`。

### Scoring Standard

- P1 [9]: BLS 代码 `3` 正确对应 1～4 MPa。
- P2 [9]: BLS 代码 `5` 正确对应 3～8 MPa。
- P3 [9]: BLS 代码 `7` 正确对应 8～20 MPa。
- P4 [9]: BLS 配管无标记为 Rc 外配管。
- P5 [8]: BLS 的 `G` 为板式连接。
- P6 [8]: BLS 的 `K` 为 BK 连接。
- P7 [8]: BLS 的 `W` 为 BK/BLB 连接。
- P8 [8]: BLG 代码 `3` 正确对应 1～6 MPa。
- P9 [8]: BLG 代码 `6` 正确对应 5～18 MPa。
- P10 [8]: BLG 只提供 `G` 板式连接。
- P11 [8]: 需要外配管接头时选择 BLS。
- P12 [8]: 设定压力写在型号末尾括号中并带 MPa 单位。

### Accepted Variants

- `5.0 MPa` 与 `5.0MPa` 等价。

### Forbidden Errors

- 声称 BLG 提供标准 Rc 外配管型。

### Tolerance

- 压力档范围按型号表精确判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 23, 25
- Printed page: 1585, 1587
- Section: BLS / BLG 型号表示
- Local scope path: 顺序阀 > BLS 与 BLG > 调整压力、配管、设定压力
- Evidence type: MODEL
- Evidence: 两页型号表示表分别定义压力代码、配管选项和括号内设定压力规则。

## VALVE-Q-0004

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: BMA / BMG 减压阀
- Model / Scope: BMA 与 BMG 型号及压力标注

### Question

说明 BMA/BMG 的二次侧压力代码和型号末尾括号内容，并比较两系列的配管边界。

### Standard Answer

二次侧设定代码 `3` 为 1～6 MPa、`5` 为 3～14 MPa、`7` 为 6～27 MPa。型号末尾括号按“二次侧设定压力—一次侧供给压力”书写，例如 `(5.0-25.0MPa)`。BMA 可选无标记 Rc1/4 外配管、`G` 板式或 `K` BK 连接；BMG 只提供 `G` 板式连接，需要外配管接头时选择 BMA。

### Scoring Standard

- P1 [10]: 代码 `3` 正确对应 1～6 MPa。
- P2 [10]: 代码 `5` 正确对应 3～14 MPa。
- P3 [10]: 代码 `7` 正确对应 6～27 MPa。
- P4 [10]: 括号首值是二次侧设定压力。
- P5 [10]: 括号次值是一次侧供给压力。
- P6 [10]: BMA 无标记为 Rc1/4 外配管。
- P7 [10]: BMA 的 `G` 为板式连接。
- P8 [10]: BMA 的 `K` 为 BK 连接。
- P9 [10]: BMG 只提供 `G` 板式连接。
- P10 [10]: BMG 需要外配管接头时选择 BMA。

### Accepted Variants

- 连字符可写作半角 `-` 或范围连接号，但两端含义必须正确。

### Forbidden Errors

- 交换括号中一次侧和二次侧压力的顺序。

### Tolerance

- 压力范围按型号表精确判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 47, 49
- Printed page: 1609, 1611
- Section: BMA / BMG 型号表示
- Local scope path: 减压阀 > BMA 与 BMG > 压力代码与配管
- Evidence type: MODEL
- Evidence: BMA 与 BMG 型号表示页给出相同压力代码、括号含义和不同连接边界。

## VALVE-Q-0005

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: JSS 弹簧蓄能器 / BU 单次输出增压器
- Model / Scope: JSS 与 BU 关键型号字段

### Question

说明 JSS 的基准压力、排出容积、安装方向和配管字段，并说明 BU 的增压比代码及型号末尾括号含义。

### Standard Answer

JSS 基准压力代码 `2`～`7` 分别对应 2～7 MPa；排出容积代码 `02`、`05`、`10` 分别对应 2.5、5.0、10 cm³；安装方向 `H` 为水平、`V` 为垂直；配管 `C/S` 为外配管 G/Rc，`G` 为板式，`GC/GS` 为板式加外配管 G/Rc。BU 增压比代码 `2`、`3`、`6` 分别为 2.2、3.0、6.0 倍；型号末尾括号填写一次侧供给压力。

### Scoring Standard

- P1 [5]: JSS 基准压力代码 `2` 对应 2 MPa。
- P2 [5]: JSS 基准压力代码 `3` 对应 3 MPa。
- P3 [5]: JSS 基准压力代码 `4` 对应 4 MPa。
- P4 [5]: JSS 基准压力代码 `5` 对应 5 MPa。
- P5 [5]: JSS 基准压力代码 `6` 对应 6 MPa。
- P6 [5]: JSS 基准压力代码 `7` 对应 7 MPa。
- P7 [5]: JSS `02` 对应 2.5 cm³。
- P8 [5]: JSS `05` 对应 5.0 cm³。
- P9 [5]: JSS `10` 对应 10 cm³。
- P10 [5]: JSS `H` 表示水平安装。
- P11 [5]: JSS `V` 表示垂直安装。
- P12 [5]: JSS `C` 表示 G 螺纹外配管。
- P13 [5]: JSS `S` 表示 Rc 螺纹外配管。
- P14 [5]: JSS `G` 表示板式连接。
- P15 [5]: JSS `GC` 表示板式加 G 螺纹外配管。
- P16 [5]: JSS `GS` 表示板式加 Rc 螺纹外配管。
- P17 [5]: BU 代码 `2` 表示 2.2 倍。
- P18 [5]: BU 代码 `3` 表示 3.0 倍。
- P19 [5]: BU 代码 `6` 表示 6.0 倍。
- P20 [5]: BU 型号末尾括号填写一次侧供给压力。

### Accepted Variants

- 容积单位可写作 `cm3` 或 `cm³`。

### Forbidden Errors

- 将 BU 括号值解释为增压后的二次侧输出压力。

### Tolerance

- 型号代码及离散容积值精确判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 33, 61
- Printed page: 1595, 1623
- Section: JSS / BU 型号表示
- Local scope path: 弹簧蓄能器与单次输出增压器 > 型号字段
- Evidence type: MODEL
- Evidence: JSS 与 BU 型号表示区分别给出基准压力、容积、安装、配管和增压比字段。

## VALVE-Q-0006

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: 无泄漏阀安全回路
- Model / Scope: VALVE_R00_2023KW_C1N.pdf :: 断压保压与掉落防止

### Question

为什么无泄漏阀或无泄漏先导止回阀适合用于夹具安全回路？说明在压力源切断或停电时的作用和风险控制目标。

### Standard Answer

这类阀在压力源切断或停电后仍能封闭回路并保持二次侧压力，避免因内部泄漏导致压力下降；其安全目标是防止工件或机构掉落，并保持夹具或执行机构的姿态。它不能替代正确的机械安全设计和卸压操作。

### Scoring Standard

- P1 [17]: 压力源切断后仍可封闭回路。
- P2 [17]: 停电时仍可保持二次侧压力。
- P3 [17]: 无泄漏结构用于抑制内部泄漏导致的压降。
- P4 [17]: 安全目标之一是防止工件或机构掉落。
- P5 [16]: 安全目标之一是保持夹具或执行机构姿态。
- P6 [16]: 无泄漏保压不能替代机械安全设计和卸压操作。

### Accepted Variants

- “失压”可等同于“压力源切断”。

### Forbidden Errors

- 声称停电后系统可无限期安全保压而无需机械防护或检查。

### Tolerance

- N/A

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 3-8
- Printed page: 1565-1570
- Section: 安全回路与无泄漏可靠性
- Local scope path: 液压阀总览 > 安全与保压回路
- Evidence type: TEXT
- Evidence: 示例回路与安全说明将无泄漏保压绑定到压力源切断、停电、掉落防止和姿态保持。

## VALVE-Q-0007

**Type: CALCULATION**

### Target

- Binding: DOCUMENT_COMMON
- Product: 密闭液压回路
- Model / Scope: VALVE_R00_2023KW_C1N.pdf :: 油温变化引起的压力变化

### Question

某密闭回路由无泄漏阀保持在 20.00 MPa。PDF 给出的参考关系是油温每下降 1 ℃，油压约下降 0.69 MPa。若油温下降 8 ℃，按十进制 `ROUND_HALF_UP` 保留两位小数，计算压力变化量和估算剩余压力。

### Standard Answer

压力下降量为 `0.69 × 8 = 5.52 MPa`；估算剩余压力为 `20.00 − 5.52 = 14.48 MPa`。最终结果保留两位小数，使用 `ROUND_HALF_UP`。

### Scoring Standard

- P1 [17]: 正确采用 0.69 MPa/℃ 的参考关系。
- P2 [17]: 正确使用温差 8 ℃。
- P3 [17]: 正确计算压力下降量 5.52 MPa。
- P4 [17]: 正确计算剩余压力 14.48 MPa。
- P5 [16]: 压力结果使用 MPa 单位。
- P6 [16]: 明确使用十进制 ROUND_HALF_UP 保留两位小数。

### Accepted Variants

- 可分步或用单一表达式 `20.00-0.69×8`。

### Forbidden Errors

- 将降温误算为压力上升，或使用二进制浮点近似替代规定舍入规则。

### Tolerance

- 最终值精确到 0.01 MPa；只接受 14.48 MPa。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1569
- Section: 油温与压力变化参考
- Local scope path: 无泄漏可靠性 > 温度影响说明
- Evidence type: FORMULA
- Evidence: 文档明确给出油温每变化 1 ℃，油压约变化 0.69 MPa 的参考关系。

## VALVE-Q-0008

**Type: CHART**

### Target

- Binding: DOCUMENT_COMMON
- Product: 无泄漏阀可靠性验证
- Model / Scope: VALVE_R00_2023KW_C1N.pdf :: 无泄漏耐久图

### Question

从无泄漏耐久图的两个标注点读取 45.2 小时和 115.8 小时时的油温与油压，并说明图中结论。

### Standard Answer

45.2 小时标注约为 19 ℃、16.5 MPa；115.8 小时标注也约为 19 ℃、16.5 MPa。两个相同油温条件下的标注压力没有显示因泄漏造成的下降，支持无泄漏保压的可靠性结论。

### Scoring Standard

- P1 [15]: 读取第一个标注时间 45.2 小时。
- P2 [15]: 读取 45.2 小时点油温约 19 ℃。
- P3 [14]: 读取 45.2 小时点油压约 16.5 MPa。
- P4 [14]: 读取第二个标注时间 115.8 小时。
- P5 [14]: 读取 115.8 小时点油温约 19 ℃。
- P6 [14]: 读取 115.8 小时点油压约 16.5 MPa。
- P7 [14]: 结论限定为图中未显示泄漏导致的压降，不扩张为无限期保证。

### Accepted Variants

- 时间可按图像分辨率写为约 45 h 和约 116 h。

### Forbidden Errors

- 用温压公式替代对图中标注点的视觉读取。

### Tolerance

- 视觉读图公差：时间 ±1 h、温度 ±1 ℃、压力 ±0.5 MPa。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 1569
- Section: 无泄漏可靠性图
- Local scope path: 无泄漏可靠性 > 耐久时间—压力图
- Evidence type: CHART
- Evidence: 图中在 45.2 h 和 115.8 h 位置分别标注 19 ℃ 与 16.5 MPa。

## VALVE-Q-0009

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: BK 单动无泄漏阀
- Model / Scope: BK22 / BK25 / BK32 规格

### Question

列出 BK22□3、BK25□3、BK32□3 的使用压力、耐压和最小受压面积，并给出共通温度、使用流体和质量。

### Standard Answer

BK22□3：2～7 MPa、耐压 10.5 MPa、最小受压面积 17.0 cm²；BK25□3：7～30 MPa、耐压 37.5 MPa、最小受压面积 14.2 cm²；BK32□3：2～7 MPa、耐压 10.5 MPa、最小受压面积 30.0 cm²。共通使用温度 0～70 ℃，使用 ISO VG32 一般液压油，质量约 1.4 kg。

### Scoring Standard

- P1 [9]: BK22□3 的使用压力为 2～7 MPa。
- P2 [9]: BK22□3 的耐压为 10.5 MPa。
- P3 [9]: BK22□3 的最小受压面积为 17.0 cm²。
- P4 [9]: BK25□3 的使用压力为 7～30 MPa。
- P5 [8]: BK25□3 的耐压为 37.5 MPa。
- P6 [8]: BK25□3 的最小受压面积为 14.2 cm²。
- P7 [8]: BK32□3 的使用压力为 2～7 MPa。
- P8 [8]: BK32□3 的耐压为 10.5 MPa。
- P9 [8]: BK32□3 的最小受压面积为 30.0 cm²。
- P10 [8]: 共通使用温度为 0～70 ℃。
- P11 [8]: 共通使用流体为 ISO VG32 一般液压油。
- P12 [8]: 质量约 1.4 kg。

### Accepted Variants

- 面积单位可写作 `cm2` 或 `cm²`。

### Forbidden Errors

- 将 BK25 高压规格的耐压值用于 BK22 或 BK32。

### Tolerance

- 表中数值精确判定；质量允许写“约 1.4 kg”。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 1575
- Section: BK 规格
- Local scope path: BK > 规格表
- Evidence type: TABLE
- Evidence: BK 规格表逐型号列出使用压力、耐压、最小受压面积、温度、流体和质量。

## VALVE-Q-0010

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: BEQ 复动无泄漏阀
- Model / Scope: BEQ0220 / BEQ0250 规格与先导压力

### Question

比较 BEQ0220 与 BEQ0250 的使用压力和耐压，并写出开启压力、先导压力公式、最小受压面积、温度和质量。

### Standard Answer

BEQ0220 使用压力 1.0～7.0 MPa、耐压 10.5 MPa；BEQ0250 使用压力 7.0～30.0 MPa、耐压 37.5 MPa。共通开启压力 0.07 MPa；所需先导压力至少为 `A2 保持压力 ÷ 5.5 + 0.3 MPa`；最小受压面积 14.3 cm²；温度 0～70 ℃；质量约 1.3 kg。

### Scoring Standard

- P1 [10]: BEQ0220 使用压力为 1.0～7.0 MPa。
- P2 [10]: BEQ0220 耐压为 10.5 MPa。
- P3 [10]: BEQ0250 使用压力为 7.0～30.0 MPa。
- P4 [10]: BEQ0250 耐压为 37.5 MPa。
- P5 [10]: 开启压力为 0.07 MPa。
- P6 [10]: 先导压力计算先用 A2 保持压力除以 5.5。
- P7 [10]: 先导压力计算再加 0.3 MPa。
- P8 [10]: 最小受压面积为 14.3 cm²。
- P9 [10]: 使用温度为 0～70 ℃。
- P10 [10]: 质量约 1.3 kg。

### Accepted Variants

- 先导公式可写作 `Ppilot ≥ PA2/5.5 + 0.3 MPa`。

### Forbidden Errors

- 省略先导公式中的固定加成 0.3 MPa。

### Tolerance

- 规格值按表中值精确判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 17
- Printed page: 1579
- Section: BEQ 规格
- Local scope path: BEQ > 规格表 > 压力与受压面积
- Evidence type: TABLE
- Evidence: BEQ 规格表列出两型号压力范围、耐压、开启压力、先导压力关系和共通条件。

## VALVE-Q-0011

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: BLS / BLG 顺序阀
- Model / Scope: 调整范围、使用压力和螺杆变化量

### Question

列出 BLS 三个调整压力档和每转压力变化量，并列出 BLG 两个调整压力档、使用压力范围和每转压力变化量。

### Standard Answer

BLS：1～4 MPa 档每转约 0.7 MPa，3～8 MPa 档每转约 1.0 MPa，8～20 MPa 档每转约 2.6 MPa；总体使用压力 2～30 MPa。BLG2830：调整 1～6 MPa、使用 2～35 MPa、每转约 1.0 MPa；BLG2860：调整 5～18 MPa、使用 6～35 MPa、每转约 2.8 MPa。

### Scoring Standard

- P1 [8]: BLS 调整档一为 1～4 MPa。
- P2 [8]: BLS 调整档一每转约变化 0.7 MPa。
- P3 [7]: BLS 调整档二为 3～8 MPa。
- P4 [7]: BLS 调整档二每转约变化 1.0 MPa。
- P5 [7]: BLS 调整档三为 8～20 MPa。
- P6 [7]: BLS 调整档三每转约变化 2.6 MPa。
- P7 [7]: BLS 总体使用压力为 2～30 MPa。
- P8 [7]: BLG2830 调整范围为 1～6 MPa。
- P9 [7]: BLG2830 使用范围为 2～35 MPa。
- P10 [7]: BLG2830 每转约变化 1.0 MPa。
- P11 [7]: BLG2860 调整范围为 5～18 MPa。
- P12 [7]: BLG2860 使用范围为 6～35 MPa。
- P13 [7]: BLG2860 每转约变化 2.8 MPa。
- P14 [7]: 所有压力值使用 MPa 单位。

### Accepted Variants

- “一圈”可等同于“一转”。

### Forbidden Errors

- 将 BLG2860 的 2.8 MPa/转误配给 BLG2830。

### Tolerance

- 调整范围和使用范围精确判定；每转变化量按“约”值判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 23, 25
- Printed page: 1585, 1587
- Section: BLS / BLG 规格
- Local scope path: 顺序阀 > 规格表 > 调整与使用压力
- Evidence type: TABLE
- Evidence: 两张规格表列出各压力档、总体使用压力和调整螺杆每转变化量。

## VALVE-Q-0012

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: BLS / BLG 与 BLB 压力平衡阀
- Model / Scope: 顺序夹紧与释放动作

### Question

说明 BLS/BLG 与 BLB 组合回路从供压、顺序夹紧到释放的动作逻辑，并给出 BLB 的代表释放比。

### Standard Answer

供压时，P 口压力先供给前级回路；当压力超过 BLS/BLG 的设定值后，顺序阀开启并向 CYL 侧供压，形成后续夹紧动作。释放时，BLB 压力平衡阀使 CYL 侧压力按先导关系释放，代表释放比约为 1:20。顺序阀设定值必须与实际使用压力保持规定差值。

### Scoring Standard

- P1 [20]: 说明初始供压先作用于前级回路。
- P2 [20]: 说明达到 BLS/BLG 设定值后顺序阀开启。
- P3 [20]: 说明开启后向 CYL 侧供压并形成后续夹紧。
- P4 [20]: 说明释放由 BLB 压力平衡阀按先导关系完成。
- P5 [20]: 代表释放比约为 1:20。

### Accepted Variants

- “二十比一的压力比”可按方向明确时接受。

### Forbidden Errors

- 声称顺序阀在达到设定压力前即向后级完全供压。

### Tolerance

- 释放比接受 1:19～1:21 的近似表述。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 21-30
- Printed page: 1583-1592
- Section: 顺序阀与压力平衡阀回路
- Local scope path: BLS / BLG / BLB > 动作回路
- Evidence type: CIRCUIT
- Evidence: 回路图与动作说明给出设定压力以上开启、CYL 供压及 BLB 约 1:20 的释放关系。

## VALVE-Q-0013

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: BLS / BLG 顺序阀
- Model / Scope: 设定压力与并联使用边界

### Question

BLS/BLG 在设定压力、实际使用压力和并联多阀设定方面有哪些必须遵守的压差要求？

### Standard Answer

型号中的设定压力必须写明单位；实际使用压力与设定压力之间至少保持 1 MPa 差值。并联使用多个 BLS 或 BLG 时，各阀设定压力之间也至少相差 1 MPa，以避免动作顺序不明确或相互干扰。

### Scoring Standard

- P1 [17]: 设定压力必须带明确压力单位。
- P2 [17]: 实际使用压力与设定压力至少相差 1 MPa。
- P3 [17]: 并联 BLS 的设定值彼此至少相差 1 MPa。
- P4 [17]: 并联 BLG 的设定值彼此至少相差 1 MPa。
- P5 [16]: 压差要求用于保持明确动作顺序。
- P6 [16]: 压差要求用于避免并联阀相互干扰。

### Accepted Variants

- “不得小于 1 MPa”与“至少 1 MPa”等价。

### Forbidden Errors

- 将压差要求写成 0.1 MPa 或仅作为建议项。

### Tolerance

- 最小压差精确判定为 1 MPa。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 23, 25
- Printed page: 1585, 1587
- Section: 顺序阀使用注意
- Local scope path: BLS / BLG > 设定压力注意事项
- Evidence type: CAUTION
- Evidence: 两页注意事项均要求使用压力与设定压力、并联各设定值之间保持至少 1 MPa。

## VALVE-Q-0014

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: BMA / BMG 减压阀
- Model / Scope: 一次侧、二次侧与最小压差

### Question

列出 BMA/BMG 三个压力档的一次侧范围、二次侧设定范围和最小压差，并给出共通最小受压面积。

### Standard Answer

代码 3：一次侧 2～7 MPa、二次侧 1～6 MPa、最小压差 1 MPa；代码 5：一次侧 6～30 MPa、二次侧 3～14 MPa、最小压差 3 MPa；代码 7：一次侧 9～30 MPa、二次侧 6～27 MPa、最小压差 3 MPa。共通最小受压面积为 23.3 cm²。

### Scoring Standard

- P1 [10]: 代码 3 一次侧范围为 2～7 MPa。
- P2 [10]: 代码 3 二次侧范围为 1～6 MPa。
- P3 [10]: 代码 3 最小压差为 1 MPa。
- P4 [10]: 代码 5 一次侧范围为 6～30 MPa。
- P5 [10]: 代码 5 二次侧范围为 3～14 MPa。
- P6 [10]: 代码 5 最小压差为 3 MPa。
- P7 [10]: 代码 7 一次侧范围为 9～30 MPa。
- P8 [10]: 代码 7 二次侧范围为 6～27 MPa。
- P9 [10]: 代码 7 最小压差为 3 MPa。
- P10 [10]: 共通最小受压面积为 23.3 cm²。

### Accepted Variants

- 面积单位可写作 `cm2`。

### Forbidden Errors

- 交换一次侧供给范围和二次侧设定范围。

### Tolerance

- 表中压力范围和面积精确判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 47, 49
- Printed page: 1609, 1611
- Section: BMA / BMG 规格
- Local scope path: 减压阀 > 压力范围与最小压差
- Evidence type: TABLE
- Evidence: BMA 与 BMG 规格表给出相同的三档一次侧、二次侧、最小压差和受压面积。

## VALVE-Q-0015

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: BMA / BMG 减压阀
- Model / Scope: 连接形式、耐压和质量对照

### Question

对照 BMA 与 BMG 的连接形式、三档耐压、温度、流体和质量。

### Standard Answer

BMA 支持 Rc1/4 外配管、G 板式和 K 型 BK 连接；BMG 仅 G 板式。两系列代码 3 的耐压为 10.5 MPa，代码 5 和 7 的耐压均为 37.5 MPa；共通温度 0～70 ℃，使用 ISO VG32 一般液压油。BMA 质量约 1.5 kg，BMG 约 0.8 kg。

### Scoring Standard

- P1 [10]: BMA 支持 Rc1/4 外配管。
- P2 [9]: BMA 支持 G 板式连接。
- P3 [9]: BMA 支持 K 型 BK 连接。
- P4 [9]: BMG 仅支持 G 板式连接。
- P5 [9]: 代码 3 耐压为 10.5 MPa。
- P6 [9]: 代码 5 耐压为 37.5 MPa。
- P7 [9]: 代码 7 耐压为 37.5 MPa。
- P8 [9]: 共通使用温度为 0～70 ℃。
- P9 [9]: 共通使用流体为 ISO VG32 一般液压油。
- P10 [9]: BMA 质量约 1.5 kg。
- P11 [9]: BMG 质量约 0.8 kg。

### Accepted Variants

- 质量可带“约”字。

### Forbidden Errors

- 声称 BMG 标准提供 Rc1/4 外配管连接。

### Tolerance

- 连接形式和耐压精确判定；质量 ±0.05 kg。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 47, 49
- Printed page: 1609, 1611
- Section: BMA / BMG 型号与规格
- Local scope path: 减压阀 > 系列对照
- Evidence type: TABLE
- Evidence: 两系列型号和规格表共同给出连接形式、耐压、温度、流体和质量。

## VALVE-Q-0016

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: JSS 弹簧蓄能器
- Model / Scope: 容量、安装方向和配管组合

### Question

对照 JSS 的三个排出容积代码，并说明水平安装时外配管/复合配管的接口方向选择。

### Standard Answer

`02`、`05`、`10` 分别表示 2.5、5.0、10 cm³。水平安装代码为 `H`，对于外配管 `C/S` 或复合配管 `GC/GS`，还需指定接口方向：`A` 为上方，`B` 为侧方；垂直安装为 `V`，不套用水平安装的 A/B 方向定义。

### Scoring Standard

- P1 [15]: `02` 对应 2.5 cm³。
- P2 [15]: `05` 对应 5.0 cm³。
- P3 [14]: `10` 对应 10 cm³。
- P4 [14]: `H` 正确解释为水平安装。
- P5 [14]: 水平安装时 `A` 为上方接口。
- P6 [14]: 水平安装时 `B` 为侧方接口。
- P7 [14]: A/B 接口方向定义不直接套用于 `V` 垂直安装。

### Accepted Variants

- “顶部”可等同于“上方”。

### Forbidden Errors

- 将 A/B 解释为蓄能器压力档。

### Tolerance

- 容积值按型号表精确判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 33
- Printed page: 1595
- Section: JSS 型号表示
- Local scope path: JSS > 排出容积、安装和接口方向
- Evidence type: TABLE
- Evidence: 型号表定义三档容积、H/V 安装和仅对特定水平配管有效的 A/B 方向。

## VALVE-Q-0017

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: BU 单次输出增压器
- Model / Scope: BU5020 / BU5030 / BU5060 压力与排出量

### Question

列出 BU5020、BU5030、BU5060 的一次侧输入压力、顺序阀设定压力、二次侧输出压力和排出量。

### Standard Answer

BU5020：输入 5.0～11.4 MPa，设定 4.0～9.1 MPa，输出 11.0～25.0 MPa，排出 30 cm³；BU5030：输入 3.0～8.4 MPa，设定 2.3～6.7 MPa，输出 9.0～25.2 MPa，排出 23 cm³；BU5060：输入 1.5～4.2 MPa，设定 1.1～3.2 MPa，输出 9.0～25.2 MPa，排出 12 cm³。

### Scoring Standard

- P1 [8]: BU5020 输入范围为 5.0～11.4 MPa。
- P2 [8]: BU5020 顺序阀设定范围为 4.0～9.1 MPa。
- P3 [8]: BU5020 输出范围为 11.0～25.0 MPa。
- P4 [8]: BU5020 排出量为 30 cm³。
- P5 [8]: BU5030 输入范围为 3.0～8.4 MPa。
- P6 [8]: BU5030 顺序阀设定范围为 2.3～6.7 MPa。
- P7 [8]: BU5030 输出范围为 9.0～25.2 MPa。
- P8 [8]: BU5030 排出量为 23 cm³。
- P9 [8]: BU5060 输入范围为 1.5～4.2 MPa。
- P10 [7]: BU5060 顺序阀设定范围为 1.1～3.2 MPa。
- P11 [7]: BU5060 输出范围为 9.0～25.2 MPa。
- P12 [7]: BU5060 排出量为 12 cm³。
- P13 [7]: 正确区分输入、顺序设定、输出和排出容积四列。

### Accepted Variants

- 容积单位可写作 `cm3`。

### Forbidden Errors

- 将排出容积当作连续流量，或交换输入和输出压力。

### Tolerance

- 表中范围和容量精确判定。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 61
- Printed page: 1623
- Section: BU 规格
- Local scope path: BU > 规格表 > 压力范围与排出量
- Evidence type: TABLE
- Evidence: BU 规格表逐型号列出输入、顺序设定、输出和一次排出量。

## VALVE-Q-0018

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: BU 单次输出增压器
- Model / Scope: BU5030 增压压力曲线

### Question

从 BU 增压压力曲线读取：BU5030 在一次侧输入压力 5 MPa 时，二次侧输出压力约为多少？

### Standard Answer

沿横轴 5 MPa 找到 BU5030 曲线并读纵轴，二次侧输出压力约为 15 MPa。

### Scoring Standard

- P1 [20]: 明确读取的是 BU5030 曲线。
- P2 [20]: 横轴输入值正确定位为 5 MPa。
- P3 [20]: 纵轴输出读数约为 15 MPa。
- P4 [20]: 正确区分一次侧输入与二次侧输出。
- P5 [20]: 说明该答案来自视觉读图而非仅用铭牌增压比公式替代。

### Accepted Variants

- 14.5～15.5 MPa 范围内的视觉读数可接受。

### Forbidden Errors

- 只写“3 倍”而不给出图上输出压力，或读取 BU5020/BU5060 曲线。

### Tolerance

- 视觉读图公差：14.5～15.5 MPa。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 61
- Printed page: 1623
- Section: 增压压力图
- Local scope path: BU > 一次侧输入压力—二次侧输出压力曲线 > BU5030
- Evidence type: CHART
- Evidence: BU5030 曲线在横轴 5 MPa 附近对应纵轴约 15 MPa。

## VALVE-Q-0019

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: AU 连续输出增压器
- Model / Scope: 正确回路与启动顺序

### Question

说明 AU 安装到三位换向阀回路时的中位连接要求，以及执行器释放与增压口供压的正确先后顺序。

### Standard Answer

三位换向阀中位必须使 A、B 与 T 连通，不能使用 A/B 封闭的中位。启动时先确认执行器已完全释放，再向增压口供压；停机或拆卸快速接头前必须先停止供压并确认压力释放。

### Scoring Standard

- P1 [17]: 三位阀中位必须使 A 与 T 连通。
- P2 [17]: 三位阀中位必须使 B 与 T 连通。
- P3 [17]: 禁止采用 A/B 封闭的中位。
- P4 [17]: 必须在执行器完全释放后再向增压口供压。
- P5 [16]: 拆卸快速接头前停止供压。
- P6 [16]: 拆卸快速接头前确认压力已经释放。

### Accepted Variants

- “A、B 均回油箱”可等同于“A、B 与 T 连通”。

### Forbidden Errors

- 在执行器尚未释放时先向增压口供压。

### Tolerance

- N/A

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 57
- Printed page: 1619
- Section: AU 使用注意事项
- Local scope path: AU > 回路连接与启动顺序
- Evidence type: PROCEDURE
- Evidence: 注意事项明确禁止 A/B 封闭中位，并规定完全释放后再供给增压口。

## VALVE-Q-0020

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: AU 连续输出增压器
- Model / Scope: 流量、泄漏、脉动与多机边界

### Question

列出 AU 使用中与二次压力、内部泄漏、脉动及多台并用有关的四类风险和对应措施。

### Standard Answer

二次压力升高时输出流量会下降，重载行程时间会增加；二次侧内部泄漏会使增压器不能正常增压；控制条件可能造成脉动，可增设蓄能器或降低一次侧输入压力；在同一低压单元并用多台 AU 会加剧压力波动，应评估容量与回路稳定性。另应注意平衡停止泵回路中 P1 与 T/D 间的内泄漏可能缩短泵寿命。

### Scoring Standard

- P1 [13]: 二次压力升高会使输出流量下降。
- P2 [13]: 重载时行程时间会增加。
- P3 [13]: 二次侧内部泄漏会导致不能正常增压。
- P4 [13]: 增设蓄能器可缓解脉动。
- P5 [12]: 降低一次侧输入压力可缓解脉动。
- P6 [12]: 多台 AU 并用会加剧压力波动。
- P7 [12]: P1 与 T/D 间内泄漏可能缩短泵寿命。
- P8 [12]: 多机应用应评估低压单元容量和回路稳定性。

### Accepted Variants

- “压力不稳”可等同于“压力波动”。

### Forbidden Errors

- 声称二次压力越高输出流量越大。

### Tolerance

- N/A

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 57
- Printed page: 1619
- Section: AU 使用注意事项
- Local scope path: AU > 性能和回路风险
- Evidence type: CAUTION
- Evidence: 注意事项逐项说明压力—流量关系、内泄漏、脉动、多机并用和泵寿命风险。

## VALVE-Q-0021

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: BH 手动无泄漏阀组
- Model / Scope: 保压功能与防误操作步骤

### Question

说明 BH 在一次侧供压切断后的功能、三种回路代码含义，以及手动切换的防误操作步骤。

### Standard Answer

BH 在一次侧供压切断后仍保持二次侧压力，直到手柄被切换。回路代码 `A` 为常开、`B` 为常闭、`NN` 为双回路。切换时先拉起防误操作手柄，再将控制杆向规定方向转动约 ±45°；不得直接强扳控制杆。

### Scoring Standard

- P1 [15]: 说明一次侧供压切断后仍保持二次侧压力。
- P2 [15]: `A` 正确解释为常开。
- P3 [14]: `B` 正确解释为常闭。
- P4 [14]: `NN` 正确解释为双回路。
- P5 [14]: 先拉起防误操作手柄。
- P6 [14]: 再将控制杆转动约 ±45°。
- P7 [14]: 不得越过防误操作步骤直接强扳控制杆。

### Accepted Variants

- “安全锁杆”可等同于“防误操作手柄”。

### Forbidden Errors

- 颠倒先拉起防误操作手柄和转动控制杆的顺序。

### Tolerance

- 控制杆角度接受约 40°～50°。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 77
- Printed page: 1639
- Section: BH 动作与回路
- Local scope path: BH > 保压功能、回路代码和手柄操作
- Evidence type: PROCEDURE
- Evidence: 产品说明、回路符号和操作图给出断压保压、A/B/NN 和两步防误操作。

## VALVE-Q-0022

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: BC 电气无泄漏阀组
- Model / Scope: 电气/气动控制与失压保压边界

### Question

说明 BC 的控制方式、一次侧供压切断后的状态，以及 `C`、`Z`、`U`、`YY` 回路代码的含义。为什么不能只根据“电气控制”推断掉电后自动卸压？

### Standard Answer

BC 以空气电磁阀控制无泄漏阀；一次侧供压切断后，二次侧压力仍保持，直到电气/空气控制使阀切换。`C` 为常开，`Z` 为常闭，`U` 为双电磁阀规格，`YY` 为双回路。无泄漏结构的目的正是保持封闭状态，因此掉电行为必须按具体回路和控制状态判断，不能假定自动卸压。

### Scoring Standard

- P1 [15]: 由空气电磁阀控制无泄漏阀。
- P2 [15]: 一次侧供压切断后仍保持二次侧压力。
- P3 [14]: `C` 正确解释为常开。
- P4 [14]: `Z` 正确解释为常闭。
- P5 [14]: `U` 正确解释为双电磁阀规格。
- P6 [14]: `YY` 正确解释为双回路。
- P7 [14]: 掉电行为必须按回路和控制状态判断，不能假定自动卸压。

### Accepted Variants

- “气控电磁阀”可等同于“空气电磁阀”。

### Forbidden Errors

- 声称任何 BC 回路一旦掉电都会自动释放二次侧压力。

### Tolerance

- N/A

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 79
- Printed page: 1641
- Section: BC 功能与回路符号
- Local scope path: BC > 电气/气动控制、保压与回路代码
- Evidence type: CIRCUIT
- Evidence: BC 说明与符号表定义空气电磁阀控制、断压保压和 C/Z/U/YY。

## VALVE-Q-0023

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: 液压阀与液压单元
- Model / Scope: VALVE_R00_2023KW_C1N.pdf :: 安装清洁、密封带与空气排放

### Question

给出安装液压阀时的清洁、密封带缠绕和回路排气步骤，包括排气时的压力限制与紧固动作。

### Standard Answer

安装前清洁阀口、配管和接头，清除切屑和异物。缠密封带时从管端保留 1～2 个螺纹不缠。排气时将回路压力降到 2 MPa 以下，将相关端口锁紧螺母松开约一圈，摇动配管使含气液压油排出，然后重新拧紧；高点或末端难以排气时设置自动排气阀。初次运行后还应复查并紧固连接件。

### Scoring Standard

- P1 [10]: 安装前清洁阀口、配管和接头。
- P2 [10]: 清除切屑和异物以防泄漏或动作不良。
- P3 [10]: 密封带从管端保留 1～2 个螺纹。
- P4 [10]: 排气时压力降到 2 MPa 以下。
- P5 [10]: 相关锁紧螺母松开约一圈。
- P6 [10]: 排气时摇动配管。
- P7 [10]: 排出含气液压油后重新拧紧锁紧螺母。
- P8 [10]: 高点或末端可设置自动排气阀。
- P9 [10]: 初次运行后复查连接件。
- P10 [10]: 初次运行后紧固松动连接件。

### Accepted Variants

- “不超过 2 MPa”可接受，但不得写成正常高压下排气。

### Forbidden Errors

- 在高压状态完全拆下接头排气，或让密封带覆盖管端第一扣螺纹。

### Tolerance

- 压力上限精确判定为 2 MPa；保留螺纹接受 1～2 扣。

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 81
- Printed page: 1725
- Section: 安装注意事项
- Local scope path: 共通注意事项 > 清洁、密封和空气排放
- Evidence type: PROCEDURE
- Evidence: 安装页逐项规定清洁、密封带留扣、2 MPa 以下松一圈排气、摇管和复紧。

## VALVE-Q-0024

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: 液压阀与液压单元
- Model / Scope: VALVE_R00_2023KW_C1N.pdf :: 操作与维护安全

### Question

概括液压阀操作、拆卸和维护时必须执行的安全隔离与定期检查项目。

### Standard Answer

仅由受过培训的人员操作；操作或拆卸前停止设备，使液压压力和电源均为零并等待部件冷却，防止夹伤，禁止擅自改造。维护时检查并紧固配管连接、安装螺栓、螺母、挡圈和夹具，检查液压油老化、异常声音和异常动作；自动接头会带入空气，应定期排气。接触基准面和圆柱面应保持清洁，产品存放在阴凉干燥处，维修应交由制造商或授权方处理。

### Scoring Standard

- P1 [6]: 仅由受过培训的人员操作。
- P2 [6]: 拆卸前停止设备。
- P3 [6]: 拆卸前使液压压力为零。
- P4 [6]: 拆卸前切断电源。
- P5 [6]: 拆卸前等待部件冷却。
- P6 [5]: 识别夹伤风险并采取防护。
- P7 [5]: 禁止擅自改造。
- P8 [5]: 检查并紧固配管连接。
- P9 [5]: 检查安装螺栓。
- P10 [5]: 检查螺母。
- P11 [5]: 检查挡圈。
- P12 [5]: 检查夹具。
- P13 [5]: 检查液压油老化。
- P14 [5]: 检查异常声音。
- P15 [5]: 检查异常动作。
- P16 [5]: 自动接头带入空气时应定期排气。
- P17 [5]: 保持接触基准面和圆柱面清洁。
- P18 [5]: 产品应存放在阴凉干燥处。
- P19 [5]: 维修应由制造商或授权方处理。

### Accepted Variants

- “断电并卸压”可概括两个隔离动作，但两项必须都出现。

### Forbidden Errors

- 仅切断电源而不卸压就拆卸，或允许用户自行改造和内部维修。

### Tolerance

- N/A

### Source

- PDF: VALVE_R00_2023KW_C1N.pdf
- Physical page: 83
- Printed page: 1727
- Section: 操作与维护注意事项
- Local scope path: 共通注意事项 > 安全隔离、检查与维修
- Evidence type: CAUTION
- Evidence: 操作维护页明确要求培训、零压断电、冷却、防夹、禁改造、定期检查排气与授权维修。
