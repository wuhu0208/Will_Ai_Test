---
schema_version: will-ai-question-bank/v1
source_pdf: LSA_LSE_R00_2023KW_C1N.pdf
source_sha256: fc60d3fccd1cd784233e95c31b708a2ac877e03874e892b9f9cfc617582f865c
source_pages: 34
question_bank_version: V1
product_scope: LSA/LSE
---

# LSA_LSE_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LSA_LSE_R00_2023KW_C1N.pdf`
- SHA-256: `fc60d3fccd1cd784233e95c31b708a2ac877e03874e892b9f9cfc617582f865c`
- Physical pages: 34
- Product: KOSMEK LSA/LSE 油压复动式侧向夹紧器
- Product printed pages: 947-958
- Included common-reference printed pages: 1725-1730
- Included control-valve printed pages: 1257-1262、1265-1272
- Included sales-reference physical pages: 33-34（无印刷页码）
- Source-evidence policy: PDF 页面图像是视觉事实的最终依据；抽取文本仅用于导航，不能作为来源真值。

## 2. Scope

### 2.1 Product and document scope

本题库覆盖 LSA 标准侧向夹紧器系列和 LSE 高能力侧向夹紧器系列，包括产品定位、
型号语法、规格、夹紧力与保持力关系、尺寸、安装、液压回路、速度调整、保养、
安全事项，以及本 PDF 收录的适用直装式控制阀。

商业质保和销售网络资料保留在来源清单中，但不纳入核心能力题。液压
安装、速度控制、操作、保养、符号和附属控制阀等通用事实必须采用限定到具体
页面的本地范围和正确的绑定类型，避免与 LSA/LSE 产品本地要求混淆。

### 2.2 Model Grammar

LSA 和 LSE 的印刷字段顺序为：

`<系列><主体尺寸><设计编号>-<配管方式><压板方向>`

| 字段 | 合法值 | 含义与约束 |
|---|---|---|
| 系列 | `LSA`、`LSE` | `LSA` 是标准侧向夹紧器系列；`LSE` 是带机械自锁机构的高能力侧向夹紧器系列。 |
| 主体尺寸 | `036` | 夹紧器本体夹紧部分外径等级为 φ36 mm。 |
| 设计编号 | `0` | 本 PDF 列出的产品版本/设计编号。 |
| 配管方式 | `C` | 板式配管型，附带 G 螺纹堵头，可安装另购的直装式速度控制阀。 |
| 压板方向 | `L`、`C`、`R` | 面向供油口观察时，压板方向分别为左、中央或右。 |

两个系列共用主体尺寸、设计编号、配管方式和方向字段语法，但使用限制和速度控制
规则并非全部相同。尤其是 LSE 必须使用进油节流型 BZL-A 速度控制阀。

合法示例：

- `LSA0360-CL`
- `LSA0360-CC`
- `LSA0360-CR`
- `LSE0360-CL`
- `LSE0360-CC`
- `LSE0360-CR`

非法示例及原因：

- `LSA0400-CR`：本 PDF 未列出 LSA 主体尺寸代码 `040`。
- `LSE0361-CR`：本 PDF 未列出设计编号 `1`。
- `LSA0360-SR`：本 PDF 未列出配管方式 `S`。
- `LSE0360-CB`：本 PDF 未列出压板方向 `B`。
- `LSA0360-RC`：配管方式与压板方向字段顺序错误。
- `LSE0360-CR-A`：BZL 控制方式不是 LSE 产品型号的后缀字段。

### 2.3 Source-first inventory and initial dispositions

`HIGH` 和 `MEDIUM` 项在对应问题及构建审计完成前均保持未完成状态。处置列仅标明
计划工作，不提前声明已覆盖。每一对物理页是同一印刷跨页的重复呈现；Inventory
只记录一次，不将重复页面视为新证据。

| Inventory ID | 物理页 / 印刷页 | 本地范围 | 证据类型 | 优先级 | 可测试对象 | 初始处置 |
|---|---|---|---|---|---|---|
| LSA-LSE-SI-001 | 1-2 / 947-948 | LSA 概述与特点 | TEXT + DRAWING | HIGH | 侧推定位、上方零干涉、安装尺寸通用性、2.8 kN 标称夹紧力及直装式速度控制阀 | WP2 `FACT`；保留图示本地限定 |
| LSA-LSE-SI-002 | 3-4 / 949-950 | LSA 型号、规格与夹紧力关系 | MODEL + TABLE + FORMULA + CHART | HIGH | 四字段语法、φ36 本体、行程/容量/压力/温度/流体/重量、`F = 0.394 x P`、压力-夹紧力表及不可使用范围后果 | 型号语法及 `LSA-LSE-Q-0001`；WP2 `TABLE`；WP3 `CALCULATION` / `CHART` |
| LSA-LSE-SI-003 | 5-6 / 951-952 | LSA 尺寸、设计、安装与速度控制 | DRAWING + TABLE + TEXT | HIGH | 油口、安装几何、禁止同时供压、焊接/干燥环境控制、M4 力矩、销轴操作和速度调整 | WP2 `TABLE`；WP3 `PROCEDURE` / `CAUTION`；重复尺寸保留为直接查询证据 |
| LSA-LSE-SI-004 | 7-8 / 953-954 | LSE 概述与高能力机构 | TEXT + DRAWING | HIGH | 侧推定位、相对 LSA 的 1.5 倍夹紧力、机械自锁、保持力作用及 BZL-A 要求 | WP2 `FACT`；WP3 `CAUTION`；机构图留待选择性视觉核验 |
| LSA-LSE-SI-005 | 9-10 / 955-956 | LSE 型号、规格及夹紧力/保持力关系 | MODEL + TABLE + FORMULA + CHART | HIGH | 共用四字段语法、行程/容量/压力限制、`F = 0.601 x P`、`Fk = 0.953 x P`、3.62 kN 保持力上限及反作用力注意事项 | 型号语法及 `LSA-LSE-Q-0001`；WP2 `TABLE`；WP3 `CALCULATION` / `CHART` / `CAUTION` |
| LSA-LSE-SI-006 | 11-12 / 957-958 | LSE 尺寸、设计、安装与速度控制 | DRAWING + TABLE + TEXT | HIGH | 方向变型、安装几何、禁止同时供压、M4 力矩、进油节流调整、排气、多夹紧器控制及带负荷释放 | WP2 `TABLE`；WP3 `PROCEDURE` / `CAUTION`；保留 LSE 本地回路例外 |
| LSA-LSE-SI-007 | 13-14 / 1725-1726 | 液压安装与速度控制回路通用事项 | TEXT + TABLE + STATE_DIAGRAM | HIGH | ISO-VG32 油品表、清洁、密封胶带、排气、紧固检查、单/复动回路规则及 LSE 例外 | WP3 `PROCEDURE` / `CAUTION`；限定页面的 `DOCUMENT_COMMON` |
| LSA-LSE-SI-008 | 15-16 / 1727-1728 | 操作、保养与质保通用事项 | TEXT + DRAWING | HIGH | 人员资格、隔离/零压/冷却、重启检查、禁止接触/改造、清洁、检查、存放及大修 | WP3 `CAUTION`；质保内容为 LOW 并排除；限定页面范围 |
| LSA-LSE-SI-009 | 17-18 / 1729-1730 | 通用符号参考 | TABLE | MEDIUM | 表面粗糙度及 O 形圈材质/硬度的新旧符号对应关系 | WP2 `TABLE`；限定页面的 `DOCUMENT_COMMON` |
| LSA-LSE-SI-010 | 19-20 / 1257-1258 | 直装式控制阀系列概述 | TEXT + DRAWING + TABLE | MEDIUM | BZL/BZT/BZX/JZG/BZS 的用途、直装关系和压力等级 | WP2 `FACT` / `TABLE`；附属产品范围 |
| LSA-LSE-SI-011 | 21-22 / 1259-1260 | BZL 低压速度控制阀型号与兼容性 | MODEL + TABLE + TEXT | HIGH | 螺纹/设计/控制方式语法、A/B 回路含义、压力/温度/力矩、兼容性、禁止重复使用及 LSA/LSE 对应关系 | WP2 `MODEL` / `TABLE`；WP3 `CAUTION` |
| LSA-LSE-SI-012 | 23-24 / 1261-1262 | BZL 流量曲线、尺寸与注意事项 | CHART + DRAWING + TEXT | MEDIUM | 调整前后流量与圈数/压力损失关系、油口方向、低压排气和加工尺寸 | WP3 `CHART` / `CAUTION`；必须进行真实视觉读图 |
| LSA-LSE-SI-013 | 25-26 / 1265-1266 | BZX 排气阀 | MODEL + TABLE + DRAWING + TEXT | MEDIUM | 螺纹语法、35 MPa 限制、力矩、兼容性、堵头旋松限制及低压排气 | WP2 `MODEL` / `TABLE`；WP3 `CAUTION`；附属范围 |
| LSA-LSE-SI-014 | 27-28 / 1267-1268 | 带排气功能的 JZG G 螺纹堵头 | MODEL + TABLE + DRAWING + TEXT | MEDIUM | 螺纹语法、35 MPa 限制、力矩/材质规则、兼容性及低压排气 | WP2 `MODEL` / `TABLE`；WP3 `CAUTION`；附属范围 |
| LSA-LSE-SI-015 | 29-30 / 1269-1270 | BZS 直装式顺序阀型号与规格 | MODEL + TABLE + DRAWING + TEXT | HIGH | 螺纹/设计语法、压力范围、通路、力矩、兼容性、污染、压差、重复使用及流量控制 | WP2 `MODEL` / `TABLE`；WP3 `CAUTION` |
| LSA-LSE-SI-016 | 31-32 / 1271-1272 | BZS 尺寸、设定与动作顺序 | DRAWING + TABLE + CHART + PROCEDURE | HIGH | 调整范围、油口方向、压力设定、防转套力矩、动作顺序、多阀压差、空气及调试 | WP3 `PROCEDURE` / `CHART` / `CAUTION`；仅在布局关系不明确时选择性视觉核验 |
| LSA-LSE-SI-017 | 33-34 / 无印刷页码 | 销售地址与网络 | TEXT + DRAWING | NON-TEST | 联系方式和销售区域 | 排除；不属于耐久的 LSA/LSE 技术知识 |
| LSA-LSE-SI-018 | 1-32 / 全部收录印刷页 | 重复导航及成对跨页呈现 | TEXT | NON-TEST | 侧栏导航、章节标签、页面重复和交叉引用界面 | 作为导航/呈现重复排除；来源清单以本地技术内容为准 |

## 3. Question Statistics

- Total: 8
- FACT: 2
- MODEL: 2
- SPEC_LOOKUP: 2
- TABLE: 2

## 4. Questions

## LSA-LSE-Q-0001

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: LSA/LSE 油压复动式侧向夹紧器
- Model / Scope: LSA0360-C□ 标准系列和 LSE0360-C□ 高能力系列

### Question

按 PDF 的型号字段顺序解读 `LSA0360-CL` 与 `LSE0360-CR`。说明两个前缀的
产品系列边界、`036`、末位 `0`、`C` 以及 `L`/`R` 的含义，并判断两个型号
是否合法。

### Standard Answer

`LSA` 表示标准侧向夹紧器系列；`LSE` 表示带机械自锁机构的高能力侧向夹紧器
系列。两个型号中的 `036` 都表示夹紧器本体夹紧部分外径为 φ36 mm，末位
`0` 是本 PDF 列出的设计编号，`C` 表示板式配管型并配有 G 螺纹堵头。面向
供油口观察时，`L` 表示压板向左，`R` 表示压板向右。因此 `LSA0360-CL` 和
`LSE0360-CR` 的字段顺序与取值均合法。

### Scoring Standard

- P1 [10]: 正确说明 `LSA` 是标准侧向夹紧器系列。
- P2 [15]: 正确说明 `LSE` 是带机械自锁机构的高能力侧向夹紧器系列。
- P3 [15]: 正确说明 `036` 表示夹紧器本体夹紧部分外径 φ36 mm。
- P4 [10]: 正确说明末位 `0` 是设计编号。
- P5 [15]: 正确说明 `C` 为配有 G 螺纹堵头的板式配管型。
- P6 [10]: 正确限定压板方向的观察视角为面向供油口。
- P7 [10]: 正确说明 `L` 为左、`R` 为右。
- P8 [15]: 正确判断两个示例型号的字段顺序和取值均合法。

### Accepted Variants

- `φ36 mm` 可写为 `Φ36 mm` 或 `直径 36 mm`。
- `板式配管型` 可写为 `板式连接型`。
- `机械自锁机构` 可写为 `机械式自锁机构`。

### Forbidden Errors

- 交换 LSA 与 LSE 的标准/高能力系列边界。
- 将 `036` 解释为行程、压力或夹紧力。
- 将末位 `0` 解释为方向或控制方式。
- 将 `C` 解释为压板中央方向。
- 不限定观察视角，或交换 `L` 与 `R`。
- 声称任一示例型号的字段顺序或取值非法。

### Tolerance

- 必须准确给出系列边界、φ36 mm 主体尺寸等级、设计编号 `0`、配管方式 `C` 和方向含义。

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 3-4, 7-10
- Printed page: 949-950, 953-956
- Section: LSA/LSE 特点 / 型号表示 / 规格
- Local scope path: LSA 标准侧向夹紧器与 LSE 高能力自锁侧向夹紧器；LSA0360-C□ / LSE0360-C□ 型号字段
- Evidence type: TEXT + MODEL + TABLE + DRAWING
- Evidence: LSA/LSE 特点页区分标准和高能力自锁系列；型号页给出“系列-036-0-C-方向”的顺序，将 036 定义为 φ36 mm 本体尺寸、0 定义为设计编号、C 定义为配有 G 螺纹堵头的板式配管，并以面向供油口的视角定义 L/C/R。

## LSA-LSE-Q-0002

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: LSA/LSE 油压复动式侧向夹紧器
- Model / Scope: LSA 标准系列与 LSE 高能力系列的产品定位

### Question

比较 LSA 与 LSE 侧向夹紧器的产品定位。说明两个系列共同适合的夹紧方式，以及
LSE 相对同尺寸 LSA 的夹紧力、锁紧机构和保持能力差异。

### Standard Answer

LSA 与 LSE 都从工件侧面施力，适合侧推定位或夹紧，并可消除夹紧器在工件上方
造成的干涉。LSE 是高能力系列，同尺寸下夹紧力约为 LSA 的 1.5 倍；LSE 内置
机械自锁机构，在供油压力下降时仍能产生较高保持力。LSA 是不带该机械自锁机构
的标准系列。

### Scoring Standard

- P1 [20]: 说明两个系列都从工件侧面施力，适合侧推定位或夹紧。
- P2 [15]: 说明侧向布置可消除夹紧器在工件上方造成的干涉。
- P3 [20]: 正确区分 LSA 为标准系列、LSE 为高能力系列。
- P4 [20]: 说明同尺寸 LSE 的夹紧力约为 LSA 的 1.5 倍。
- P5 [15]: 说明 LSE 内置机械自锁机构。
- P6 [10]: 说明该机构能在供油压力下降时提供较高保持力。

### Accepted Variants

- `侧推定位` 可写为 `横向定位` 或 `侧面定位`。
- `约 1.5 倍` 可写为 `1.5 倍左右`。

### Forbidden Errors

- 声称 LSA 是高能力自锁系列而 LSE 是标准系列。
- 声称 LSA 内置机械自锁机构。
- 将 LSE 相对 LSA 的夹紧力关系写成更小或相同。
- 声称两个系列从工件上方施力。

### Tolerance

- 倍率必须表达为同尺寸 LSE 约为 LSA 的 1.5 倍，不接受反向比较。

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 1-2, 7-8
- Printed page: 947-948, 953-954
- Section: LSA/LSE 特点
- Local scope path: LSA 标准侧向夹紧器与 LSE 高能力机械自锁侧向夹紧器的产品定位
- Evidence type: TEXT + DRAWING
- Evidence: LSA 特点页说明侧推定位和上方零干涉；LSE 特点页说明同尺寸夹紧力约为 LSA 的 1.5 倍，并说明机械自锁机构和高保持力。

## LSA-LSE-Q-0003

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: LSA/LSE 油压复动式侧向夹紧器
- Model / Scope: LSA0360-C□ 与 LSE0360-C□ 规格表

### Question

根据规格表比较 `LSA0360-C□` 与 `LSE0360-C□`。分别给出两者的夹紧侧/释放侧
油量、最高使用压力、耐压和重量，并给出两者共同的总行程、夹紧行程、行程余量、
最低动作压力、使用温度和液压油要求。

### Standard Answer

`LSA0360-C□` 的夹紧侧油量为 1.6 cm³、释放侧油量为 1.3 cm³，最高使用压力
7.0 MPa，耐压 10.5 MPa，重量 0.5 kg。`LSE0360-C□` 的夹紧侧油量为
3.2 cm³、释放侧油量为 3.0 cm³，最高使用压力 6.0 MPa，耐压 9.0 MPa，
重量 0.7 kg。两者的总行程均为 3.5 mm，其中夹紧行程 2.5 mm、行程余量
1.0 mm；最低动作压力均为 0.5 MPa，使用温度均为 0～70 ℃，使用流体均为
相当于 ISO-VG32 的一般液压油。

### Scoring Standard

- P1 [15]: 正确给出 LSA 的夹紧侧/释放侧油量 1.6/1.3 cm³。
- P2 [15]: 正确给出 LSE 的夹紧侧/释放侧油量 3.2/3.0 cm³。
- P3 [15]: 正确给出 LSA 的最高使用压力 7.0 MPa、耐压 10.5 MPa。
- P4 [15]: 正确给出 LSE 的最高使用压力 6.0 MPa、耐压 9.0 MPa。
- P5 [10]: 正确给出 LSA/LSE 重量分别为 0.5/0.7 kg。
- P6 [15]: 正确给出共同的总行程 3.5 mm、夹紧行程 2.5 mm、余量 1.0 mm。
- P7 [5]: 正确给出共同的最低动作压力 0.5 MPa。
- P8 [10]: 正确给出共同的 0～70 ℃ 温度范围和 ISO-VG32 一般液压油要求。

### Accepted Variants

- 油量单位可用 `cm³`、`cm3` 或 `mL`，数值必须等价。
- 重量可换算为 LSA 500 g、LSE 700 g。

### Forbidden Errors

- 交换 LSA 与 LSE 的油量、压力或重量。
- 将最高使用压力写成耐压，或反之。
- 将总行程 3.5 mm 误写为夹紧行程。
- 省略液压油粘度等级或写成非 ISO-VG32。

### Tolerance

- 本题为规格表精确查询；数值仅接受等价单位换算，不接受近似值。

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 3-4, 9-10
- Printed page: 949-950, 955-956
- Section: LSA/LSE 规格
- Local scope path: LSA0360-C□ 与 LSE0360-C□ 的产品规格表
- Evidence type: TABLE + TEXT
- Evidence: 两个系列的规格表分别列出行程、油量、压力、温度、使用流体和重量。

## LSA-LSE-Q-0004

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: LSA/LSE 油压复动式侧向夹紧器
- Model / Scope: LSA0360-C□ 与 LSE0360-C□ 本体安装螺栓

### Question

安装 `LSA0360-C□` 或 `LSE0360-C□` 本体时，安装螺栓的规格、强度等级、
规定紧固力矩和安装孔使用要求分别是什么？

### Standard Answer

两个系列均使用 `M4×0.7` 安装螺栓，螺栓强度等级为 12.9，规定紧固力矩为
4.0 N·m，并且必须使用本体上的全部安装孔进行固定。

### Scoring Standard

- P1 [25]: 正确给出安装螺栓规格 `M4×0.7`。
- P2 [25]: 正确给出螺栓强度等级 12.9。
- P3 [25]: 正确给出紧固力矩 4.0 N·m。
- P4 [25]: 明确要求使用全部安装孔固定本体。

### Accepted Variants

- `M4×0.7` 可写为 `M4x0.7`。
- `N·m` 可写为 `Nm` 或 `N･m`。

### Forbidden Errors

- 给出其他螺纹规格、强度等级或紧固力矩。
- 声称可以只使用部分安装孔。
- 将速度控制阀本体力矩当作夹紧器本体安装力矩。

### Tolerance

- 紧固力矩必须为 4.0 N·m；不接受范围或近似值。

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 5-6, 11-12
- Printed page: 951-952, 957-958
- Section: 设计方面的注意事项
- Local scope path: LSA0360-C□ 与 LSE0360-C□ 本体安装要求
- Evidence type: TEXT + TABLE
- Evidence: 两个系列的设计注意事项均列出 M4×0.7、强度等级 12.9、4.0 N·m，并要求使用全部安装孔。

## LSA-LSE-Q-0005

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: BZL 低压用直装式速度控制阀
- Model / Scope: BZL0101-A 与 BZL0101-B；LSA/LSE 对应关系

### Question

解读 `BZL0101-A` 与 `BZL0101-B` 的型号字段，说明 `010`、设计编号 `1`、
控制方式 `A`/`B` 的含义；并分别给出 `LSA0360-C□` 与 `LSE0360-C□`
应采用的 BZL 型号和控制方式。

### Standard Answer

`BZL` 表示低压用直装式速度控制阀。`010` 中的螺纹尺寸代码 `10` 表示
G1/8A，后面的 `1` 是设计编号。后缀 `A` 表示进油节流，`B` 表示回油节流。
`LSA0360-C□` 对应 `BZL0101-B`，采用回油节流；`LSE0360-C□` 对应
`BZL0101-A`，必须采用进油节流。

### Scoring Standard

- P1 [15]: 正确说明 BZL 是低压用直装式速度控制阀。
- P2 [15]: 正确说明螺纹尺寸代码 `10` 表示 G1/8A。
- P3 [10]: 正确说明 `1` 是设计编号。
- P4 [15]: 正确说明 `A` 表示进油节流。
- P5 [15]: 正确说明 `B` 表示回油节流。
- P6 [15]: 正确匹配 LSA0360-C□ 与 BZL0101-B/回油节流。
- P7 [15]: 正确匹配 LSE0360-C□ 与 BZL0101-A/进油节流。

### Accepted Variants

- `进油节流` 可写为 `入口节流`。
- `回油节流` 可写为 `出口节流`。

### Forbidden Errors

- 交换 A/B 的控制方式。
- 交换 LSA 与 LSE 的 BZL 对应型号。
- 将 BZL 的 A/B 后缀作为 LSA/LSE 产品型号的一部分。
- 声称 LSE 应采用回油节流。

### Tolerance

- 型号、螺纹和控制方式必须精确匹配，不接受仅回答“安装速度控制阀”。

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 7-12, 21-22
- Printed page: 953-958, 1259-1260
- Section: LSE 特点 / LSA/LSE 设计注意事项 / BZL 型号表示、规格与对应机器型号
- Local scope path: LSA0360-C□、LSE0360-C□ 与 G1/8A BZL 速度控制阀的直接对应关系
- Evidence type: TEXT + MODEL + TABLE
- Evidence: LSE 产品页明确要求 BZL-A；BZL 型号页定义 10、1、A/B，并在对应机器型号表中分别列出 LSA0360-C□ 与 BZL0101-B、LSE0360-C□ 与 BZL0101-A。

## LSA-LSE-Q-0006

**Type: FACT**

### Target

- Binding: DOCUMENT_COMMON
- Product: LSA/LSE 可用直装式控制阀
- Model / Scope: LSA_LSE_R00_2023KW_C1N.pdf :: 控制阀系列概述及 BZX/JZG 规格

### Question

本 PDF 收录的直装式控制阀中，分别说明 BZL、BZX、JZG 和 BZS 的主要用途。
同时给出 BZX 与 JZG 的最高使用压力，并说明两者在功能上的关键差别。

### Standard Answer

BZL 是用于调节夹紧器动作速度的低压速度控制阀；BZX 是可直接安装并通过操作
扳手排除回路空气的排气阀；JZG 是带排气功能的 G 螺纹堵头；BZS 是用于控制
多个夹紧器定位、夹紧等先后顺序的直装式顺序阀。BZX 与 JZG 的最高使用压力
均为 35 MPa。两者的关键差别是 BZX 是独立排气阀，而 JZG 同时承担 G 螺纹
堵头和低压排气功能。

### Scoring Standard

- P1 [20]: 正确说明 BZL 用于调节夹紧器动作速度。
- P2 [20]: 正确说明 BZX 是通过操作扳手排除回路空气的排气阀。
- P3 [20]: 正确说明 JZG 是带排气功能的 G 螺纹堵头。
- P4 [20]: 正确说明 BZS 用于控制多个夹紧器的动作顺序。
- P5 [10]: 正确给出 BZX 与 JZG 的最高使用压力均为 35 MPa。
- P6 [10]: 正确区分 BZX 的独立排气阀用途与 JZG 的堵头兼排气用途。

### Accepted Variants

- `动作顺序` 可写为 `顺序动作` 或 `先后动作`。
- `排气阀` 可写为 `放气阀`。

### Forbidden Errors

- 将 BZL 说成顺序阀或堵头。
- 将 BZS 说成单纯的速度控制阀。
- 声称 JZG 不具备堵头功能。
- 给出 BZX/JZG 最高使用压力为 7 MPa。

### Tolerance

- 压力值必须为 35 MPa；各系列用途必须能够相互区分。

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 19-20, 25-30
- Printed page: 1257-1258, 1265-1270
- Section: 控制阀种类 / BZX 排气阀 / JZG 带排气功能堵头 / BZS 直装式顺序阀
- Local scope path: 本 PDF 控制阀章节中的 BZL、BZX、JZG、BZS 功能与 BZX/JZG 压力规格
- Evidence type: TEXT + TABLE
- Evidence: 控制阀概述页定义各类阀用途；BZX 与 JZG 规格页均列出 35 MPa 最高使用压力，并分别描述排气阀和带排气功能堵头。

## LSA-LSE-Q-0007

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: BZS 直装式顺序阀
- Model / Scope: BZS0100、BZS0200、BZS0300 规格与 LSA/LSE 兼容性

### Question

比较 `BZS0100`、`BZS0200` 与 `BZS0300`：给出三者的 G 螺纹尺寸和规定
紧固力矩，并给出它们共同的顺序动作压力调节范围、使用压力范围、耐压和开启压力。
`LSA0360-C□`、`LSE0360-C□` 对应哪个 BZS 型号？

### Standard Answer

`BZS0100`、`BZS0200`、`BZS0300` 的 G 螺纹尺寸依次为 G1/8A、G1/4A、
G3/8A，规定紧固力矩依次为 10、25、35 N·m。三者共同的顺序动作压力调节
范围为 1.0～6.0 MPa，使用压力范围为 2.0～7.0 MPa，耐压为 10.5 MPa，
开启压力为 0.03 MPa。`LSA0360-C□` 和 `LSE0360-C□` 均对应 `BZS0100`。

### Scoring Standard

- P1 [20]: 正确给出三个型号的螺纹尺寸依次为 G1/8A、G1/4A、G3/8A。
- P2 [20]: 正确给出紧固力矩依次为 10、25、35 N·m。
- P3 [15]: 正确给出顺序动作压力调节范围 1.0～6.0 MPa。
- P4 [15]: 正确给出使用压力范围 2.0～7.0 MPa。
- P5 [10]: 正确给出耐压 10.5 MPa。
- P6 [10]: 正确给出开启压力 0.03 MPa。
- P7 [10]: 正确说明 LSA0360-C□ 与 LSE0360-C□ 均对应 BZS0100。

### Accepted Variants

- 压力范围可使用连字符或“至”表达，但上下限不得改变。
- `N·m` 可写为 `Nm` 或 `N･m`。

### Forbidden Errors

- 交换型号与螺纹尺寸或紧固力矩的对应关系。
- 将调节范围与使用压力范围混淆。
- 将开启压力写成最低动作压力 0.5 MPa。
- 声称 LSA/LSE 036 型对应 BZS0200 或 BZS0300。

### Tolerance

- 本题所有规格值均为精确表格值，不接受近似或省略单位。

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 29-30
- Printed page: 1269-1270
- Section: BZS 型号表示 / 规格 / 对应机器型号
- Local scope path: BZS0100/BZS0200/BZS0300 规格表及 LSA0360-C□、LSE0360-C□ 对应表
- Evidence type: MODEL + TABLE + TEXT
- Evidence: BZS 型号与规格页定义螺纹代码和设计编号，列出压力、力矩规格，并在对应机器型号表中将 LSA0360-C□、LSE0360-C□ 列于 BZS0100。

## LSA-LSE-Q-0008

**Type: TABLE**

### Target

- Binding: DOCUMENT_COMMON
- Product: LSA/LSE PDF 通用符号参考
- Model / Scope: LSA_LSE_R00_2023KW_C1N.pdf :: 印刷页 1729-1730 的表面粗糙度与 O 形密封圈标示

### Question

根据通用符号更改表，给出新标示 `Rz 6.3`、`Rz 25`、`Rz 100` 分别对应的
算术平均粗糙度 Ra 参考值；并说明 O 形密封圈新标示中的 `NBR-70-1`、`NBR-90`、
`P` 和末尾 `N` 分别表示什么。

### Standard Answer

`Rz 6.3`、`Rz 25`、`Rz 100` 对应的 Ra 参考值依次为 1.6、6.3、25。
O 形密封圈新标示中，`NBR-70-1` 表示一般用三聚橡胶、A 型硬度 70，
`NBR-90` 表示一般用三聚橡胶、A 型硬度 90；`P` 是滑动用种类标记，末尾
`N` 表示一般用品质等级。

### Scoring Standard

- P1 [15]: 正确给出 Rz 6.3 对应 Ra 1.6。
- P2 [15]: 正确给出 Rz 25 对应 Ra 6.3。
- P3 [15]: 正确给出 Rz 100 对应 Ra 25。
- P4 [20]: 按 PDF 原文说明 NBR-70-1 为一般用三聚橡胶、A 型硬度 70。
- P5 [20]: 按 PDF 原文说明 NBR-90 为一般用三聚橡胶、A 型硬度 90。
- P6 [10]: 正确说明 P 表示滑动用。
- P7 [5]: 正确说明末尾 N 表示一般用品质等级。

### Accepted Variants

- `三聚橡胶` 可按材料代号写为 `NBR 橡胶`，但不得改变硬度等级。
- `A 型硬度` 可写为 `邵氏 A 硬度`。

### Forbidden Errors

- 将 Rz 数值直接当作 Ra 参考值。
- 交换 NBR-70-1 与 NBR-90 的硬度。
- 将 `P` 解释为压力或公称号。
- 将末尾 `N` 解释为材料识别符号。

### Tolerance

- Ra 参考值和硬度值必须与表格精确一致。

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 17-18
- Printed page: 1729-1730
- Section: 关于表面粗糙度、O 形密封圈的标示更改通知
- Local scope path: 表面粗糙度新旧标示比较与 O 形密封圈新标示字段定义
- Evidence type: TABLE + TEXT
- Evidence: 表面粗糙度表列出三个 Rz 等级及相应 Ra 参考值；O 形密封圈说明表定义材料识别符号、硬度、种类标记和品质等级。
