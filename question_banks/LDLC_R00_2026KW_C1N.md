---
schema_version: will-ai-question-bank/v1
source_pdf: LDLC_R00_2026KW_C1N.pdf
source_sha256: 12fba84b296d827658e4ae67377be48bacfa1519748a23e81217a613111b5b02
source_pages: 100
question_bank_version: V1
product_scope: LDLC
---

# LDLC_R00_2026KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LDLC_R00_2026KW_C1N.pdf`
- SHA-256: `12fba84b296d827658e4ae67377be48bacfa1519748a23e81217a613111b5b02`
- 物理页数: 100
- Product: KOSMEK LD 外螺纹型油压支撑器、LC 法兰型油压支撑器及文档内适用附件
- 主要产品印刷页: 959-1016
- 文档内附件与通用资料印刷页: 1113-1118、1257-1274、1697-1710、1725-1730、1749-1750
- 来源证据原则: PDF 页面及其结构化文字、表格、图表和图示为 Source Truth；文本提取仅用于定位，存在结构或视觉歧义时以 PDF 页面视觉证据为准。

## 2. Scope

### 2.1 产品与文档范围

本题库的主要产品范围是 LD 外螺纹型油压支撑器和 LC 法兰型油压支撑器，
覆盖动作原理、型号表示、规格、能力曲线、外形与安装尺寸、空气传感器连接型、
气压清洁功能、柱塞弹簧设计、安装和使用注意事项。

PDF 还直接收录 XLC-VENT 呼吸阀、BZL/BZX/JZG/BZS 控制阀、LZ-BZS 阀块、
安装座、配管块、螺母等附件，以及液压通用注意事项和标示对照。只有在 Target
明确绑定相应附件、型号或 DOCUMENT_COMMON 时，才可使用这些文档内资料。

目录和通用注意事项中出现的 LCW、TNE、TC、TND、LDD 等其他支撑器系列，
不代表本 PDF 收录了这些系列的完整规格。其内容只允许按本 PDF 明示的共同适用
条件使用，不得把 LD 或 LC 的型号、尺寸、能力或规格迁移到其他系列。

公司地址、销售网点和销售网络图属于非技术联系信息，不进入产品能力题目。

### 2.2 LD 型号语法

LD 的规范结构为：

`LD<主体尺寸><设计编号>-<柱塞弹簧力><动作确认>-<选配项>`

无符号字段在实际型号中省略；字段顺序不得改变。

| 字段 | 资料列出的值 | 含义与约束 |
|---|---|---|
| 主体尺寸 | `016`、`022`、`026`、`030`、`036`、`045` | 分别对应外径螺纹 M16x1.0、M22x1.5、M26x1.5、M30x1.5、M36x1.5、M45x1.5。 |
| 设计编号 | `3` | 本资料列出的产品版本信息。 |
| 柱塞弹簧力 | `L`、`H`、无符号 | `L` 为弱弹簧型，`H` 为强弹簧型；选择 `Q` 或 `EQ` 时该字段无符号。 |
| 动作确认 | `M`、无符号 | `M` 为空气传感器连接型；无符号为标准无动作确认。 |
| 选配项 | `S`、`Q`、`E`、`ES`、`EQ`、无符号 | 分别表示液压上升小型本体、液压上升行程加长、弹簧上升、弹簧上升小型本体、弹簧上升行程加长和标准液压上升。 |

主体尺寸与选配项、动作确认之间存在资料规定的可对应范围。判断完整型号是否合法时，
除校验字段值和顺序外，还必须核对同页的“外螺纹尺寸及可否对应”表，不得假定所有字段
可以任意组合。

### 2.3 LC 型号语法

LC 的规范结构为：

`LC<主体尺寸><设计编号>-<配管方式><柱塞弹簧力><动作确认>-<选配项>`

无符号字段在实际型号中省略；字段顺序不得改变。例如 `LC0553-CLM-E` 中，
`C`、`L`、`M` 连续书写，不能拆写成多个连字符字段。

| 字段 | 资料列出的值 | 含义与约束 |
|---|---|---|
| 主体尺寸 | `026`、`030`、`036`、`040`、`048`、`055`、`065`、`075`、`090` | 表示本体外径 phi 26、30、36、40、48、55、65、75、90 mm。 |
| 设计编号 | `3` | 本资料列出的产品版本信息。 |
| 配管方式 | `C`、`S` | `C` 为板式连接型，配 G 螺纹堵头并带排气功能；`S` 为 Rc 螺纹外配管型。 |
| 柱塞弹簧力 | `L`、`H`、无符号 | `L` 为弱弹簧型，`H` 为强弹簧型；选择 `Q`、`EQ` 或 `D` 时该字段无符号。 |
| 动作确认 | `M`、无符号 | `M` 为空气传感器连接型；无符号为标准无动作确认。 |
| 选配项 | `Q`、`E`、`EQ`、`D`、无符号 | 分别表示液压上升行程加长、弹簧上升、弹簧上升行程加长、无活塞中空型和标准液压上升。 |

资料要求 `S` 外配管型与 `M` 空气传感器连接型的组合另行确认，也要求 `M` 与 `Q`、
`EQ` 行程加长型的组合另行确认。因此，语法字段看似成立并不等于组合已经被本资料明确批准。

### 2.4 来源覆盖索引

下表按相邻重复物理页形成的印刷跨页汇总来源对象。当前题目覆盖列用于约束后续增量工作，
不得把“候选”理解为已经形成 Gold。

| Coverage ID | 物理页 / 印刷页 | 局部范围 | 证据类型 | 可测试对象 | 当前题目覆盖 / 范围决定 |
|---|---|---|---|---|---|
| LDLC-SI-001 | 1-2 / 959-960 | 油压支撑器总览 | TEXT + DRAWING | 支撑器用途、系列选择边界 | 候选；其他系列仅作选择边界，不迁移规格 |
| LDLC-SI-002 | 3-6 / 961-964 | LD 特点与动作说明 | TEXT + DRAWING | 接触、锁紧、释放动作及功能 | `LDLC-Q-0002`-`LDLC-Q-0004`、`LDLC-Q-0006` |
| LDLC-SI-003 | 7-8 / 965-966 | LD 型号表示与规格 | TABLE + MODEL | 型号字段、合法组合、支撑力和通用规格 | `LDLC-Q-0007`、`LDLC-Q-0009`、`LDLC-Q-0011`；其余规格候选 |
| LDLC-SI-004 | 9-12 / 967-970 | LD 能力曲线 | CHART | 油压、柱塞行程与容许负载的视觉读取 | 候选；Chart Gold 必须视觉读取 |
| LDLC-SI-005 | 13-16 / 971-974 | LD 标准型与 S 型外形尺寸 | DRAWING + TABLE | 代表型号尺寸和安装要求 | 候选；避免仅换尺寸的重复题 |
| LDLC-SI-006 | 17-18 / 975-976 | LD-Q 行程加长型 | DRAWING + TABLE | Q 型尺寸、行程和型号边界 | 候选 |
| LDLC-SI-007 | 19-22 / 977-980 | LD-E、LD-ES、LD-EQ | DRAWING + TABLE | 弹簧上升系列动作与尺寸 | 候选 |
| LDLC-SI-008 | 23-26 / 981-984 | LD-M 空气传感器连接型 | STATE_DIAGRAM + TABLE | 传感器气路、检测条件和尺寸 | 候选 |
| LDLC-SI-009 | 27-28 / 985-986 | LD 气压清洁与柱塞弹簧设计 | TEXT + DRAWING | 清洁气路、接触螺栓设计 | 候选 |
| LDLC-SI-010 | 29-30 / 987-988 | LC 特点与产品说明 | TEXT + DRAWING | 法兰型结构和功能 | `LDLC-Q-0002`、`LDLC-Q-0003`、`LDLC-Q-0010` |
| LDLC-SI-011 | 31-34 / 989-992 | LC 动作说明 | TEXT + DRAWING | 接触、锁紧、释放动作及配管差异 | `LDLC-Q-0005`、`LDLC-Q-0006`；其余动作细节候选 |
| LDLC-SI-012 | 35-36 / 993-994 | LC 型号表示与规格 | TABLE + MODEL | 字段顺序、合法值、组合限制和规格 | `LDLC-Q-0001`、`LDLC-Q-0008`；其余规格候选 |
| LDLC-SI-013 | 37-40 / 995-998 | LC 能力曲线与 LC-D | CHART + DRAWING | 曲线视觉读取、无活塞中空型边界 | 候选；Chart Gold 必须视觉读取 |
| LDLC-SI-014 | 41-42 / 999-1000 | LC 标准型外形尺寸 | DRAWING + TABLE | 代表型号尺寸和安装要求 | 候选 |
| LDLC-SI-015 | 43-46 / 1001-1004 | LC-Q 行程加长型外形尺寸 | DRAWING + TABLE | Q 型尺寸、行程和安装要求 | 候选 |
| LDLC-SI-016 | 47-50 / 1005-1008 | LC-E、LC-EQ | DRAWING + TABLE | 弹簧上升系列动作与尺寸 | 候选 |
| LDLC-SI-017 | 51-52 / 1009-1010 | LC-D 无活塞中空型 | DRAWING + TABLE | 用户自备活塞杆条件和尺寸 | 候选 |
| LDLC-SI-018 | 53-56 / 1011-1014 | LC-M 空气传感器连接型 | STATE_DIAGRAM + TABLE | 传感器气路、检测条件和尺寸 | 候选 |
| LDLC-SI-019 | 57-58 / 1015-1016 | LC 气压清洁与柱塞弹簧设计 | TEXT + DRAWING | 清洁气路、接触螺栓设计 | 候选 |
| LDLC-SI-020 | 59-60 / 1113-1114 | XLC-VENT 呼吸阀 | TEXT + TABLE | 40 um 过滤、安装扭矩和异常动作风险 | 候选；仅限 LC/TC-C 明示适用范围 |
| LDLC-SI-021 | 61-62 / 1115-1116 | 支撑器设计注意事项 | TEXT + FORMULA | 支撑力安全系数、动作时间、流量控制、接触螺栓计算 | 候选；按明示适用系列绑定 |
| LDLC-SI-022 | 63-64 / 1117-1118 | 支撑器安装注意事项 | TEXT + DRAWING | 安装基准、紧固、O 形圈和接触螺栓拆装 | 候选；按明示安装类型绑定 |
| LDLC-SI-023 | 65-66 / 1725-1726 | 液压油、排气与速度控制 | PROCEDURE + STATE_DIAGRAM | 油液条件、排气步骤和节流方式 | 候选，绑定 DOCUMENT_COMMON |
| LDLC-SI-024 | 67-68 / 1727-1728 | 操作、维护与保修 | TEXT + PROCEDURE | 安全操作和维护 | 操作维护候选；商业保修条款排除 |
| LDLC-SI-025 | 69-70 / 1257-1258 | 控制阀总览 | TABLE | BZL、BZT、BZX、JZG、BZS 功能选择 | 候选；附件独立绑定 |
| LDLC-SI-026 | 71-72 / 1259-1260 | BZL 型号与规格 | MODEL + TABLE | G 螺纹、进出油节流、压力范围 | 候选 |
| LDLC-SI-027 | 73-74 / 1261-1262 | BZL 外形与流量曲线 | DRAWING + CHART | 尺寸和流量视觉读取 | 候选；Chart Gold 必须视觉读取 |
| LDLC-SI-028 | 75-76 / 1265-1266 | BZX 排气阀 | MODEL + TABLE + CAUTION | 型号、压力、排气操作风险 | 候选 |
| LDLC-SI-029 | 77-78 / 1267-1268 | JZG 排气阀 | MODEL + TABLE + CAUTION | 型号、压力、排气操作风险 | 候选 |
| LDLC-SI-030 | 79-80 / 1269-1270 | BZS 顺序阀型号与规格 | MODEL + TABLE + CAUTION | 调压范围、压力差、安装和复用限制 | 候选 |
| LDLC-SI-031 | 81-82 / 1271-1272 | BZS 外形与动作 | DRAWING + CAUTION | P1/P2 方向、调整螺钉范围和危险 | 候选 |
| LDLC-SI-032 | 83-84 / 1273-1274 | LZ-BZS 阀块 | TABLE + DRAWING | 对应 BZS 型号、材料和随附范围 | 候选 |
| LDLC-SI-033 | 85-86 / 1697-1698 | 安装座适用范围 | TABLE | 支撑器与安装座的文档内对应关系 | 候选；不得扩展到未列型号 |
| LDLC-SI-034 | 87-90 / 1699-1702 | WHZ-MD、LZY-MD、LZ-MS/LZ-MP | TABLE + DRAWING | 安装座与阀块尺寸、质量和对应关系 | 候选 |
| LDLC-SI-035 | 91-96 / 1703-1710 | 配管块与螺母 | TABLE + DRAWING | LZ、TMZ、DZ、WNZ、TNEZ 附件对应关系 | 候选；按附件精确型号绑定 |
| LDLC-SI-036 | 97-98 / 1729-1730 | 表面粗糙度与 O 形圈标示 | TABLE + MODEL | 新旧标示换算和字段含义 | 候选，绑定 DOCUMENT_COMMON |
| LDLC-SI-037 | 99-100 / 1749-1750 | 公司地址与销售网络 | TEXT + DRAWING | 联系信息和网点地图 | 排除：非耐久技术知识 |

## 3. Question Statistics

- Total: 11
- FACT: 5
- SPEC_LOOKUP: 2
- MODEL: 2
- TABLE: 2
- CALCULATION: 0
- CHART: 0
- PROCEDURE: 0
- CAUTION: 0

## 4. Questions

## LDLC-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LC 法兰型油压支撑器
- Model / Scope: LC0553-CLM-E

### Question

请按 PDF 的型号字段顺序，解读 `LC0553-CLM-E` 的主体尺寸、设计编号、
配管方式、柱塞弹簧力、动作确认和选配项，并判断该型号是否符合本资料明确列出的字段语法。

### Standard Answer

`LC0553-CLM-E` 中，`055` 表示本体外径 phi 55 mm；`3` 是设计编号；
`C` 表示板式连接型，配有 G 螺纹堵头并带排气功能；`L` 表示弱弹簧型；
`M` 表示空气传感器连接型；`E` 表示弹簧上升型。各字段值及顺序均符合本资料的
型号表示，且规格表明确列出空气传感器连接型与 `E` 型的写法，所以该型号符合本资料
明确列出的字段语法。

### Scoring Standard

- P1 [15]: 正确说明 `055` 表示本体外径 phi 55 mm。
- P2 [10]: 正确说明 `3` 是设计编号。
- P3 [20]: 正确说明 `C` 为板式连接型，配 G 螺纹堵头并带排气功能。
- P4 [15]: 正确说明 `L` 为弱弹簧型。
- P5 [15]: 正确说明 `M` 为空气传感器连接型。
- P6 [15]: 正确说明 `E` 为弹簧上升型。
- P7 [10]: 明确判断字段值和顺序符合资料列出的型号语法。

### Accepted Variants

- `phi 55 mm` 可写为 `φ55 mm`、`Φ55 mm` 或 `直径 55 mm`。
- `板式连接型` 可写为 `板式配管型`，但必须保留 G 螺纹堵头和排气功能。
- 允许不改变技术含义的同义中文表述；型号代码、字段顺序和结论必须一致。

### Forbidden Errors

- 将 `C` 解释为外配管型，或将 `S` 解释为板式连接型。
- 将 `L` 解释为强弹簧型。
- 将 `M` 解释为气压清洁接口而不是空气传感器连接型。
- 将 `E` 解释为液压上升型或行程加长型。
- 将 `CLM` 拆成改变字段顺序的型号写法。

### Tolerance

- 型号代码、字段顺序和尺寸值必须精确匹配；无数值容差。

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 35
- Printed page: 993-994
- Section: LC 型号表示 / 规格
- Local scope path: LC > 型号表示 > LC0553-CLM-E 字段；规格 > LC0553-□□M-E
- Evidence type: TABLE + MODEL
- Evidence: 型号表示依次定义主体尺寸、设计编号、配管方式、柱塞弹簧力、动作确认和选配项；同页定义 055、3、C、L、M、E 的含义，规格表列有 `LC0553-□□M-E`。

## LDLC-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LD 外螺纹型与 LC 法兰型油压支撑器
- Model / Scope: LD / LC 共用楔形筒夹结构

### Question

LD 与 LC 油压支撑器的楔形筒夹结构如何同时实现强支撑、顺畅动作、柔性接触和可靠工件接触？

### Standard Answer

楔形筒夹利用楔形效果获得强抱紧力；扩大筒夹与柱塞之间的间隙，使柱塞动作顺畅并提高持久性；
接触工件的力仅为柱塞弹簧力，因此能够柔性接触工件；弹性垫块使筒夹始终处于受压状态，
从而避免夹紧过程中的微动，并防止柱塞与工件之间产生间隙。

### Scoring Standard

- P1 [20]: 正确说明楔形效果提供强抱紧力。
- P2 [20]: 正确说明扩大筒夹与柱塞间隙可保证动作顺畅。
- P3 [20]: 正确说明扩大间隙还有助于提高持久性。
- P4 [20]: 正确说明工件接触力仅为柱塞弹簧力，从而实现柔性接触。
- P5 [20]: 正确说明弹性垫块使筒夹保持受压，避免微动和接触间隙。

### Accepted Variants

- `抱紧力` 可表述为 `夹持柱塞的力`，但不得误写成直接夹紧工件。
- `持久性` 可表述为 `耐久性`。

### Forbidden Errors

- 声称柱塞依靠额定支撑力冲击工件完成接触。
- 声称扩大筒夹与柱塞间隙会降低动作顺畅性。
- 将弹性垫块描述为解除柱塞锁定的机构。

### Tolerance

- N/A

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 3, 29
- Printed page: 961-962, 987-988
- Section: LD / LC 剖面结构
- Local scope path: LD 与 LC > 剖面结构 > 强劲支撑与顺畅动作 / 可靠工件接触
- Evidence type: TEXT + DRAWING
- Evidence: 两个产品页均说明楔形筒夹的楔形效果产生强抱紧力，扩大筒夹与柱塞间隙保证顺畅性和持久性，接触力仅为柱塞弹簧力，弹性垫块使筒夹保持受压以避免微动和间隙。

## LDLC-Q-0003

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LD 外螺纹型与 LC 法兰型油压支撑器
- Model / Scope: LD / LC 内置顺序动作

### Question

LD 与 LC 油压支撑器在一个油压回路中依次执行哪三个动作，什么内置元件保证该顺序？

### Standard Answer

动作顺序为：柱塞上升、柱塞接触工件、锁定柱塞。该顺序由内置的高性能顺序控制用弹簧保证。

### Scoring Standard

- P1 [20]: 正确给出第一步为柱塞上升。
- P2 [20]: 正确给出第二步为柱塞接触工件。
- P3 [20]: 正确给出第三步为锁定柱塞。
- P4 [20]: 正确说明三个动作可在一个油压回路中依次完成。
- P5 [20]: 正确指出保证顺序的是内置顺序控制用弹簧。

### Accepted Variants

- `锁定柱塞` 可写为 `抱紧柱塞`。
- 必须保留三个动作的先后顺序。

### Forbidden Errors

- 将锁定放在接触工件之前。
- 声称该顺序必须由三个独立油压回路完成。
- 将顺序控制用弹簧误写为柱塞弹簧。

### Tolerance

- N/A

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 3, 29
- Printed page: 961-962, 987-988
- Section: LD / LC 剖面结构
- Local scope path: LD 与 LC > 可靠的顺序动作
- Evidence type: TEXT
- Evidence: 两个产品页均明确说明内置高性能顺序控制用弹簧，可在一个油压回路中依次执行“柱塞上升→接触工件→锁定”。

## LDLC-Q-0004

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LD 外螺纹型油压支撑器
- Model / Scope: LD / LD-Q 与 LD-E / LD-EQ 动作差异

### Question

比较 LD 液压上升型与弹簧上升型在油压 OFF、放置工件和油压 ON 时的柱塞状态。

### Standard Answer

液压上升型 LD/LD-Q 在油压 OFF 时柱塞处于下降状态；油压 ON 后柱塞上升，接触工件并在任意位置停止，
随后在供给油压作用下被抱紧。弹簧上升型 LD-E/LD-EQ 在油压 OFF 时柱塞处于上浮状态；放置工件后，
柱塞因工件重量下降并在力平衡位置停止；油压 ON 后柱塞同样被抱紧，不能被从上方压下。

### Scoring Standard

- P1 [15]: 正确说明液压上升型在油压 OFF 时柱塞下降。
- P2 [20]: 正确说明液压上升型在油压 ON 后上升、接触工件并停在任意位置。
- P3 [15]: 正确说明弹簧上升型在油压 OFF 时柱塞上浮。
- P4 [20]: 正确说明放置工件后弹簧上升型柱塞因工件重量下降并平衡停止。
- P5 [15]: 正确说明两类产品均在油压 ON 后抱紧柱塞。
- P6 [15]: 正确说明抱紧后柱塞不能被从上方压下。

### Accepted Variants

- `上浮` 可写为 `由弹簧保持升起`。
- `平衡停止` 可写为 `在工件重量与弹簧力平衡的位置停止`。

### Forbidden Errors

- 声称液压上升型在油压 OFF 时柱塞上浮。
- 声称弹簧上升型必须先供油才能接触工件。
- 声称油压 ON 后柱塞仍可自由下降。

### Tolerance

- N/A

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 5
- Printed page: 963-964
- Section: LD 动作原理
- Local scope path: LD > 动作原理 > 液压上升型 / 弹簧上升型
- Evidence type: TEXT + STATE_DIAGRAM
- Evidence: 动作说明分别给出 LD/LD-Q 在 OFF 时下降、ON 时上升接触并抱紧，以及 LD-E/LD-EQ 在 OFF 时上浮、工件使其下降平衡、ON 时抱紧的状态变化。

## LDLC-Q-0005

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LC 法兰型油压支撑器
- Model / Scope: LC-D 无活塞杆中空型

### Question

LC-D 无活塞杆中空型由谁提供活塞杆，油压 OFF 时如何使其接触工件，油压 ON 后发生什么？

### Standard Answer

LC-D 的活塞杆由用户自备。油压 OFF 时支撑器不抱紧活塞杆，应由另行设置的推拉式夹紧器等机构驱动活塞杆，
使其接触工件；油压 ON 后，支撑器抱紧活塞杆，完成锁定，活塞杆不能被从上方压下。

### Scoring Standard

- P1 [20]: 正确说明活塞杆由用户自备。
- P2 [20]: 正确说明油压 OFF 时支撑器不抱紧活塞杆。
- P3 [20]: 正确说明需由另设的推拉式夹紧器等机构驱动活塞杆。
- P4 [20]: 正确说明外部机构使活塞杆接触工件。
- P5 [20]: 正确说明油压 ON 后支撑器抱紧并锁定活塞杆。

### Accepted Variants

- `推拉式夹紧器` 可表述为资料允许的同类外部作动机构，但不得声称 LC-D 自带该机构。
- `抱紧` 可写为 `锁定`。

### Forbidden Errors

- 声称 LC-D 随产品提供活塞杆。
- 声称 LC-D 由内置柱塞弹簧自动使活塞杆接触工件。
- 声称油压 OFF 时已经抱紧活塞杆。

### Tolerance

- N/A

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 31
- Printed page: 989-990
- Section: LC 动作原理
- Local scope path: LC > 动作原理 > 无活塞杆中空型 LC-D
- Evidence type: TEXT + STATE_DIAGRAM
- Evidence: LC-D 状态图注明活塞杆由用户自备；OFF 时未抱紧，另设推拉式夹紧器等使活塞杆接触工件；ON 时完成抱紧。

## LDLC-Q-0006

**Type: FACT**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LD / LC 空气传感器连接型油压支撑器
- Model / Scope: LD-M / LD-M-E 与 LC-M / LC-M-E / LC-M-Q

### Question

LD 与 LC 的空气传感器连接型应把空气传感器接到哪个接口，检测什么量，用于确认什么状态？

### Standard Answer

应把空气传感器连接到支撑器的呼吸口，通过检测压差来确认支撑器柱塞的动作。

### Scoring Standard

- P1 [35]: 正确指出空气传感器连接到呼吸口。
- P2 [35]: 正确指出检测量为压差。
- P3 [30]: 正确说明用途是确认支撑器柱塞的动作。

### Accepted Variants

- `压差` 可写为 `压力差`。
- `确认柱塞动作` 可表述为 `检测柱塞是否动作`。

### Forbidden Errors

- 声称空气传感器连接到供油口。
- 声称检测的是液压油流量。
- 将该功能描述为测量支撑力。

### Tolerance

- N/A

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 5, 31
- Printed page: 963-964, 989-990
- Section: LD / LC 动作原理
- Local scope path: LD 与 LC > 空气传感器连接型 > 呼吸口与压差检测
- Evidence type: TEXT
- Evidence: 两处动作原理均说明将空气传感器连接在呼吸口上，检测压差，以确认支撑器柱塞的动作。

## LDLC-Q-0007

**Type: SPEC_LOOKUP**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LD 外螺纹型油压支撑器
- Model / Scope: LD0303 标准液压上升型

### Question

给出标准液压上升型 `LD0303` 在油压 7 MPa 时的支撑力、支撑力计算公式、柱塞行程和有效行程。

### Standard Answer

`LD0303` 在油压 7 MPa 时的支撑力为 4.0 kN；支撑力计算公式为
`0.70 x P - 0.91` kN，其中 `P` 为供给油压，单位 MPa；柱塞行程为 8 mm，
有效行程为 7.5 mm。

### Scoring Standard

- P1 [25]: 正确给出 7 MPa 时支撑力为 4.0 kN。
- P2 [25]: 正确给出计算公式 `0.70 x P - 0.91` kN。
- P3 [10]: 正确说明 `P` 是供给油压且单位为 MPa。
- P4 [20]: 正确给出柱塞行程 8 mm。
- P5 [20]: 正确给出有效行程 7.5 mm。

### Accepted Variants

- 公式乘号可写为 `x`、`×` 或省略为 `0.70P - 0.91`。
- `4.0 kN` 可写为 `4 kN`。

### Forbidden Errors

- 使用其他主体尺寸型号的支撑力或公式。
- 将 8 mm 写成有效行程，或将 7.5 mm 写成柱塞总行程。
- 省略公式结果单位 kN 或把 `P` 的单位写成 kN。

### Tolerance

- 表格值、单位和公式系数必须精确匹配；无数值容差。

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 7
- Printed page: 965-966
- Section: LD 规格
- Local scope path: LD > 规格 > 标准液压上升型 > LD0303 列
- Evidence type: TABLE
- Evidence: 标准型规格表的 LD0303 列依次给出 7 MPa 支撑力 4.0 kN、公式 0.70xP-0.91 kN、柱塞行程 8 mm、有效行程 7.5 mm；注释定义 P 为供给油压 MPa。

## LDLC-Q-0008

**Type: SPEC_LOOKUP**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LC 法兰型油压支撑器
- Model / Scope: LC0403 标准液压上升型

### Question

给出标准液压上升型 `LC0403` 在油压 7 MPa 时的支撑力、支撑力计算公式、柱塞行程和有效行程。

### Standard Answer

`LC0403` 在油压 7 MPa 时的支撑力为 5.5 kN；支撑力计算公式为
`0.96 x P - 1.25` kN，其中 `P` 为供给油压，单位 MPa；柱塞行程为 8 mm，
有效行程为 7.5 mm。

### Scoring Standard

- P1 [25]: 正确给出 7 MPa 时支撑力为 5.5 kN。
- P2 [25]: 正确给出计算公式 `0.96 x P - 1.25` kN。
- P3 [10]: 正确说明 `P` 是供给油压且单位为 MPa。
- P4 [20]: 正确给出柱塞行程 8 mm。
- P5 [20]: 正确给出有效行程 7.5 mm。

### Accepted Variants

- 公式乘号可写为 `x`、`×` 或省略为 `0.96P - 1.25`。

### Forbidden Errors

- 使用其他主体尺寸型号的支撑力或公式。
- 将 8 mm 写成有效行程，或将 7.5 mm 写成柱塞总行程。
- 省略公式结果单位 kN 或把 `P` 的单位写成 kN。

### Tolerance

- 表格值、单位和公式系数必须精确匹配；无数值容差。

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 35
- Printed page: 993-994
- Section: LC 规格
- Local scope path: LC > 规格 > 标准液压上升型 > LC0403 列
- Evidence type: TABLE
- Evidence: 标准型规格表的 LC0403 列依次给出 7 MPa 支撑力 5.5 kN、公式 0.96xP-1.25 kN、柱塞行程 8 mm、有效行程 7.5 mm；注释定义 P 为供给油压 MPa。

## LDLC-Q-0009

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LD 外螺纹型油压支撑器
- Model / Scope: LD0163-Q

### Question

`LD0163-Q` 的各字段本身分别表示什么？该完整组合是否被本资料的型号对应表列为可选？

### Standard Answer

`LD` 表示外螺纹型油压支撑器；`016` 表示 M16x1.0 外径螺纹；`3` 是设计编号；
`Q` 表示液压上升行程加长型。虽然 `016` 和 `Q` 都是资料中出现的字段值，但型号对应表只列出
`LD0223-Q`、`LD0263-Q`、`LD0303-Q`、`LD0363-Q`、`LD0453-Q`，没有列出 `LD0163-Q`，
所以该完整组合不能判定为资料明确支持的可选型号。

### Scoring Standard

- P1 [15]: 正确识别 `LD` 为外螺纹型油压支撑器。
- P2 [20]: 正确说明 `016` 对应 M16x1.0 外径螺纹。
- P3 [15]: 正确说明 `3` 是设计编号。
- P4 [20]: 正确说明 `Q` 是液压上升行程加长型。
- P5 [20]: 正确指出 Q 型对应表从 LD0223 开始且不含 LD0163。
- P6 [10]: 明确得出不能判定 `LD0163-Q` 为资料支持组合的结论。

### Accepted Variants

- `M16x1.0` 中的乘号可写为 `x` 或 `×`。
- 结论可写为 `资料未列为可选` 或 `按本 PDF 不合法`，但不得宣称现实中绝对不存在定制品。

### Forbidden Errors

- 因为 `016` 和 `Q` 分别出现过，就判定它们可以任意组合。
- 声称 Q 型对应表包含 `LD0163-Q`。
- 将 `Q` 解释为弹簧上升型。

### Tolerance

- 型号代码和螺纹规格必须精确匹配；无数值容差。

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 7
- Printed page: 965-966
- Section: LD 型号表示 / 规格
- Local scope path: LD > 型号表示 > 主体尺寸与选配项对应表 > Q 型
- Evidence type: TABLE + MODEL
- Evidence: 型号字段定义 016 为 M16x1.0、设计编号为 3、Q 为液压上升行程加长型；Q 型型号行列出 LD0223-Q 至 LD0453-Q，不含 LD0163-Q。

## LDLC-Q-0010

**Type: TABLE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LC 法兰型油压支撑器
- Model / Scope: LC 配管方式 C 与直装速度控制阀

### Question

LC 选择配管方式 `C` 时，其配管结构是什么？需要直装速度控制阀时应选择什么控制方式和 KOSMEK 型号系列，阀是否随 LC 提供？

### Standard Answer

`C` 为板式连接型，配有 G 螺纹堵头并带排气功能。LC 使用速度控制阀时必须选择进油节流型；
使用 KOSMEK 产品时选择 `BZL□-A`。速度控制阀由用户另行购买，不随 LC 提供。

### Scoring Standard

- P1 [20]: 正确说明 `C` 为板式连接型。
- P2 [20]: 正确说明配有 G 螺纹堵头并带排气功能。
- P3 [25]: 正确说明 LC 必须选择进油节流型速度控制阀。
- P4 [20]: 正确给出 KOSMEK 对应系列为 `BZL□-A`。
- P5 [15]: 正确说明速度控制阀由用户另行购买。

### Accepted Variants

- `BZL□-A` 可写为 `BZL-A 系列`，但必须保留进油节流含义。
- `板式连接` 可写为 `板式配管`。

### Forbidden Errors

- 选择出油节流型 `BZL□-B`。
- 声称速度控制阀随 LC 标准附带。
- 将 `C` 解释为 Rc 螺纹外配管型。

### Tolerance

- 型号系列和节流方向必须精确匹配；无数值容差。

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 29, 35
- Printed page: 987-988, 993-994
- Section: LC 剖面结构 / 型号表示
- Local scope path: LC > 可直接安装的速度控制阀；型号表示 > 配管方式 C
- Evidence type: TEXT + TABLE
- Evidence: 产品说明指出 C 型板式配管可直装带排气功能的速度控制阀；型号页定义 C 为板式连接、配 G 螺纹堵头并带排气功能，并要求 LC 选进油节流型 `BZL□-A`，阀由用户另购。

## LDLC-Q-0011

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LD 外螺纹型油压支撑器
- Model / Scope: LD 主体尺寸代码与外径螺纹映射

### Question

分别给出 LD 主体尺寸代码 `016`、`022`、`026`、`030`、`036`、`045` 对应的外径螺纹规格。

### Standard Answer

`016` 对应 M16x1.0；`022` 对应 M22x1.5；`026` 对应 M26x1.5；
`030` 对应 M30x1.5；`036` 对应 M36x1.5；`045` 对应 M45x1.5。

### Scoring Standard

- P1 [17]: 正确给出 `016` 对应 M16x1.0。
- P2 [17]: 正确给出 `022` 对应 M22x1.5。
- P3 [17]: 正确给出 `026` 对应 M26x1.5。
- P4 [17]: 正确给出 `030` 对应 M30x1.5。
- P5 [16]: 正确给出 `036` 对应 M36x1.5。
- P6 [16]: 正确给出 `045` 对应 M45x1.5。

### Accepted Variants

- 螺纹规格中的乘号可写为 `x` 或 `×`。
- 允许按任意顺序列出，但每个尺寸代码必须与正确螺纹一一对应。

### Forbidden Errors

- 混用 LC 的本体外径含义。
- 将任一螺距写成资料未列出的值。
- 只列出螺纹而未绑定对应主体尺寸代码。

### Tolerance

- 尺寸代码、螺纹公称直径和螺距必须精确匹配；无数值容差。

### Source

- PDF: LDLC_R00_2026KW_C1N.pdf
- Physical page: 7
- Printed page: 965-966
- Section: LD 型号表示
- Local scope path: LD > 型号表示 > 主体尺寸
- Evidence type: TABLE
- Evidence: 主体尺寸表逐项将 016、022、026、030、036、045 对应到 M16x1.0、M22x1.5、M26x1.5、M30x1.5、M36x1.5、M45x1.5。
