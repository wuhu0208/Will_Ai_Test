---
schema_version: will-ai-question-bank/v1
source_pdf: LHV_R00_2023KW_C1N.pdf
source_sha256: c137f9f1c4ce25d500d5e185311e8efe083a18bc08557bdaaac4b86288476f10
source_pages: 52
question_bank_version: V1
product_scope: LHV
---

# LHV_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: LHV_R00_2023KW_C1N.pdf
- SHA-256: c137f9f1c4ce25d500d5e185311e8efe083a18bc08557bdaaac4b86288476f10
- 物理页数: 52
- Product: KOSMEK LHV 单回路双向检知型低压油压复动旋转式夹紧器
- 来源证据原则: PDF 页面及其表格、公式、曲线、图示和文字为 Source Truth；文本提取仅用于导航，数值与视觉关系以页面证据为准。

## 2. Scope

### 2.1 产品与文档范围

本题库覆盖 LHV 的单气路双向动作确认、动作原理、型号表示、规格、夹紧力、容许动作时间、
压板设计、安装和专项注意事项。BZL 低压速度控制阀、LZH 压板附件和 LZV0010 传感单元
只在 Target 明确绑定对应附件或 LHV 适用范围时收录。油压系列通用的排气、速度回路、安全
和保养要求按 DOCUMENT_COMMON 绑定。标示变更、商业质量保证和销售网点不作为 LHV 技术题。

### 2.2 LHV 型号语法

LHV 型号按 LHV<主体尺寸><设计编号>-C<夹紧时旋转方向>E[-<选配件>] 组成。主体尺寸代码
040、048、055、065、075 对应本体外径 φD=40、48、55、65、75 mm；设计编号为 0；C 表示
板式配管型，配有 G 螺纹堵头，可安装另购 BZL；R/L 分别表示夹紧时顺时针/逆时针旋转；
E 为单回路双向检知型的固定动作确认记号；无选配件为标准锥形夹紧压板型，A 为快换压板 A 型。

### 2.3 来源清单

| Coverage ID | 物理页 | 局部范围 | Evidence type | 可测试对象 / 范围决定 | Priority / Disposition |
|---|---:|---|---|---|---|
| LHV-SI-001 | 1-4 | 油压旋转式夹紧器 > 全般 | TEXT + TABLE | 跨系列概览 | LOW：排除宣传比较；LHV 边界由本文件 Scope 固定 |
| LHV-SI-002 | 5-6 | LHV > 特点与结构 | TEXT + DRAWING | 低压复动、单气路双向确认、防尘与传感单元；覆盖 LHV-Q-0003、LHV-Q-0025 | HIGH：已映射 |
| LHV-SI-003 | 7-8 | LHV > 动作原理 | STATE_DIAGRAM + TABLE | 夹紧、途中、释放顺序及 OUT1/OUT2；覆盖 LHV-Q-0004、LHV-Q-0017 | HIGH：已映射 |
| LHV-SI-004 | 9-10 | LHV > 空气传感流程 | TABLE + CHART + DRAWING | 传感器、气压、连接数量、排气孔和清洁；覆盖 LHV-Q-0005、LHV-Q-0006、LHV-Q-0026 | HIGH：已映射 |
| LHV-SI-005 | 11-12 | LHV > 型号表示与规格 | MODEL + TABLE + FORMULA | 型号字段、尺寸代码、规格和公式；覆盖 LHV-Q-0001、LHV-Q-0002、LHV-Q-0007 至 LHV-Q-0012 | HIGH：已映射 |
| LHV-SI-006 | 13-14 | LHV > 夹紧力曲线 | CHART + TABLE + FORMULA | P、L、F 关系和不可使用范围；覆盖 LHV-Q-0011 至 LHV-Q-0013 | HIGH：已映射 |
| LHV-SI-007 | 15-16 | LHV > 容许动作时间 | CHART + FORMULA + TEXT | 惯性力矩、旋转/全动作时间与过快风险；覆盖 LHV-Q-0014、LHV-Q-0015 | HIGH：已映射 |
| LHV-SI-008 | 17-20 | LHV > 外形尺寸与 A 型 | TABLE + DRAWING | 安装接口、标准型和快换 A 型；覆盖 LHV-Q-0018、LHV-Q-0028 | MEDIUM：代表性覆盖，不做尺寸替换式扩增 |
| LHV-SI-009 | 21-22 | LHV > 压板设计与附件 | TABLE + DRAWING | 标准/A 型压板设计及 LZH 附件；覆盖 LHV-Q-0016、LHV-Q-0027 | HIGH：已映射 |
| LHV-SI-010 | 23-26 | 油压旋转式夹紧器 > 注意事项 | TEXT + TABLE + DRAWING | 回路、惯性、安装、压板和速度调整；覆盖 LHV-Q-0015、LHV-Q-0018、LHV-Q-0020、LHV-Q-0028 | HIGH：已映射 |
| LHV-SI-011 | 27-30 | 油压系列 > 通用事项 | TEXT + CIRCUIT_DIAGRAM | 排气、安全、保养和复动回油节流；覆盖 LHV-Q-0019 至 LHV-Q-0022 | HIGH：技术内容已映射；商业保修条款排除 |
| LHV-SI-012 | 31-32 | 标示更改通知 | TABLE + TEXT | 表面粗糙度和 O 形圈标示历史 | EXCLUDED：行政性标示换代，不是 LHV 核心技术知识 |
| LHV-SI-013 | 33-38 | 控制阀 > BZL 低压速度控制阀 | MODEL + TABLE + DRAWING | BZL-B 规格、LHV 适配及安装限制；覆盖 LHV-Q-0020、LHV-Q-0023、LHV-Q-0024 | MEDIUM：已映射 |
| LHV-SI-014 | 39-46 | BZX/JZG/BZS 控制阀附件 | MODEL + TABLE | 其他控制阀和顺序阀 | EXCLUDED：未与 LHV 当前选型问题唯一绑定，不扩增附件目录题 |
| LHV-SI-015 | 47-50 | 传感单元 > LZV0010 | MODEL + TABLE + DRAWING | LHV 适用型号、输出和清洁；覆盖 LHV-Q-0025、LHV-Q-0026 | MEDIUM：已映射 |
| LHV-SI-016 | 51-52 | 公司与销售网点 | TEXT | 联系方式 | EXCLUDED：非耐久产品技术知识 |

## 3. Question Statistics

- Total: 28
- Direct LHV: 19
- Accessory / Related Product: 5
- Document Common: 4
- FACT: 3
- SPEC_LOOKUP: 3
- MODEL: 3
- TABLE: 4
- CALCULATION: 2
- CHART: 2
- PROCEDURE: 6
- CAUTION: 5

## 4. Questions

## LHV-Q-0001

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LHV
- Model / Scope: LHV0480-CRE-A

### Question

按资料解析 LHV0480-CRE-A，说明主体尺寸及 φD、设计编号、配管方式、夹紧时旋转方向、
E 的动作确认含义和选配件。

### Standard Answer

LHV 为单回路双向检知型旋转式夹紧器；048 是主体尺寸代码，对应 φD=48 mm；0 是设计编号；
C 为板式配管型，配有 G 螺纹堵头，可安装另购 BZL；R 为夹紧时顺时针旋转；E 表示单回路
双向动作确认；A 为快换压板 A 型。

### Scoring Standard

- P1 [15]: LHV 系列身份
- P2 [15]: 048 主体尺寸
- P3 [10]: φD=48 mm
- P4 [10]: 设计编号 0
- P5 [15]: C 为板式配管型并配 G 螺纹堵头
- P6 [10]: BZL 需另购
- P7 [10]: R 为夹紧时顺时针
- P8 [10]: E 为单回路双向确认
- P9 [5]: A 为快换压板 A 型

### Accepted Variants

- 板式配管型可写为板式连接型。

### Forbidden Errors

- 不得把 R 解释为释放方向或把 A 解释为传感器输出。

### Tolerance

- 型号代码和 φD 须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 11
- Printed page: 591
- Section: 型号表示
- Local scope path: LHV > 型号表示 > LHV0480-CRE-A
- Evidence type: MODEL + DRAWING
- Evidence: 型号图依次定义主体尺寸、设计编号、C、R/L 和选配件，并显示固定 E。

## LHV-Q-0002

**Type: MODEL**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: LHV 型号语法

### Question

判断以下型号是否合法并说明理由：LHV0400-CLE、LHV0550-CRE-A、LHV0600-CRE、
LHV0481-CRE、LHV0650-BRE、LHV0750-CCE。

### Standard Answer

LHV0400-CLE 和 LHV0550-CRE-A 合法。LHV0600-CRE 不合法，因为没有 060 主体尺寸；
LHV0481-CRE 不合法，因为设计编号为 0；LHV0650-BRE 不合法，因为配管方式为 C；
LHV0750-CCE 不合法，因为旋转方向只有 R/L，没有 C。

### Scoring Standard

- P1 [15]: 正确判定 LHV0400-CLE
- P2 [15]: 正确判定 LHV0550-CRE-A
- P3 [20]: 排除 060 主体尺寸
- P4 [15]: 排除设计编号 1
- P5 [20]: 排除配管方式 B
- P6 [15]: 排除旋转方向 C

### Accepted Variants

- 可用字段表逐项判断。

### Forbidden Errors

- 不得并入其他旋转夹紧器的尺寸或配管代码。

### Tolerance

- 合法性与代码须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 11
- Printed page: 591
- Section: 型号表示
- Local scope path: LHV > 型号表示 > 字段允许值
- Evidence type: MODEL
- Evidence: 页面仅列出 040/048/055/065/075、设计 0、配管 C、旋转 R/L 和选配无符号/A。

## LHV-Q-0003

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 产品特点

### Question

LHV 属于什么压力和动作类型？它如何用空气回路确认夹紧与释放？

### Standard Answer

LHV 是 1.5 至 7 MPa 低压油压复动旋转式夹紧器，采用单回路双向检知机构，仅用一路常供气
配合双输出空气传感器即可确认夹紧和释放两种动作。

### Scoring Standard

- P1 [20]: 低压范围 1.5 至 7 MPa
- P2 [20]: 油压复动旋转式夹紧器
- P3 [25]: 单回路双向检知
- P4 [20]: 仅用一路常供气
- P5 [15]: 确认夹紧和释放两种动作

### Accepted Variants

- 释放可写为松开。

### Forbidden Errors

- 不得说成单动或需要两路确认气。

### Tolerance

- 压力范围须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 5
- Printed page: 585
- Section: 特点
- Local scope path: LHV > 单回路双向检知特点
- Evidence type: TEXT + DRAWING
- Evidence: 页面标明低压 1.5 至 7 MPa、液压复动，并对比一路气与传统两路气。

## LHV-Q-0004

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 夹紧、动作途中、释放状态

### Question

列出 LHV 在夹紧、旋转动作途中和释放状态下的夹紧油压、释放油压、OUT1 与 OUT2 状态。

### Standard Answer

夹紧：夹紧油压 ON、释放油压 OFF、OUT1 ON、OUT2 OFF；动作途中：OUT1 和 OUT2 均 OFF，
油压由当前动作方向决定；释放：夹紧油压 OFF、释放油压 ON、OUT1 OFF、OUT2 ON。

### Scoring Standard

- P1 [20]: 夹紧油压 ON、释放油压 OFF
- P2 [20]: 夹紧时 OUT1 ON、OUT2 OFF
- P3 [20]: 途中两输出均 OFF
- P4 [20]: 释放油压 ON、夹紧油压 OFF
- P5 [20]: 释放时 OUT1 OFF、OUT2 ON

### Accepted Variants

- ON/OFF 可写为接通/断开。

### Forbidden Errors

- 不得颠倒 OUT1/OUT2 或把途中输出写成 ON。

### Tolerance

- 状态须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 587
- Section: 动作原理（内部结构）
- Local scope path: LHV > 动作原理 > 三状态表
- Evidence type: STATE_DIAGRAM + TABLE
- Evidence: 页面按夹紧、旋转途中和释放给出两侧油压与 OUT1/OUT2。

## LHV-Q-0005

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 排气孔与检出气口

### Question

说明 LHV 排气孔和空气传感器检出气口的设计要求，以及违反要求的后果。

### Standard Answer

排气孔必须向大气开放并防止冷却液和切削屑进入；堵塞会使空气传感器误动作。检出气口应装
低开启压力单向阀，推荐 SMC AKH 系列，开启压力 0.005 MPa，以降低异物侵入风险。

### Scoring Standard

- P1 [20]: 排气孔向大气开放
- P2 [20]: 防止冷却液和切削屑侵入
- P3 [20]: 堵塞导致传感器误动作
- P4 [20]: 检出气口装低开启压力单向阀
- P5 [20]: 推荐 AKH、开启压力 0.005 MPa

### Accepted Variants

- 误动作可写为错误检测。

### Forbidden Errors

- 不得封堵排气孔或把 0.005 MPa 当作供气压力。

### Tolerance

- 开启压力须为 0.005 MPa。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 589
- Section: 关于传感的说明
- Local scope path: LHV > 空气传感 > 排气孔与单向阀
- Evidence type: CAUTION + CIRCUIT_DIAGRAM
- Evidence: 页面要求排气孔开放防侵入，并给出 AKH 与 0.005 MPa。

## LHV-Q-0006

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 推荐空气传感条件

### Question

给出 LHV 推荐空气传感器类型、单传感器连接数量、单台连接限制、推荐气压和连接 4 台时下限。

### Standard Answer

推荐 SMC ISA3-G 系列 2 点输出型；一台传感器通常连接 2 至 4 台夹紧器，连接 1 台须咨询；
推荐空气压力 0.1 至 0.2 MPa，连接 4 台时须在 0.15 MPa 以上。

### Scoring Standard

- P1 [20]: ISA3-G 系列
- P2 [15]: 2 点输出型
- P3 [20]: 连接 2 至 4 台
- P4 [15]: 1 台须咨询
- P5 [15]: 推荐 0.1 至 0.2 MPa
- P6 [15]: 4 台时至少 0.15 MPa

### Accepted Variants

- 2 点输出可写为双输出。

### Forbidden Errors

- 不得把 0.6 MPa 回路上限标注当作推荐压力。

### Tolerance

- 数量和压力须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 9
- Printed page: 589
- Section: 关于空气传感元件
- Local scope path: LHV > 推荐空气传感器表
- Evidence type: TABLE
- Evidence: 页面列出 ISA3-G、2 至 4 台、单台咨询和推荐压力。

## LHV-Q-0007

**Type: SPEC_LOOKUP**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 系列通用规格

### Question

给出 LHV 的最高使用压力、耐压、无负载最低动作压力、旋转角度精度、夹紧位置重复精度、
推荐空气压力、温度和使用流体。

### Standard Answer

最高 7 MPa，耐压 10.5 MPa；无负载最低动作压力 LHV0400 为 2.0 MPa，其余尺寸为 1.5 MPa；
旋转角度 90°±3°，夹紧位置重复精度 ±0.5°；空气 0.1 至 0.2 MPa；温度 0 至 70 ℃；
使用相当于 ISO-VG-32 的一般液压油。

### Scoring Standard

- P1 [15]: 最高 7 MPa
- P2 [10]: 耐压 10.5 MPa
- P3 [20]: 最低压力 040 为 2.0、其余 1.5 MPa
- P4 [15]: 90°±3°
- P5 [10]: 重复精度 ±0.5°
- P6 [10]: 空气 0.1 至 0.2 MPa
- P7 [10]: 0 至 70 ℃
- P8 [10]: ISO-VG-32 一般液压油

### Accepted Variants

- ISO VG 32 写法可接受。

### Forbidden Errors

- 不得把耐压作为正常使用上限或省略最低压力的尺寸差异。

### Tolerance

- 数值须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 592
- Section: 规格
- Local scope path: LHV > 规格表 > 通用与尺寸差异
- Evidence type: TABLE
- Evidence: 规格表给出压力、角度、空气、温度和流体，脚注限定无负载最低动作压力。

## LHV-Q-0008

**Type: SPEC_LOOKUP**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHV
- Model / Scope: LHV0550-C□E[-A]

### Question

查询 LHV0550 的夹紧侧面积、内径、活塞杆径、夹紧/释放容量、全行程、90°旋转行程、
夹紧行程和标准锥形压板型单体重量。

### Standard Answer

夹紧侧面积 8.95 cm²，内径 42 mm，活塞杆径 25 mm；夹紧容量 16.5 cm³，释放容量
19.6 cm³；全行程 18.5 mm，旋转行程 8.5 mm，夹紧行程 10 mm；标准型重量 2.0 kg。

### Scoring Standard

- P1 [15]: 8.95 cm²
- P2 [10]: 内径 42 mm
- P3 [10]: 活塞杆径 25 mm
- P4 [15]: 夹紧容量 16.5 cm³
- P5 [15]: 释放容量 19.6 cm³
- P6 [15]: 全行程 18.5 mm
- P7 [10]: 旋转 8.5 mm、夹紧 10 mm
- P8 [10]: 标准型 2.0 kg

### Accepted Variants

- cm2、cm3 可使用上标。

### Forbidden Errors

- 不得颠倒两侧容量或把 A 型 1.9 kg 当作标准型重量。

### Tolerance

- 表列值须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 12
- Printed page: 592
- Section: 规格
- Local scope path: LHV > 规格表 > LHV0550
- Evidence type: TABLE
- Evidence: LHV0550 列给出面积、直径、容量、行程和两类重量。

## LHV-Q-0009

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 主体尺寸与 φD

### Question

列出 LHV 全部主体尺寸代码及对应本体外径 φD。

### Standard Answer

040→40 mm；048→48 mm；055→55 mm；065→65 mm；075→75 mm。

### Scoring Standard

- P1 [20]: 040→40 mm
- P2 [20]: 048→48 mm
- P3 [20]: 055→55 mm
- P4 [20]: 065→65 mm
- P5 [20]: 075→75 mm

### Accepted Variants

- 可用表格回答。

### Forbidden Errors

- 不得加入 036、090、105 等其他系列尺寸。

### Tolerance

- 代码和尺寸须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 11
- Printed page: 591
- Section: 型号表示
- Local scope path: LHV > 主体尺寸
- Evidence type: TABLE + DRAWING
- Evidence: 型号页逐一列出五个尺寸代码和 φD。

## LHV-Q-0010

**Type: TABLE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 旋转方向与压板选配

### Question

说明 R、L 旋转方向和无符号、A 两种压板选配的含义。

### Standard Answer

R 为夹紧时顺时针旋转，L 为夹紧时逆时针旋转；无符号为标准锥形夹紧压板型，A 为快换压板 A 型。

### Scoring Standard

- P1 [25]: R 为夹紧时顺时针
- P2 [25]: L 为夹紧时逆时针
- P3 [25]: 无符号为标准锥形夹紧压板型
- P4 [25]: A 为快换压板 A 型

### Accepted Variants

- 顺/逆时针须以夹紧动作表述。

### Forbidden Errors

- 不得以释放方向定义 R/L。

### Tolerance

- 映射须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 11
- Printed page: 591
- Section: 型号表示
- Local scope path: LHV > 旋转方向与选配件
- Evidence type: TABLE + DRAWING
- Evidence: 页面图示 R/L 的夹紧方向，并列出无符号/A。

## LHV-Q-0011

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHV
- Model / Scope: LHV0480-C□E[-A]

### Question

LHV0480 在 P=5.5 MPa、压板长度 L=90 mm 时，按公式计算夹紧力 F，并按 ROUND_HALF_UP
保留到 0.1 kN。

### Standard Answer

F=P/(1.7183+0.0058×L)=5.5/(1.7183+0.0058×90)=5.5/2.2403=
2.455028... kN，按 ROUND_HALF_UP 得 2.5 kN。

### Scoring Standard

- P1 [25]: 公式 F=P/(1.7183+0.0058×L)
- P2 [20]: 正确代入 P=5.5、L=90
- P3 [20]: 分母 2.2403
- P4 [20]: 未舍入值 2.455028... kN
- P5 [15]: 最终 2.5 kN

### Accepted Variants

- 中间值可保留更多有效数字。

### Forbidden Errors

- 不得套用其他尺寸公式或把 L 当作厘米。

### Tolerance

- 最终接受结果按 ROUND_HALF_UP 保留到 0.1 kN 后必须精确为 2.5 kN。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 593
- Section: 夹紧力曲线图
- Local scope path: LHV > 夹紧力 > LHV0480 公式
- Evidence type: FORMULA + CHART
- Evidence: 页面给出 LHV0480 的公式以及 F、P、L 单位。

## LHV-Q-0012

**Type: CALCULATION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHV
- Model / Scope: LHV0650-C□E[-A]

### Question

LHV0650 在 L=120 mm 时需要 F=5.0 kN，反算压力 P，按 ROUND_HALF_UP 保留到 0.1 MPa，
并判断是否超过该长度对应最高压力 6.8 MPa。

### Standard Answer

由 F=P/(0.7958+0.0024×L)，得 P=F×(0.7958+0.0024×L)=
5.0×(0.7958+0.288)=5.41900 MPa，舍入为 5.4 MPa；未超过 L=120 mm 时的 6.8 MPa。
用 5.4 MPa 回代，F=5.4/1.0838=4.982... kN，按 0.1 kN 为 5.0 kN。

### Scoring Standard

- P1 [20]: 选择 LHV0650 公式
- P2 [20]: 正确变形 P=F×(0.7958+0.0024×L)
- P3 [20]: 未舍入值 5.41900 MPa
- P4 [20]: 最终 5.4 MPa 且未超过 6.8 MPa
- P5 [20]: 回代约 4.982 kN，舍入为 5.0 kN

### Accepted Variants

- 未舍入值可保留更多位数。

### Forbidden Errors

- 不得只用系列 7 MPa 上限而忽略 L=120 mm 对应上限。

### Tolerance

- 最终压力按 ROUND_HALF_UP 保留到 0.1 MPa 后必须精确为 5.4 MPa。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 14
- Printed page: 594
- Section: 夹紧力曲线图
- Local scope path: LHV > 夹紧力 > LHV0650 公式与压力上限
- Evidence type: FORMULA + TABLE
- Evidence: 页面给出公式，并在 L=120 mm 列给出最高使用压力 6.8 MPa。

## LHV-Q-0013

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHV
- Model / Scope: LHV0550 夹紧力曲线

### Question

从曲线视觉读取 LHV0550 在 P=4.2 MPa、L=130 mm 时的夹紧力，并用公式作一致性检查。

### Standard Answer

视觉读图约为 2.6 kN。公式检查 F=4.2/(1.1179+0.0038×130)=2.6056... kN，
与约 2.6 kN 的图上读数一致；公式仅用于检查视觉 Gold。

### Scoring Standard

- P1 [40]: 视觉读图约 2.6 kN
- P2 [20]: 识别 P=4.2 MPa
- P3 [15]: 识别 L=130 mm 曲线位置
- P4 [15]: 公式检查约 2.606 kN
- P5 [10]: 判断与视觉读数一致

### Accepted Variants

- 2.4 至 2.8 kN 的视觉读图结果均可接受。

### Forbidden Errors

- 不得把公式计算替代视觉取证或读取其他机型曲线。

### Tolerance

- Gold: 2.6 kN；视觉容差 2.4-2.8 kN。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 13
- Printed page: 593
- Section: 夹紧力曲线图
- Local scope path: LHV > 夹紧力曲线 > LHV0550
- Evidence type: CHART + FORMULA
- Evidence: 非离散 P=4.2、L=130 位置的视觉读数约 2.6 kN，公式作辅助校验。

## LHV-Q-0014

**Type: CHART**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHV
- Model / Scope: LHV0480 容许动作时间曲线

### Question

压板惯性力矩为 0.009 kg·m² 时，从 LHV0480 曲线视觉读取夹紧 90°旋转时间和释放 90°
旋转时间至少约为多少。

### Standard Answer

实线 90°旋转曲线在该非离散惯性力矩处，对应夹紧时间约 0.50 s、释放时间约 0.25 s。
实际调整应使时间不短于曲线读数。

### Scoring Standard

- P1 [25]: 选择 LHV0480 曲线
- P2 [20]: 选择实线 90°旋转曲线
- P3 [25]: 夹紧约 0.50 s
- P4 [20]: 释放约 0.25 s
- P5 [10]: 实际时间不得短于曲线值

### Accepted Variants

- 夹紧 0.45-0.55 s、释放 0.22-0.28 s 均可接受。

### Forbidden Errors

- 不得读取虚线全动作曲线或颠倒夹紧/释放横轴。

### Tolerance

- 夹紧 Gold 0.50 s，容差 0.45-0.55 s；释放 Gold 0.25 s，容差 0.22-0.28 s。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 15
- Printed page: 595
- Section: 容许动作时间图表
- Local scope path: LHV > 容许动作时间 > LHV0480
- Evidence type: CHART
- Evidence: 实线以惯性力矩映射夹紧上轴和释放下轴的 90°旋转时间。

## LHV-Q-0015

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 惯性力矩与动作时间边界

### Question

说明 LHV 动作时间为何必须按压板惯性力矩设定，并给出最短 90°旋转时间和过快风险。

### Standard Answer

应按实际压板惯性力矩查对应机型曲线，使动作时间不短于曲线值；即使惯性力矩很小，夹紧
90°旋转也不得短于 0.2 s，释放不得短于 0.1 s。动作过快会使停止精度恶化并损伤内部零件；
惯性过大还可能使压板无法旋转。

### Scoring Standard

- P1 [20]: 按实际惯性力矩查曲线
- P2 [20]: 时间不得短于曲线值
- P3 [15]: 夹紧最短 0.2 s
- P4 [15]: 释放最短 0.1 s
- P5 [20]: 过快导致停止精度恶化和内部损伤
- P6 [10]: 惯性过大可能无法旋转

### Accepted Variants

- 停止精度可写为停止位置精度。

### Forbidden Errors

- 不得把动作时间曲线当作最大时间或忽略最短时间。

### Tolerance

- 两个最短时间须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 15
- Printed page: 595
- Section: 容许动作时间图表
- Local scope path: LHV > 动作时间调整 > 注意事项
- Evidence type: CAUTION + CHART
- Evidence: 页面要求慢于曲线，并规定 0.2/0.1 s 下限及过快后果。

## LHV-Q-0016

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 自制旋转压板设计

### Question

设计 LHV 标准型或 A 型自制压板时，应如何确定长度、尺寸和定位结构？

### Standard Answer

先按所需夹紧力、压力和机型从能力曲线确定压板长度，再严格按相应标准锥面结合式或快换
A 型设计表加工全部配合尺寸；否则会夹紧力不足、变形、卡住或动作不良。标准型定位销孔
按需要加工且定位销由用户自备；A 型应按本体相位槽加工挡销兼相位调整销孔，挡销也由用户自备。

### Scoring Standard

- P1 [20]: 从能力曲线确定长度
- P2 [20]: 按实际机型和选配选择对应设计表
- P3 [20]: 严格遵守配合尺寸
- P4 [15]: 指出夹紧力不足、变形、卡住或动作不良风险
- P5 [10]: 标准型定位孔按需且销自备
- P6 [15]: A 型按相位槽加工挡销孔且挡销自备

### Accepted Variants

- 挡销可写为相位调整销。

### Forbidden Errors

- 不得仅按空间尺寸任意确定压板长度。

### Tolerance

- N/A

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 21
- Printed page: 601
- Section: 压板设计尺寸/附件
- Local scope path: LHV > 标准型与 A 型压板设计
- Evidence type: PROCEDURE + TABLE + DRAWING
- Evidence: 页面规定由能力曲线确定长度、按表加工和两类定位结构。

## LHV-Q-0017

**Type: FACT**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK LHV
- Model / Scope: 夹紧与释放动作顺序

### Question

说明 LHV 从释放到夹紧、再从夹紧到释放时，旋转行程和直线夹紧行程的先后顺序。

### Standard Answer

夹紧时，活塞杆先边下降边旋转，旋转结束后再垂直下降夹紧工件；释放时，活塞杆先垂直上升
解除夹紧，直线行程结束后再边旋转边上升回到释放端。

### Scoring Standard

- P1 [25]: 夹紧先下降旋转
- P2 [25]: 旋转结束后垂直夹紧
- P3 [25]: 释放先垂直上升
- P4 [25]: 随后旋转上升到释放端

### Accepted Variants

- 可按时间顺序列表回答。

### Forbidden Errors

- 不得颠倒旋转与直线夹紧行程顺序。

### Tolerance

- 顺序须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 7
- Printed page: 587
- Section: 动作原理（内部结构）
- Local scope path: LHV > 夹紧与释放机械顺序
- Evidence type: STATE_DIAGRAM + TEXT
- Evidence: 页面分别用箭头说明夹紧和释放的两阶段动作。

## LHV-Q-0018

**Type: PROCEDURE**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHV
- Model / Scope: LHV0550 标准锥形压板型安装

### Question

安装 LHV0550 本体和标准锥形旋转压板时，说明本体螺栓、强度等级、孔位、扭矩，以及压板
连接面处理、螺母规格和扭矩。

### Standard Answer

本体使用全部安装孔，以强度等级 12.9 的 M6 内六角螺栓按 14 N·m 紧固；过紧会使基座塌陷
或螺栓咬死。压板、锥套和活塞杆连接面必须脱脂清洗去除油污异物；LHV0550 标准型压板螺母
为 M22×1.5，紧固扭矩 84 至 100 N·m。

### Scoring Standard

- P1 [15]: 使用全部安装孔
- P2 [15]: M6、强度等级 12.9
- P3 [15]: 本体扭矩 14 N·m
- P4 [15]: 过紧风险
- P5 [15]: 连接面脱脂清洗
- P6 [10]: M22×1.5
- P7 [15]: 84 至 100 N·m

### Accepted Variants

- 咬死可写为热粘或卡死。

### Forbidden Errors

- 不得使用 A 型的 M6、8 N·m 压板紧固数据替代标准型螺母数据。

### Tolerance

- 螺栓、螺母和扭矩须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 23-24
- Printed page: 745-746
- Section: 油压旋转式夹紧器注意事项
- Local scope path: 旋转夹紧器 > 本体安装与标准压板安装 > LHV0550
- Evidence type: PROCEDURE + TABLE
- Evidence: 本体表给出 M6/14 N·m，压板表给出 M22×1.5/84-100 N·m，并要求清洁连接面。

## LHV-Q-0019

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 油压夹紧器
- Model / Scope: LHV_R00_2023KW_C1N.pdf :: 油压系列通用油路排气

### Question

LHV 油路混入空气时，给出安全排气步骤和推荐位置。

### Standard Answer

将供油压力调到 2 MPa 以下；松开距夹紧器最近的管接头螺母约一圈；左右摇动配管，排出含气
液压油；空气排尽后重新紧固。优先在回路最高处或末端排气，板式配管应在最高处附近设排气阀。

### Scoring Standard

- P1 [20]: 压力 2 MPa 以下
- P2 [20]: 最近接头松约一圈
- P3 [20]: 摇动配管排出含气油
- P4 [20]: 排尽后重新紧固
- P5 [20]: 最高处或末端排气

### Accepted Variants

- 管接头可写为配管接头。

### Forbidden Errors

- 不得在高压状态排气或完全拆下接头。

### Tolerance

- 须明确 2 MPa 以下。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 27
- Printed page: 1725
- Section: 安装施工方面的注意事项（油压系列通用）
- Local scope path: 油压系列 > 排净油压回路内的空气
- Evidence type: PROCEDURE + DRAWING
- Evidence: 页面给出五步排气和推荐位置。

## LHV-Q-0020

**Type: CAUTION**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK LHV
- Model / Scope: LHV_R00_2023KW_C1N.pdf :: LHV 复动速度控制回路

### Question

LHV 的夹紧侧和释放侧应采用哪种节流回路？为何不优先采用进油节流？

### Standard Answer

LHV 属于资料所列的一般复动夹紧器，两侧均采用回油节流（meter-out）；对应直接安装 BZL 时
应选 B 控制方式。进油节流易受油路混入空气影响，难以稳定控制速度。若采用回油节流，还应
控制供油量，避免动作中回路压力异常上升。

### Scoring Standard

- P1 [25]: 夹紧侧回油节流
- P2 [25]: 释放侧回油节流
- P3 [15]: BZL 选 B 控制方式
- P4 [20]: 进油节流易受混入空气影响
- P5 [15]: 回油节流需防止动作中压力上升

### Accepted Variants

- 回油节流可写 meter-out。

### Forbidden Errors

- 不得套用 TLA/TLV/TMV 等例外产品的两侧进油节流规则到 LHV。

### Tolerance

- N/A

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 27-28
- Printed page: 1725-1726
- Section: 夹紧器的速度控制回路及注意事项
- Local scope path: 油压系列 > 复动夹紧器 > LHV 回油节流
- Evidence type: CAUTION + CIRCUIT_DIAGRAM
- Evidence: 通用页规定非例外复动夹紧器两侧回油节流，并说明空气和回路压力风险。

## LHV-Q-0021

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 油压夹紧器
- Model / Scope: LHV_R00_2023KW_C1N.pdf :: 油压系列通用拆卸与复机安全

### Question

拆卸、维护 LHV 并重新启动时，应执行哪些基本安全步骤？

### Standard Answer

先防止被驱动物体坠落和设备误动作；切断压力源和电源，确认油压、气压回路压力为零；等待
设备完全冷却后再拆卸。重新启动前检查螺栓等连接部位无异常，再低风险试运行确认动作正常。

### Scoring Standard

- P1 [20]: 防坠落和误动作
- P2 [20]: 切断压力源和电源
- P3 [20]: 确认油压、气压为零
- P4 [20]: 待设备冷却
- P5 [20]: 复机前检查连接并试运行

### Accepted Variants

- 可补充锁定挂牌，但不能替代零压确认。

### Forbidden Errors

- 不得在残压或高温状态拆卸。

### Tolerance

- N/A

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 29
- Printed page: 1727
- Section: 操作方面的注意事项
- Local scope path: 油压系列 > 拆卸与重新启动
- Evidence type: PROCEDURE + CAUTION
- Evidence: 通用页要求防坠落、隔离能源、零压、冷却和复机检查。

## LHV-Q-0022

**Type: PROCEDURE**

### Target

- Binding: DOCUMENT_COMMON
- Product: KOSMEK 油压夹紧器
- Model / Scope: LHV_R00_2023KW_C1N.pdf :: 油压系列通用保养检查

### Question

给出 LHV 日常保养的重点清洁和检查项目，并说明污物的后果。

### Standard Answer

定期清洁活塞杆、柱塞周围；污物会损伤密封，导致动作不正常或漏油。检查配管、安装螺栓、
螺母、固定环和夹紧器有无松动，检查液压油老化、异常噪声以及动作是否正常顺畅；长期闲置后
重新启用尤其要确认动作状况。

### Scoring Standard

- P1 [20]: 清洁活塞杆和柱塞周围
- P2 [20]: 污物损伤密封并导致动作不良或漏油
- P3 [20]: 检查配管和紧固件松动
- P4 [20]: 检查液压油老化
- P5 [20]: 检查噪声、动作及长期闲置后状态

### Accepted Variants

- 动作不正常可写为动作不良。

### Forbidden Errors

- 不得在发现漏油、松动或异常动作后继续使用。

### Tolerance

- N/A

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 29
- Printed page: 1727
- Section: 保养、检查
- Local scope path: 油压系列 > 清洁与定期检查
- Evidence type: PROCEDURE + CAUTION
- Evidence: 页面列出运动部位清洁、松动、油液、噪声和动作检查。

## LHV-Q-0023

**Type: TABLE**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK BZL 低压速度控制阀
- Model / Scope: LHV0550 适配 BZL0101-B

### Question

LHV0550 应选用哪种直接安装 BZL？给出最高压力、耐压、控制方式、螺纹、开启压力、最大流道
面积、本体推荐紧固扭矩和重量。

### Standard Answer

选 BZL0101-B；最高使用压力 7 MPa，耐压 10.5 MPa，回油节流；G1/8A，开启压力
0.12 MPa，最大流道面积 2.6 mm²，本体推荐紧固扭矩 10 N·m，重量 12 g。

### Scoring Standard

- P1 [20]: BZL0101-B
- P2 [15]: 最高 7 MPa、耐压 10.5 MPa
- P3 [15]: 回油节流
- P4 [10]: G1/8A
- P5 [10]: 开启压力 0.12 MPa
- P6 [10]: 2.6 mm²
- P7 [10]: 10 N·m
- P8 [10]: 12 g

### Accepted Variants

- 最大流道面积可写为最大通流面积。

### Forbidden Errors

- 不得选进油节流 A 型或 LHV0650/0750 使用的 BZL0201-B。

### Tolerance

- 型号和数值须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 35-36
- Printed page: 1259-1260
- Section: BZL 低压速度控制阀
- Local scope path: BZL > 规格与对应机型 > LHV0550
- Evidence type: TABLE + ACCESSORY_MAPPING
- Evidence: 对应表将 LHV0550 映射至 BZL0101-B，规格表给出参数。

## LHV-Q-0024

**Type: CAUTION**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK BZL 低压速度控制阀
- Model / Scope: BZL-B 用于 LHV

### Question

在 LHV 上安装或更换 BZL-B 时，说明紧固、跨夹紧器复用、端口方向和调速起点要求。

### Standard Answer

必须按对应 BZL 的本体推荐扭矩安装，因为端面为金属密封，扭矩不足会密封不良并无法调流量；
以前使用过的 BZL 不得换装到其他夹紧器上重复使用。P1 接供油侧、P2 接夹紧器侧；调速时先
从低速小流量侧开始，再逐步向高速大流量侧调整。

### Scoring Standard

- P1 [20]: 按对应推荐扭矩安装
- P2 [20]: 扭矩不足导致金属密封不良和无法调流量
- P3 [20]: 已使用 BZL 不得换装到其他夹紧器复用
- P4 [20]: P1 供油侧、P2 夹紧器侧
- P5 [20]: 从低速小流量侧逐步调高

### Accepted Variants

- 供油侧可写为压力源侧。

### Forbidden Errors

- 不得把跨夹紧器限制扩大成来源未规定的绝对复用禁令，也不得反接 P1/P2。

### Tolerance

- N/A

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 25, 35
- Printed page: 747, 1259
- Section: 速度调整 / BZL 注意事项
- Local scope path: LHV > BZL-B 安装与调整
- Evidence type: CAUTION + DRAWING + TABLE
- Evidence: 产品页规定低速起调；BZL 页规定扭矩、跨夹紧器复用限制和端口方向。

## LHV-Q-0025

**Type: MODEL**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK 传感单元 LZV0010
- Model / Scope: LZV0010-C3HA

### Question

解析 LZV0010-C3HA 的设计编号、适用夹紧器组、连接数量、传感器供气压力和输出方式，
并说明是否适配 LHV。

### Standard Answer

设计编号 0；C 为包含 LHV 在内的单回路双向检知夹紧器组；3 表示连接 3 台夹紧器；
H 表示 0.200 MPa；A 表示 NPN 输出。因此该型号适配 3 台 LHV。

### Scoring Standard

- P1 [15]: 设计编号 0
- P2 [20]: C 组包含 LHV
- P3 [20]: 连接 3 台
- P4 [20]: H 为 0.200 MPa
- P5 [15]: A 为 NPN
- P6 [10]: 判断适配 3 台 LHV

### Accepted Variants

- 0.200 MPa 可写为 0.2 MPa。

### Forbidden Errors

- 不得把 C 当作 LHV 配管方式或把 A 当作 PNP。

### Tolerance

- 字段须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 47
- Printed page: 1713
- Section: 传感单元 LZV0010 型号表示
- Local scope path: LZV0010 > 型号表示 > LZV0010-C3HA
- Evidence type: MODEL + TABLE
- Evidence: 型号图定义 0/C/3/H/A，C 适用组明确包含 LHV。

## LHV-Q-0026

**Type: PROCEDURE**

### Target

- Binding: PRODUCT_SERIES
- Product: KOSMEK 传感单元 LZV0010
- Model / Scope: LZV0010-C□□□ 与 LHV

### Question

LZV0010 与 LHV 组合时，OUT1、OUT2 分别是什么？清洁检测回路应在什么状态清洁哪里？

### Standard Answer

OUT1 为 LHV 夹紧动作确认，OUT2 为释放动作确认。应定期清洁 A 端口后部、夹紧器侧的检测
回路；对 LHV 清洁时必须让夹紧器处于释放状态，再通过清洁回路排出异物。

### Scoring Standard

- P1 [20]: OUT1 为夹紧确认
- P2 [20]: OUT2 为释放确认
- P3 [20]: 定期清洁 A 端口后部检测回路
- P4 [20]: 清洁对象为夹紧器侧回路
- P5 [20]: LHV 处于释放状态

### Accepted Variants

- 释放可写为松开。

### Forbidden Errors

- 不得颠倒输出或在夹紧状态清洁 LHV 回路。

### Tolerance

- 状态和输出须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 47-48
- Printed page: 1713-1714
- Section: LZV0010 使用注意事项
- Local scope path: LZV0010 > LHV 输出与清洁回路
- Evidence type: PROCEDURE + CIRCUIT_DIAGRAM
- Evidence: 页面定义两路输出，并要求 LHV 在释放状态清洁 A 端口后部回路。

## LHV-Q-0027

**Type: FACT**

### Target

- Binding: EXACT_MODEL
- Product: KOSMEK LZH 锥面结合式毛坯压板
- Model / Scope: LHV0550 对应 LZH0550-T

### Question

LHV0550 标准锥形压板型对应的毛坯压板型号、材质、表面处理和使用前加工要求是什么？

### Standard Answer

对应 LZH0550-T；材质 S50CH，表面发黑处理。使用前按需要补充加工前端，并按 LHV0550
锥面结合式压板设计尺寸加工定位和配合部位。

### Scoring Standard

- P1 [35]: LZH0550-T
- P2 [20]: S50CH
- P3 [15]: 发黑处理
- P4 [15]: 按需补充加工前端
- P5 [15]: 按 LHV0550 设计尺寸加工定位和配合部位

### Accepted Variants

- 发黑可写为黑染处理。

### Forbidden Errors

- 不得写成 A 型毛坯 LZH0550-A 或声称可不加工直接使用。

### Tolerance

- 型号须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 21-22
- Printed page: 601-602
- Section: 压板设计尺寸/附件
- Local scope path: LHV > 锥面结合式毛坯压板 > LHV0550
- Evidence type: TABLE + DRAWING
- Evidence: 附件表将 LHV0550 对应到 LZH0550-T，并给出材质、表面和加工要求。

## LHV-Q-0028

**Type: CAUTION**

### Target

- Binding: MODEL_FAMILY
- Product: KOSMEK LHV
- Model / Scope: LHV□□□□-C□E-A 快换压板 A 型

### Question

A 型 LHV 使用偏心压板时，夹紧点必须处于什么范围？挡销兼相位调整销还有什么拆卸功能？

### Standard Answer

夹紧点必须位于以压板紧固部为基准的 90°范围内。挡销兼相位调整销在安装时用于相位调整，
拆卸时兼作挡块；若不使用该销，拆卸压板时必须另备挡块。

### Scoring Standard

- P1 [35]: 夹紧点位于压板紧固部基准 90°范围
- P2 [25]: 安装时用于相位调整
- P3 [20]: 拆卸时兼作挡块
- P4 [20]: 不用该销时须另备挡块

### Accepted Variants

- 挡销可写为相位调整销。

### Forbidden Errors

- 不得把 90°范围解释为旋转角度精度或允许任意偏心位置。

### Tolerance

- 90°范围须精确。

### Source

- PDF: LHV_R00_2023KW_C1N.pdf
- Physical page: 23, 25
- Printed page: 745, 747
- Section: 油压旋转式夹紧器注意事项
- Local scope path: LHV-A > 偏心压板与挡销
- Evidence type: CAUTION + DRAWING
- Evidence: 页面图示 90°夹紧点范围，并说明挡销的相位调整和拆卸挡块功能。
