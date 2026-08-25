---
schema_version: will-ai-question-bank/v1
source_pdf: TNE_R01_2026KW_C1N.pdf
source_sha256: 898ac3440cc8b798790b20e0ed804d1f2f99ba6c5fe3697c161ad3bd01e81f16
source_pages: 40
question_bank_version: V1
product_scope: TNE
---

# TNE_R01_2026KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `TNE_R01_2026KW_C1N.pdf`
- SHA-256: `898ac3440cc8b798790b20e0ed804d1f2f99ba6c5fe3697c161ad3bd01e81f16`
- Physical pages: 40
- Product scope: TNE 外螺纹型油压支撑器及 PDF 内直接适用的安装、传感、清洁和通用注意事项

## 2. Scope

本题库覆盖 TNE 的型号语法、液压上升型与弹簧上升型动作、标准型与行程加长型规格、支撑力、空气传感、喷气清洁、安装尺寸与力矩、附件以及适用于 TNE 的安全和维护要求。公司介绍、销售网点、纯目录导航和与 TNE 无直接绑定的其他产品数据不作为考核对象。

## 3. Question Statistics

- Total: 8
- MODEL: 2
- SPEC_LOOKUP: 2
- TABLE: 3
- PROCEDURE: 1

## 4. Questions

## TNE-Q-0001

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 全系列型号表示

### Question

说明 TNE 型号 `TNE0300-LM-E` 中主体尺寸、设计编号、柱塞弹簧力、动作确认方式和选配项分别表示什么。

### Standard Answer

`030` 表示主体外螺纹尺寸 M30×1.5；`0` 是设计编号；`L` 表示弱柱塞弹簧；`M` 表示空气传感器连接型；`E` 表示弹簧上升型。

### Scoring Standard

- P1 [20]: `030` 正确解释为 M30×1.5 主体尺寸。
- P2 [20]: `0` 正确解释为设计编号。
- P3 [20]: `L` 正确解释为弱柱塞弹簧。
- P4 [20]: `M` 正确解释为空气传感器连接型。
- P5 [20]: `E` 正确解释为弹簧上升型。

### Accepted Variants

- “弱弹簧型”可等同于“弱柱塞弹簧”。

### Forbidden Errors

- 将 `M` 解释为主体尺寸或将 `E` 解释为液压上升型。

### Tolerance

- N/A

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 7
- Printed page: 1033
- Section: 型号表示
- Local scope path: TNE > 型号表示 > 字段 1 至 5
- Evidence type: TEXT
- Evidence: 型号表示页逐项定义主体尺寸、设计编号、柱塞弹簧力、动作确认 `M` 和选配项 `E`；M30×1.5 对应主体尺寸 030。

## TNE-Q-0002

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 型号组合规则

### Question

列出 TNE 选配项字段中无符号、Q、E、EQ 的含义，并说明空气传感器连接型与行程加长型组合时应如何处理。

### Standard Answer

无符号表示液压上升标准型；Q 表示液压上升行程加长型；E 表示弹簧上升型；EQ 表示弹簧上升行程加长型。空气传感器连接型与 Q 或 EQ 组合（M-Q、M-EQ）需要另行咨询，不能按普通标准组合直接选用。

### Scoring Standard

- P1 [20]: 说明无符号是液压上升标准型。
- P2 [20]: 说明 Q 是液压上升行程加长型。
- P3 [20]: 说明 E 是弹簧上升型。
- P4 [20]: 说明 EQ 是弹簧上升行程加长型。
- P5 [20]: 说明 M-Q、M-EQ 需另行咨询。

### Accepted Variants

- “标准液压上升型”可等同于“液压上升标准型”。

### Forbidden Errors

- 声称 M-Q 或 M-EQ 是无需确认即可订购的常规组合。

### Tolerance

- N/A

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 7
- Printed page: 1033-1034
- Section: 型号表示
- Local scope path: TNE > 型号表示 > 选配项及组合注意事项
- Evidence type: TABLE
- Evidence: 选配项定义表给出无符号、Q、E、EQ 的动作类型；组合矩阵下方注明 TNE-M-Q、TNE-M-EQ 请另行咨询。

## TNE-Q-0003

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE0260/TNE0300/TNE0360/TNE0450 通用压力与环境规格

### Question

TNE 全系列的最高使用压力、最低动作压力、使用温度和规定使用流体分别是什么？

### Standard Answer

最高使用压力 35 MPa；最低动作压力 7 MPa；使用温度 0～70 ℃；使用流体为相当于 ISO 粘度等级 ISO-VG-32 的一般液压油。

### Scoring Standard

- P1 [25]: 最高使用压力 35 MPa。
- P2 [25]: 最低动作压力 7 MPa。
- P3 [25]: 使用温度 0～70 ℃。
- P4 [25]: 使用流体为相当于 ISO-VG-32 的一般液压油。

### Accepted Variants

- `ISO VG 32` 与 `ISO-VG-32` 等价。

### Forbidden Errors

- 将 7 MPa 误作最高压力，或省略压力单位。

### Tolerance

- 数值和范围按表中值精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 8
- Printed page: 1034
- Section: 规格
- Local scope path: TNE > 规格 > 标准/E 型与 Q/EQ 型共通条件
- Evidence type: TABLE
- Evidence: 两组规格表均列出最高 35 MPa、最低 7 MPa、0～70 ℃和 ISO-VG-32 一般液压油。

## TNE-Q-0004

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE0260/TNE0300/TNE0360/TNE0450 支撑力公式

### Question

分别写出 TNE0260、TNE0300、TNE0360、TNE0450 的支撑力计算公式。P 的单位是什么？

### Standard Answer

支撑力单位为 kN，P 为供给油压（MPa）。TNE0260：0.30×P−1.04；TNE0300：0.36×P−1.08；TNE0360：0.56×P−1.68；TNE0450：0.78×P−2.33。

### Scoring Standard

- P1 [20]: TNE0260 公式为 0.30×P−1.04 kN。
- P2 [20]: TNE0300 公式为 0.36×P−1.08 kN。
- P3 [20]: TNE0360 公式为 0.56×P−1.68 kN。
- P4 [20]: TNE0450 公式为 0.78×P−2.33 kN。
- P5 [20]: P 明确为供给油压，单位 MPa。

### Accepted Variants

- 乘号可写作 `×`、`*` 或省略为系数乘 P。

### Forbidden Errors

- 将支撑力结果单位写成 N，或交换不同主体尺寸的公式。

### Tolerance

- 公式系数和常数精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 9
- Printed page: 1035-1036
- Section: 能力曲线图
- Local scope path: TNE > 支撑力曲线图 > 支撑力表与计算公式
- Evidence type: TABLE
- Evidence: 支撑力表按四种主体尺寸列出公式，并在注释中将 P 定义为供给油压 MPa。

## TNE-Q-0005

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE0260/TNE0300/TNE0360/TNE0450 在 21 MPa 下的支撑力

### Question

供给油压为 21 MPa 时，TNE0260、TNE0300、TNE0360、TNE0450 的表列支撑力分别是多少？

### Standard Answer

依次为 5.2 kN、6.5 kN、10.1 kN、14.0 kN。

### Scoring Standard

- P1 [25]: TNE0260 为 5.2 kN。
- P2 [25]: TNE0300 为 6.5 kN。
- P3 [25]: TNE0360 为 10.1 kN。
- P4 [25]: TNE0450 为 14.0 kN。

### Accepted Variants

- 允许保留无意义尾零，如 5.20 kN。

### Forbidden Errors

- 模型与数值错配，或遗漏 kN 单位。

### Tolerance

- 采用表列值精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 9
- Printed page: 1035-1036
- Section: 能力曲线图
- Local scope path: TNE > 支撑力曲线图 > 21 MPa 行
- Evidence type: TABLE
- Evidence: 支撑力表 21 MPa 行按 TNE0260 至 TNE0450 顺序列出 5.2、6.5、10.1、14.0 kN。

## TNE-Q-0006

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 标准型与 Q 型柱塞行程

### Question

比较 TNE0260、TNE0300、TNE0360、TNE0450 的标准型与 Q 型柱塞行程。

### Standard Answer

标准型柱塞行程依次为 6.5、8、10、12 mm；Q 型依次为 13、16、20、24 mm，均为对应标准型的 2 倍。

### Scoring Standard

- P1 [35]: 标准型四个行程依次为 6.5、8、10、12 mm。
- P2 [35]: Q 型四个行程依次为 13、16、20、24 mm。
- P3 [30]: 正确指出 Q 型对应行程为标准型的 2 倍。

### Accepted Variants

- 可分别逐型号陈述，不要求使用“依次”形式。

### Forbidden Errors

- 将有效行程与柱塞行程混为一谈。

### Tolerance

- 行程值按表中值精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 8
- Printed page: 1034
- Section: 规格
- Local scope path: TNE > 规格 > 标准/E 与 Q/EQ 柱塞行程行
- Evidence type: TABLE
- Evidence: 标准/E 表与 Q/EQ 表分别列出四种主体尺寸的柱塞行程 6.5/8/10/12 mm 和 13/16/20/24 mm。

## TNE-Q-0007

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 与 TNE-E 动作原理

### Question

说明液压上升型 TNE 与弹簧上升型 TNE-E 在油压关闭时的初始状态、接触工件方式以及供压后的共同抱紧结果。

### Standard Answer

TNE 在油压关闭时柱塞下降；供油后柱塞由液压上升并以柱塞弹簧力接触工件，小活塞到达上升端后抱紧机构抱紧柱塞。TNE-E 在油压关闭时柱塞由弹簧保持上升，放入工件后靠工件重量压至着座面；供油后抱紧机构同样抱紧柱塞。两者抱紧后均能承受来自上方的外力而不下降。

### Scoring Standard

- P1 [20]: 说明 TNE 油压关闭时柱塞下降。
- P2 [20]: 说明 TNE 供油后液压上升并接触工件。
- P3 [20]: 说明 TNE-E 油压关闭时柱塞弹簧上升。
- P4 [20]: 说明工件靠自重将 TNE-E 柱塞压至着座面。
- P5 [20]: 说明供油后抱紧，抱紧后承受上方外力不下降。

### Accepted Variants

- “锁紧柱塞”可等同于“抱紧柱塞”。

### Forbidden Errors

- 声称 TNE-E 靠液压使柱塞上升，或 TNE 抱紧后柱塞仍可自由下降。

### Tolerance

- N/A

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 5-6
- Printed page: 1031-1032
- Section: 动作原理
- Local scope path: TNE > 动作说明 > 液压上升型与弹簧上升型
- Evidence type: STATE_DIAGRAM
- Evidence: 两组动作图分别给出油压 OFF、接触/着座和油压 ON 抱紧状态，并说明抱紧后柱塞不会因上方外力下降。

## TNE-Q-0008

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 柱塞动作速度控制

### Question

TNE 柱塞全行程动作时间的标准是多少？应使用什么类型和节流方向的流量调整阀？动作过快和阀启开压力过高分别有什么风险？

### Standard Answer

全行程动作时间标准约为 0.5～1 秒。应使用启开压力 0.1 MPa 以下、带单向阀的流量调整阀，并采用进油节流。动作过快会使柱塞接触工件时反弹，可能在柱塞与工件有间隙时抱紧；阀启开压力过高会使释放时柱塞无法复位。

### Scoring Standard

- P1 [20]: 全行程动作时间约 0.5～1 秒。
- P2 [20]: 使用带单向阀的流量调整阀。
- P3 [20]: 采用进油节流且启开压力不高于 0.1 MPa。
- P4 [20]: 动作过快会反弹并可能带间隙抱紧。
- P5 [20]: 启开压力过高会导致释放时柱塞无法复位。

### Accepted Variants

- “单向节流阀”可等同于“带单向阀的流量调整阀”。

### Forbidden Errors

- 建议采用回油节流控制 TNE 的上升速度。

### Tolerance

- 时间范围和启开压力按规定值精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 油压支撑器注意事项
- Local scope path: 设计方面的注意事项 > 8) 通过调整供油量调整柱塞的动作时间
- Evidence type: TEXT
- Evidence: 注意事项规定全行程 0.5～1 秒、带单向阀的进油节流和启开压力 0.1 MPa 以下，并列出反弹间隙抱紧及无法复位的后果。
