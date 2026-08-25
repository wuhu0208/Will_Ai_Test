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

### 2.1 覆盖原则

- `HIGH`：型号、动作、规格、能力、传感、清洁、安装和关键故障后果均映射到题目。
- `MEDIUM`：直接适用于 TNE 的通用液压施工、维护、保修和外配管安装座映射到代表题。
- `LOW/EXCLUDED`：纯目录、销售联系方式、其他产品专属数据、重复的新旧标示对照及空白页保留处置理由，不生成题目。

### 2.2 图表与计算边界

- 离散支撑力表使用 `TABLE`；载荷/变位连续曲线使用 `CHART`，不以公式替代视觉读图。
- 空气传感和喷气清洁接触力使用 PDF 公式与明确输入进行确定性计算；最终值采用 `ROUND_HALF_UP`。

### 2.3 来源清单

| Coverage ID | 物理页 | 局部范围 | Evidence type | 可测试对象 / 范围决定 | Priority / Disposition |
|---|---:|---|---|---|---|
| TNE-SI-001 | 1-2 | 封面与空白 | VISUAL | 无耐久技术事实 | EXCLUDED：无可测试对象 |
| TNE-SI-002 | 3-4 | TNE 总览、结构与特征 | TEXT + DRAWING | 产品边界、结构与耐环境设计；`TNE-Q-0001`-`0002` | MEDIUM：型号边界已映射，宣传描述排除 |
| TNE-SI-003 | 5-6 | 液压/弹簧上升动作 | STATE_DIAGRAM | 动作次序与抱紧结果；`TNE-Q-0007` | HIGH：已映射 |
| TNE-SI-004 | 7-8 | 型号表示与规格 | MODEL + TABLE + FORMULA | 字段、组合、压力、行程、弹簧力；`TNE-Q-0001`-`0004`、`0006`、`0015` | HIGH：已映射 |
| TNE-SI-005 | 9-12 | 支撑力与载荷/变位曲线 | TABLE + FORMULA + CHART | 四尺寸支撑力、公式与视觉变位；`TNE-Q-0004`-`0005`、`0025` | HIGH：已映射；物理页 12 空白半页无对象 |
| TNE-SI-006 | 13-20 | 标准/Q/E/EQ/M 外形与安装 | DRAWING + TABLE + CAUTION | 螺纹、力矩、接触螺栓与传感型结构；`TNE-Q-0009`-`0010` | HIGH：代表性安装事实已映射，重复尺寸保留查阅 |
| TNE-SI-007 | 21-22 | 空气传感器流程 | STATE_DIAGRAM + TABLE + FORMULA | 供气、器件、ON/OFF、接触力与运行风险；`TNE-Q-0011`-`0012`、`0014`、`0017` | HIGH：已映射 |
| TNE-SI-008 | 23-24 | 喷气清洁与弹簧设计 | STATE_DIAGRAM + FORMULA + TABLE | 清洁压力、接触力和弹簧边界；`TNE-Q-0013`、`0016`、`0021` | HIGH：已映射；自制弹簧细部尺寸为专项设计参考 |
| TNE-SI-009 | 25-28 | TNE 支撑器注意事项 | TEXT + DRAWING + TABLE | 速度、呼吸、接触螺栓、底面承载和安装力矩；`TNE-Q-0008`-`0010`、`0018`-`0021` | HIGH：已映射 |
| TNE-SI-010 | 29-32 | 液压通用施工、操作、维护与保修 | TEXT + PROCEDURE + TABLE | 排气、安全、维护、保修；`TNE-Q-0022`、`0024` | MEDIUM：TNE 适用事实已映射 |
| TNE-SI-011 | 33-34 | 粗糙度与 O 形圈标示变更 | TABLE | 新旧标示对照 | LOW：重复标准对照，清单保留 |
| TNE-SI-012 | 35-38 | TNEZ-S/SQ 外配管安装座 | DRAWING + TABLE + MODEL | TNE/TNE-Q 适用边界；`TNE-Q-0023` | MEDIUM：已映射；物理页 38 MEMO 排除 |
| TNE-SI-013 | 39-40 | 公司与销售网点 | TEXT | 联系方式与公司信息 | EXCLUDED：非耐久技术知识 |

## 3. Question Statistics

- Total: 25
- Direct TNE: 22
- Document Common: 2
- Accessory: 1
- MODEL: 2
- SPEC_LOOKUP: 7
- TABLE: 4
- CALCULATION: 2
- CHART: 1
- PROCEDURE: 5
- CAUTION: 4

## 4. Questions

## TNE-Q-0001

**Type: MODEL**

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

**Type: MODEL**

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

**Type: SPEC_LOOKUP**

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

**Type: SPEC_LOOKUP**

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
- P5 [10]: P 明确为供给油压。
- P6 [10]: P 的单位为 MPa。

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

**Type: TABLE**

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

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 标准型与 Q 型柱塞行程

### Question

比较 TNE0260、TNE0300、TNE0360、TNE0450 的标准型与 Q 型柱塞行程。

### Standard Answer

标准型柱塞行程依次为 6.5、8、10、12 mm；Q 型依次为 13、16、20、24 mm，均为对应标准型的 2 倍。

### Scoring Standard

- P1 [11]: TNE0260 标准型为 6.5 mm。
- P2 [11]: TNE0300 标准型为 8 mm。
- P3 [11]: TNE0360 标准型为 10 mm。
- P4 [11]: TNE0450 标准型为 12 mm。
- P5 [11]: TNE0260-Q 为 13 mm。
- P6 [11]: TNE0300-Q 为 16 mm。
- P7 [11]: TNE0360-Q 为 20 mm。
- P8 [11]: TNE0450-Q 为 24 mm。
- P9 [12]: 正确指出 Q 型对应行程为标准型的 2 倍。

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

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 与 TNE-E 动作原理

### Question

说明液压上升型 TNE 与弹簧上升型 TNE-E 在油压关闭时的初始状态、接触工件方式以及供压后的共同抱紧结果。

### Standard Answer

TNE 在油压关闭时柱塞下降；供油后柱塞由液压上升并以柱塞弹簧力接触工件，小活塞到达上升端后抱紧机构抱紧柱塞。TNE-E 在油压关闭时柱塞由弹簧保持上升，放入工件后靠工件重量压至着座面；供油后抱紧机构同样抱紧柱塞。两者抱紧后均能承受来自上方的外力而不下降。

### Scoring Standard

- P1 [15]: 说明 TNE 油压关闭时柱塞下降。
- P2 [15]: 说明 TNE 供油后柱塞由液压上升。
- P3 [10]: 说明 TNE 以柱塞弹簧力接触工件。
- P4 [15]: 说明 TNE-E 油压关闭时柱塞由弹簧上升。
- P5 [15]: 说明工件靠自重将 TNE-E 柱塞压至着座面。
- P6 [15]: 说明供油后抱紧机构抱紧柱塞。
- P7 [15]: 说明抱紧后承受上方外力也不下降。

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

**Type: PROCEDURE**

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
- P2 [15]: 使用带单向阀的流量调整阀。
- P3 [15]: 流量控制采用进油节流。
- P4 [15]: 阀启开压力不高于 0.1 MPa。
- P5 [15]: 动作过快会使柱塞反弹。
- P6 [10]: 反弹可能导致柱塞带间隙抱紧。
- P7 [10]: 启开压力过高会导致释放时柱塞无法复位。

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

## TNE-Q-0009

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE0260/TNE0300/TNE0360/TNE0450 本体安装

### Question

TNE0260、TNE0300、TNE0360、TNE0450 的主体外螺纹尺寸和本体推荐安装力矩分别是什么？

### Standard Answer

TNE0260：M26×1.5、31.5 N·m；TNE0300：M30×1.5、50 N·m；TNE0360：M36×1.5、63 N·m；TNE0450：M45×1.5、80 N·m。

### Scoring Standard

- P1 [13]: TNE0260 螺纹为 M26×1.5。
- P2 [12]: TNE0260 安装力矩为 31.5 N·m。
- P3 [13]: TNE0300 螺纹为 M30×1.5。
- P4 [12]: TNE0300 安装力矩为 50 N·m。
- P5 [13]: TNE0360 螺纹为 M36×1.5。
- P6 [12]: TNE0360 安装力矩为 63 N·m。
- P7 [13]: TNE0450 螺纹为 M45×1.5。
- P8 [12]: TNE0450 安装力矩为 80 N·m。

### Accepted Variants

- `N･m`、`N·m` 和 `Nm` 等价。

### Forbidden Errors

- 将接触螺栓拧紧力矩当成本体安装力矩。

### Tolerance

- 螺纹和力矩按表中值精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 14
- Printed page: 1040
- Section: 外形尺寸表以及安装部位加工尺寸表
- Local scope path: TNE 液压上升标准型 > 主体螺纹 D > 本体推荐安装力矩
- Evidence type: TABLE
- Evidence: 外形尺寸表按四种主体尺寸给出 D 螺纹 M26/M30/M36/M45×1.5 及推荐安装力矩 31.5/50/63/80 N·m。

## TNE-Q-0010

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE0260/TNE0300/TNE0360/TNE0450 接触螺栓

### Question

更换 TNE 接触螺栓时，四种主体尺寸的顶端螺纹和规定拧紧力矩如何分组？

### Standard Answer

TNE0260、TNE0300 使用 M10×1.5 顶端螺纹，拧紧力矩 16 N·m；TNE0360、TNE0450 使用 M12×1.75 顶端螺纹，拧紧力矩 40 N·m。作业前必须解除供给压力，并用扳手固定柱塞顶端二面宽以防转动。

### Scoring Standard

- P1 [20]: TNE0260/0300 为 M10×1.5。
- P2 [15]: TNE0260/0300 力矩为 16 N·m。
- P3 [20]: TNE0360/0450 为 M12×1.75。
- P4 [15]: TNE0360/0450 力矩为 40 N·m。
- P5 [15]: 更换前解除供给压力。
- P6 [15]: 更换时固定柱塞顶端以防转动。

### Accepted Variants

- “二面宽”可表述为柱塞顶端扳手位。

### Forbidden Errors

- 带压更换接触螺栓。

### Tolerance

- 螺纹和力矩按规定值精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 28
- Printed page: 1118
- Section: 安装施工方面的注意事项
- Local scope path: 4) 接触螺栓的更换 > TNE 行
- Evidence type: TABLE
- Evidence: 更换说明要求解除供给压、固定柱塞，表中 TNE0260/0300 为 M10×1.5 和 16 N·m，TNE0360/0450 为 M12×1.75 和 40 N·m。

## TNE-Q-0011

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 空气传感器连接型油压支撑器
- Model / Scope: TNE-□M/TNE-□M-E 空气传感系统

### Question

TNE 空气传感器连接型的推荐供气压力、每台传感器可连接的支撑器数量，以及 PDF 推荐的 SMC 和 CKD 传感器型号是什么？

### Standard Answer

推荐供气压力为 0.05～0.15 MPa；每台空气传感器可连接 1～4 台支撑器；SMC 推荐 ISA3-G 空气传感元件，CKD 推荐 GPS3-E 间隙开关。

### Scoring Standard

- P1 [25]: 推荐供气压力 0.05～0.15 MPa。
- P2 [25]: 每台传感器连接 1～4 台支撑器。
- P3 [25]: SMC 型号 ISA3-G。
- P4 [25]: CKD 型号 GPS3-E。

### Accepted Variants

- 厂商与型号配对正确即可，不强制写出器件中文名称。

### Forbidden Errors

- 声称一台传感器可以连接超过 4 台支撑器。

### Tolerance

- 压力范围和型号精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 21
- Printed page: 1047
- Section: 空气传感器传感流程图表
- Local scope path: TNE-M/TNE-M-E > 结构图 > 推荐气压与推荐传感器表
- Evidence type: TABLE
- Evidence: 结构图标注 P1=0.05～0.15 MPa，表列 SMC ISA3-G 与 CKD GPS3-E，并注明一台传感器连接 1～4 台支撑器。

## TNE-Q-0012

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 空气传感器连接型油压支撑器
- Model / Scope: TNE-M/TNE-M-E 传感动作

### Question

空气传感器如何通过 TNE 呼吸口确认柱塞动作？分别说明释放状态与柱塞接触工件状态下传感器检测部和信号的变化。

### Standard Answer

空气传感器接在呼吸口回路，通过 P1 与 P2 的压差判断动作。TNE 释放时传感器检测部开放并排气，信号为 OFF；柱塞上升接触工件后检测部关闭，形成可检出的压差，信号为 ON。该方法检测的是支撑器内部柱塞动作，不是直接检测工件表面。

### Scoring Standard

- P1 [20]: 说明通过呼吸口回路的 P1/P2 压差检测。
- P2 [15]: 释放时检测部开放。
- P3 [15]: 释放状态会排气。
- P4 [15]: 释放状态信号为 OFF。
- P5 [15]: 接触工件后检测部关闭。
- P6 [10]: 接触工件后信号为 ON。
- P7 [10]: 说明检测对象是柱塞动作而非直接检测工件表面。

### Accepted Variants

- “压差开关量”可等同于“通过 P1/P2 压差检测”。

### Forbidden Errors

- 声称传感器直接测量工件表面间隙或表面粗糙度。

### Tolerance

- N/A

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 21
- Printed page: 1047
- Section: 空气传感器传感流程图表
- Local scope path: TNE-M/TNE-M-E > 释放 OFF 与接触 ON 结构图
- Evidence type: STATE_DIAGRAM
- Evidence: 流程图将释放状态标为检测部开放/OFF，将工件接触状态标为检测部关闭/ON，并说明用 P1/P2 压差确认柱塞动作。

## TNE-Q-0013

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 喷气清洁功能

### Question

TNE 喷气清洁功能的推荐供气压力和防尘密封圈启开压力约为多少？供气应在柱塞哪些阶段接通或切断？

### Standard Answer

喷气清洁推荐供气压力为 0.2～0.3 MPa；防尘密封圈启开压力约 0.1 MPa。柱塞上升和抱紧时供气，柱塞下降及释放时切断供气；若下降时持续供气，柱塞可能无法复位。

### Scoring Standard

- P1 [20]: 推荐供气压力 0.2～0.3 MPa。
- P2 [15]: 防尘密封圈启开压力约 0.1 MPa。
- P3 [15]: 柱塞上升时供气。
- P4 [15]: 柱塞抱紧时供气。
- P5 [15]: 柱塞下降时切断供气。
- P6 [10]: 柱塞释放时切断供气。
- P7 [10]: 说明下降时持续供气会导致无法复位。

### Accepted Variants

- “开启压力”可等同于“启开压力”。

### Forbidden Errors

- 建议释放和下降时持续供气。

### Tolerance

- 推荐压力范围精确判定；启开压力允许表述为“约 0.1 MPa”。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 23
- Printed page: 1049
- Section: 喷气清洁功能
- Local scope path: TNE > 喷气清洁结构图及注意事项
- Evidence type: STATE_DIAGRAM
- Evidence: 两幅结构图分别标注下降/释放时切断供气和上升/抱紧时 0.2～0.3 MPa，注意事项给出约 0.1 MPa 的密封圈启开压力及持续供气无法复位的后果。

## TNE-Q-0014

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: TNE 空气传感器连接型油压支撑器
- Model / Scope: TNE0300-HM 标准行程中间位置，供气压力 0.10 MPa

### Question

按 PDF 工件接触力公式，TNE0300-HM 在供气压力 0.10 MPa 时的工件接触力范围是多少？使用 U=16 mm、强弹簧力 9.0～13.5 N、π=3.141592653589793，结果按 `ROUND_HALF_UP` 保留 1 位小数。

### Standard Answer

气压附加力为 0.10×16²×π÷4=20.106... N；加上弹簧力后，工件接触力范围为 29.1～33.6 N。

### Scoring Standard

- P1 [20]: 正确代入 U=16 mm 和 0.10 MPa。
- P2 [20]: 正确计算气压附加力约 20.106 N。
- P3 [20]: 下限使用 9.0 N 弹簧力并得到 29.1 N。
- P4 [20]: 上限使用 13.5 N 弹簧力并得到 33.6 N。
- P5 [10]: 最终结果使用 N 单位。
- P6 [10]: 最终结果按 `ROUND_HALF_UP` 保留 1 位小数。

### Accepted Variants

- 中间过程可保留更多小数，但最终范围必须符合规定舍入。

### Forbidden Errors

- 忽略柱塞弹簧力，或把 0.10 MPa 再错误换算为 100000 倍后与 mm² 相乘。

### Tolerance

- 最终下限 29.1 N、上限 33.6 N，按 `ROUND_HALF_UP` 精确到 0.1 N。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 21
- Printed page: 1047
- Section: 使用空气传感器时的工件接触力计算公式
- Local scope path: TNE-M/TNE-M-E > 接触力公式 > TNE0300 的 U 与 H 弹簧力
- Evidence type: FORMULA
- Evidence: 公式为弹簧力加供气压力×U²×π/4；TNE0300 列 U=16 mm、H 弹簧力 9.0～13.5 N。

## TNE-Q-0015

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 柱塞弹簧力范围

### Question

列出标准行程 TNE0260、TNE0300、TNE0360、TNE0450 的弱弹簧 L 和强弹簧 H 设计力范围。

### Standard Answer

TNE0260：L 5.3～7.8 N，H 7.0～11.0 N；TNE0300：L 6.6～9.7 N，H 9.0～13.5 N；TNE0360：L 9.3～14.6 N，H 12.1～21.9 N；TNE0450：L 11.8～18.6 N，H 15.4～33.4 N。

### Scoring Standard

- P1 [13]: TNE0260-L 为 5.3～7.8 N。
- P2 [12]: TNE0260-H 为 7.0～11.0 N。
- P3 [13]: TNE0300-L 为 6.6～9.7 N。
- P4 [12]: TNE0300-H 为 9.0～13.5 N。
- P5 [13]: TNE0360-L 为 9.3～14.6 N。
- P6 [12]: TNE0360-H 为 12.1～21.9 N。
- P7 [13]: TNE0450-L 为 11.8～18.6 N。
- P8 [12]: TNE0450-H 为 15.4～33.4 N。

### Accepted Variants

- 可按 L/H 两组分别列出，只要型号绑定清楚。

### Forbidden Errors

- 将 Q/EQ 行程加长型弹簧力范围混入标准行程答案。

### Tolerance

- 数值和单位按表中值精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 21
- Printed page: 1047
- Section: 使用空气传感器时的工件接触力计算公式
- Local scope path: TNE-M/TNE-M-E > 柱塞弹簧力表 > L/H 行
- Evidence type: TABLE
- Evidence: 接触力公式下方的型号表按四种 U 尺寸列出 L 与 H 的柱塞弹簧设计力范围。

## TNE-Q-0016

**Type: CALCULATION**

### Target

- Binding: EXACT_MODEL
- Product: TNE 油压支撑器
- Model / Scope: TNE0450-L 喷气清洁，供气压力 0.25 MPa

### Question

按喷气清洁接触力公式，TNE0450-L 在 0.25 MPa 供气压力下的工件接触力范围是多少？使用 U=25 mm、弱弹簧力 11.8～18.6 N、π=3.141592653589793，按 `ROUND_HALF_UP` 保留 1 位小数。

### Standard Answer

气压附加力为 0.25×25²×π÷4=122.718... N；加上弱弹簧力后，工件接触力范围为 134.5～141.3 N。

### Scoring Standard

- P1 [20]: 正确代入 U=25 mm 和 0.25 MPa。
- P2 [20]: 正确计算气压附加力约 122.718 N。
- P3 [20]: 下限加 11.8 N 并得到 134.5 N。
- P4 [20]: 上限加 18.6 N 并得到 141.3 N。
- P5 [10]: 最终结果使用 N 单位。
- P6 [10]: 最终结果按 `ROUND_HALF_UP` 保留 1 位小数。

### Accepted Variants

- 中间过程可保留更多小数。

### Forbidden Errors

- 使用强弹簧 H 的范围，或遗漏弹簧力。

### Tolerance

- 最终范围 134.5～141.3 N，按 `ROUND_HALF_UP` 精确到 0.1 N。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 23
- Printed page: 1049
- Section: 使用喷气清洁功能时的工件接触力计算公式
- Local scope path: TNE > 喷气清洁 > 公式及 TNE0450 L 弹簧力行
- Evidence type: FORMULA
- Evidence: 公式为弹簧力加供气压力×U²×π/4；型号表给出 TNE0450 的 U=25 mm 和 L 弹簧力 11.8～18.6 N。

## TNE-Q-0017

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 空气传感器连接型油压支撑器
- Model / Scope: TNE-M/TNE-M-E 运行注意事项

### Question

为避免空气传感器连接型 TNE 出现间隙、内部损坏和污染侵入，运行时必须满足哪些供气与速度要求？

### Standard Answer

传感器呼吸口应保持常时供气；若切断气压后使用，冷却液或切削屑可能从检测部侵入，导致支撑器动作不良或传感器损坏。柱塞动作时间应通过带单向阀的进油节流调整到约 0.5～1 秒，并确认柱塞与工件之间无间隙；动作过快会反弹，可能在反弹位置抱紧并冲击内部零部件。

### Scoring Standard

- P1 [15]: 传感器呼吸口保持常时供气。
- P2 [15]: 说明断气会使冷却液或切削屑从检测部侵入。
- P3 [10]: 污染侵入可能导致支撑器动作不良。
- P4 [10]: 污染侵入可能导致空气传感器损坏。
- P5 [10]: 速度控制采用进油节流。
- P6 [15]: 将动作时间调至约 0.5～1 秒。
- P7 [10]: 投入使用前确认柱塞与工件无间隙。
- P8 [10]: 动作过快会使柱塞反弹。
- P9 [5]: 反弹抱紧可能冲击内部零部件。

### Accepted Variants

- “常压供气”在明确指呼吸口持续供气时可接受。

### Forbidden Errors

- 建议传感器运行时常态切断气源。

### Tolerance

- 动作时间范围按 0.5～1 秒判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 22
- Printed page: 1048
- Section: 空气传感器传感流程图表注意事项
- Local scope path: TNE-M/TNE-M-E > 注意事项 2、3
- Evidence type: TEXT
- Evidence: 注意事项要求进油节流调整为 0.5～1 秒并确认无间隙，同时要求呼吸口常时供气，列出反弹冲击及断气污染侵入后果。

## TNE-Q-0018

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 外螺纹型油压支撑器
- Model / Scope: TNE 安装承载面

### Question

安装 TNE 外螺纹型支撑器时，底面与安装孔底面应满足什么要求？哪些典型错误安装会增加变位量或导致设备损坏？

### Standard Answer

支撑器底面必须与安装孔底面水平密接，并由底面承受载荷。错误情形包括：邻接螺母拧紧后使支撑器或配管座浮起、基座底面接触部不水平而存在缝隙、需要承载的配管座未落到底面。上述情形会使底面不能承载，增加变位量并可能损坏设备。

### Scoring Standard

- P1 [25]: 底面与安装孔底面水平密接。
- P2 [20]: 载荷必须由底面承受。
- P3 [20]: 识别邻接螺母导致支撑器/配管座浮起。
- P4 [20]: 识别底面不平或有缝隙。
- P5 [8]: 错误安装会使变位量增加。
- P6 [7]: 错误安装可能导致设备损坏。

### Accepted Variants

- 三个错误示例中准确说明任意两个即可获得 P3 与 P4。

### Forbidden Errors

- 声称只要螺纹夹紧即可、不需要底面承载。

### Tolerance

- N/A

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 27
- Printed page: 1117
- Section: 油压支撑器注意事项
- Local scope path: 设计方面的注意事项 > 13) LD/TNE/TND/LDD 外螺纹型安装
- Evidence type: DRAWING
- Evidence: OK/NG 安装图要求底面水平密接承载，并展示邻接螺母抬升、底面缝隙和配管座浮起三种 NG 情形。

## TNE-Q-0019

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 呼吸口处理

### Question

TNE 呼吸口为什么必须正确设置，应如何配管？若不设置或受污染，可能产生什么后果？

### Standard Answer

TNE 与单动夹紧器一样需要呼吸。呼吸口应采用外配管方式引至不受切粉、粉尘和冷却液影响的位置并向大气开放；可按适用回路采取防侵入措施。若不设置呼吸或污染物进入内部，支撑器可能无法发挥正常功能并发生动作不良。

### Scoring Standard

- P1 [20]: 说明 TNE 需要呼吸。
- P2 [25]: 呼吸口采用外配管方式。
- P3 [20]: 引至不受切粉/粉尘和冷却液影响的位置。
- P4 [15]: 呼吸口向大气开放。
- P5 [10]: 不设置呼吸会使支撑器不能发挥正常功能。
- P6 [10]: 污染侵入会导致动作不良。

### Accepted Variants

- “切削屑”与“切粉”视为等价。

### Forbidden Errors

- 将呼吸口封死，或把呼吸口当作供油口使用。

### Tolerance

- N/A

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 25
- Printed page: 1115-1116
- Section: 油压支撑器注意事项
- Local scope path: 设计方面的注意事项 > 9) 正确设置呼吸口 > LD/TNE/TND/LDD
- Evidence type: DRAWING
- Evidence: 应用图明确要求 TNE 呼吸口外配管至不受切粉和冷却液影响的位置；文字说明无呼吸会影响正常功能。

## TNE-Q-0020

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 与对向夹紧器的能力匹配

### Question

TNE 与夹紧器对向使用时，支撑力至少应满足什么关系？若夹紧力为 8 kN，最低支撑力是多少？

### Standard Answer

支撑力应不小于夹紧力的 1.5 倍。夹紧力为 8 kN 时，最低支撑力为 12 kN。

### Scoring Standard

- P1 [40]: 给出支撑力 ≥ 夹紧力×1.5。
- P2 [30]: 正确计算 8×1.5=12。
- P3 [20]: 最终最低支撑力为 12。
- P4 [10]: 最终结果使用 kN 单位。

### Accepted Variants

- “至少 150%”可等同于“1.5 倍以上”。

### Forbidden Errors

- 使用支撑力 ≤ 夹紧力，或将 12 kN 写成 12 N。

### Tolerance

- 12 kN 精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 25
- Printed page: 1115
- Section: 油压支撑器注意事项
- Local scope path: 设计方面的注意事项 > 1) 确认规格
- Evidence type: FORMULA
- Evidence: 注意事项明确给出“支撑力 ≥ 夹紧力×1.5”的选型关系。

## TNE-Q-0021

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 油压支撑器
- Model / Scope: TNE 接触螺栓设计与使用

### Question

说明 TNE 接触螺栓在安装、O 形密封、重量和螺纹尺寸方面的四项关键要求及违反后的风险。

### Standard Answer

必须安装接触螺栓后才能使用，否则柱塞弹簧无固定部件、柱塞无法上升；接触螺栓必须安装 O 形密封圈，否则冷却液等异物会进入内部导致故障；接触螺栓重量应在柱塞弹簧力折算承载重量的 30% 以下；螺纹尺寸必须符合产品页设计尺寸，因为接触螺栓还承担固定弹簧和机械顶升功能，尺寸不符会改变弹簧力和有效行程并导致动作不良或损坏。

### Scoring Standard

- P1 [10]: 使用前必须安装接触螺栓。
- P2 [10]: 未装接触螺栓会使柱塞无法上升。
- P3 [10]: 接触螺栓必须安装 O 形密封圈。
- P4 [10]: 未装 O 形密封圈会使污染物侵入。
- P5 [15]: 重量限制为柱塞弹簧力折算承载重量的 30% 以下。
- P6 [15]: 螺纹尺寸必须符合产品页设计尺寸。
- P7 [5]: 接触螺栓承担固定柱塞弹簧的功能。
- P8 [5]: 接触螺栓承担机械顶升功能。
- P9 [5]: 尺寸不符会改变柱塞弹簧力。
- P10 [5]: 尺寸不符会改变有效行程。
- P11 [5]: 尺寸不符会导致动作不良。
- P12 [5]: 尺寸不符会导致支撑器损坏。

### Accepted Variants

- “负载率 30% 以下”在明确指接触螺栓重量时可接受。

### Forbidden Errors

- 建议不装接触螺栓或 O 形密封圈直接运行。

### Tolerance

- 30% 上限精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 25-26
- Printed page: 1115-1116
- Section: 油压支撑器注意事项
- Local scope path: 设计方面的注意事项 > 4) 接触螺栓与 11) 重量
- Evidence type: TEXT
- Evidence: 两处注意事项分别规定必须安装接触螺栓和 O 形圈，并规定重量在柱塞弹簧力的 30% 以下及螺纹尺寸不符的后果。

## TNE-Q-0022

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: TNE 油压支撑器
- Model / Scope: TNE_R01_2026KW_C1N.pdf :: 液压系列通用安装与排气要求

### Question

TNE 油压回路配管施工结束或空气进入后，应如何排气？给出供油压力限制和主要操作顺序。

### Standard Answer

先将供油压力调到 2 MPa 以下；将离支撑器最近的配管接头螺母旋松一圈；左右摇动配管使连接处松动并排出混有空气的液压油；空气排净后重新拧紧接头螺母。宜在回路最高端和最末端附近排气，板式配管可在最高端附近设置排气阀。

### Scoring Standard

- P1 [20]: 供油压力调到 2 MPa 以下。
- P2 [20]: 最近接头螺母旋松一圈。
- P3 [20]: 摇动配管并排出含空气液压油。
- P4 [20]: 排净后重新拧紧接头。
- P5 [10]: 优先在回路最高端附近排气。
- P6 [5]: 优先在回路最末端附近排气。
- P7 [5]: 板式配管可在最高端附近设置排气阀。

### Accepted Variants

- 在不改变安全顺序的情况下可合并描述中间步骤。

### Forbidden Errors

- 在高于 2 MPa 的供油压力下松开接头排气。

### Tolerance

- 供油压力必须表述为 2 MPa 以下。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 29
- Printed page: 1725
- Section: 安装施工方面的注意事项（液压系列通用）
- Local scope path: 4) 排净油压回路内的空气
- Evidence type: PROCEDURE
- Evidence: 通用安装页按 ①～⑤ 给出 2 MPa 以下、松接头、摇管排油、复紧及最高端/末端排气步骤。

## TNE-Q-0023

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: TNE 外配管式安装座
- Model / Scope: TNEZ-S 与 TNEZ-SQ 适用关系

### Question

TNEZ-S 和 TNEZ-SQ 分别适用于哪类 TNE？TNE-Q 与 TNE-EQ 选座时有哪些明确限制？

### Standard Answer

TNEZ-S 是 TNE 标准行程用外配管式安装座，不适用于 TNE-Q；TNEZ-SQ 是 TNE-Q 液压上升行程加长型用安装座，不适用于 TNE-EQ。TNE-Q 应选 TNEZ-SQ；TNE-EQ 应按 TNEZ-S 方向另行选择/确认，不能直接使用 TNEZ-SQ。

### Scoring Standard

- P1 [25]: TNEZ-S 适用于标准行程 TNE。
- P2 [25]: TNEZ-S 不适用于 TNE-Q。
- P3 [25]: TNEZ-SQ 适用于 TNE-Q。
- P4 [25]: TNEZ-SQ 不适用于 TNE-EQ。

### Accepted Variants

- 对 TNE-EQ 表述为“需根据 TNEZ-S 另行选择”可接受。

### Forbidden Errors

- 声称 TNEZ-SQ 可直接用于 TNE-EQ。

### Tolerance

- N/A

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 36-37
- Printed page: 1706, 1711
- Section: 外配管式安装座／螺母
- Local scope path: TNEZ-S/SQ > 使用型号与型号表注意事项
- Evidence type: TABLE
- Evidence: 应用页将 TNEZ-S 绑定 TNE、TNEZ-SQ 绑定 TNE-Q；尺寸表脚注明 S 不适用于 TNE-Q、SQ 不适用于 TNE-EQ。

## TNE-Q-0024

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: TNE 油压支撑器
- Model / Scope: TNE_R01_2026KW_C1N.pdf :: 液压系列通用操作、保养与质量保证

### Question

概述 TNE 拆卸前的安全条件、日常维护重点，以及 PDF 规定的保修期判定方式。

### Standard Answer

拆卸前应对被驱动物体采取防坠落和防误动作措施，切断压力源与电源，并确认油压、气压回路压力为零；设备刚停止时还应等待完全降温。维护时定期清扫柱塞周围，检查配管、安装螺栓、螺母等是否松动，检查液压油老化、异音和动作是否顺畅，长期停用后重新启用尤其要确认动作。保修期取本厂发货后 1 年半与开始使用后 1 年两者中较短者。

### Scoring Standard

- P1 [8]: 拆卸前落实防坠落措施。
- P2 [8]: 拆卸前落实防误动作措施。
- P3 [8]: 拆卸前切断压力源。
- P4 [8]: 拆卸前切断电源。
- P5 [8]: 拆卸前确认回路压力为零。
- P6 [8]: 刚停止的设备需等待完全降温。
- P7 [8]: 定期清扫柱塞周围。
- P8 [8]: 定期检查配管和紧固件是否松动。
- P9 [8]: 定期检查液压油是否老化。
- P10 [8]: 检查装置有无异音。
- P11 [8]: 检查动作是否正常顺畅。
- P12 [12]: 保修期为发货后 1.5 年或使用后 1 年中较短者。

### Accepted Variants

- “18 个月”可等同于“1 年半”。

### Forbidden Errors

- 带压拆卸，或将保修期错误表述为两个期限中较长者。

### Tolerance

- 保修期限精确判定。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 31-32
- Printed page: 1727-1728
- Section: 操作方面的注意事项；保养、检查；质量保证
- Local scope path: 液压系列通用 > 拆卸安全、定期维护与保修期
- Evidence type: TEXT
- Evidence: 操作页规定防坠落、断压断电、压力为零和冷却后拆卸；保养页列清扫与检查项目；质量保证页规定两个保修期限取较短者。

## TNE-Q-0025

**Type: CHART**

### Target

- Binding: EXACT_MODEL
- Product: TNE 油压支撑器
- Model / Scope: TNE0360 标准/E 型，供给油压 35 MPa，静载荷 15 kN

### Question

依据载荷/变位连续曲线，TNE0360 在供给油压 35 MPa、静载荷 15 kN 时的柱塞变位约为多少？说明读图条件及允许范围。

### Standard Answer

从 TNE0360 曲线在 15 kN 处视觉读取，柱塞变位约为 44 μm；接受范围为 40～48 μm。该图表示 35 MPa 下静载荷造成的柱塞变位，不包含星号所示局部凹凸及周边夹紧器引起的工件侧变位。

### Scoring Standard

- P1 [35]: 视觉读图中心值约 44 μm。
- P2 [20]: 答案落在 40～48 μm 范围内。
- P3 [15]: 明确模型为 TNE0360。
- P4 [15]: 明确条件为 35 MPa、静载荷 15 kN。
- P5 [8]: 说明图值不包含星号所示局部凹凸。
- P6 [7]: 说明图值不包含周边夹紧器引起的工件侧变位。

### Accepted Variants

- 允许回答 40～48 μm 内的单一视觉读数并说明是近似值。

### Forbidden Errors

- 直接引用支撑力离散表的 14.0 kN 作为变位答案，或声称图值包含工件侧变形。

### Tolerance

- CHART 视觉读图公差：44 μm ±4 μm，即 40～48 μm。

### Source

- PDF: TNE_R01_2026KW_C1N.pdf
- Physical page: 9
- Printed page: 1035
- Section: 能力曲线图
- Local scope path: TNE 标准/E 型 > 载荷/变位曲线图 > TNE0360 曲线
- Evidence type: CHART
- Evidence: 连续图横轴为载荷 kN、纵轴为变位 μm；TNE0360 曲线在 15 kN 处约 44 μm，图注限定 35 MPa 静载荷并排除工件侧变位。
