USE [stock]
GO

/****** Object:  Table [dbo].[daily]    Script Date: 2018/6/24 下午 05:12:48 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[daily](
	[id] [nvarchar](10) NOT NULL,
	[day] [nvarchar](8) NOT NULL,
	[vol] [decimal](18, 0) NOT NULL,
	[turnover] [decimal](18, 0) NOT NULL,
	[price_open] [decimal](6, 2) NOT NULL,
	[price_high] [decimal](6, 2) NOT NULL,
	[price_low] [decimal](6, 2) NOT NULL,
	[price_close] [decimal](6, 2) NOT NULL,
	[spread] [decimal](6, 2) NOT NULL,
	[count] [decimal](18, 2) NOT NULL,
	[memo] [nvarchar](1000) NULL,
 CONSTRAINT [PK_daily] PRIMARY KEY CLUSTERED 
(
	[id] ASC,
	[day] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'代號' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'id'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'日期' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'day'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'成交股數' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'vol'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'成交金額' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'turnover'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'開盤價' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'price_open'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'最高價' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'price_high'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'最低價' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'price_low'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'收盤價' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'price_close'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'漲跌價差' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'spread'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'成交筆數' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'count'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'NoRecord;NoCompare' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'daily', @level2type=N'COLUMN',@level2name=N'memo'
GO


