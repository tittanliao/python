USE [stock]
GO

/****** Object:  Table [dbo].[isin]    Script Date: 2018/6/19 上午 12:14:40 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[isin](
	[id] [nvarchar](10) NOT NULL,
	[name] [nvarchar](100) NOT NULL,
	[isin_code] [nvarchar](12) NULL,
	[create_day] [nvarchar](8) NULL,
	[market_type] [nvarchar](10) NULL,
	[market_type_detail] [nvarchar](100) NULL,
	[industry_type] [nvarchar](100) NULL,
	[update_time] [datetime] NULL,
	[update_user] [nvarchar](10) NULL,
 CONSTRAINT [PK_isin] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'代號' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'isin', @level2type=N'COLUMN',@level2name=N'id'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'名稱' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'isin', @level2type=N'COLUMN',@level2name=N'name'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'國際證券辨識號碼' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'isin', @level2type=N'COLUMN',@level2name=N'isin_code'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'上市日' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'isin', @level2type=N'COLUMN',@level2name=N'create_day'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'市場別' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'isin', @level2type=N'COLUMN',@level2name=N'market_type'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'市場別_細項' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'isin', @level2type=N'COLUMN',@level2name=N'market_type_detail'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'產業別' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'isin', @level2type=N'COLUMN',@level2name=N'industry_type'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'國際證券識別碼' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'isin'
GO


