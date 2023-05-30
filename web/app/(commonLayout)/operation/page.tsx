import { getLocaleOnServer } from '@/i18n/server'
import { useTranslation } from '@/i18n/i18next-serverside-config'

const Operation = async () => {
  const locale = getLocaleOnServer()
  const { t } = await useTranslation(locale, 'common')

  return (
    // CVTE 嵌入运营报表
    <iframe src={process.env.REPORT_URL} width='100%' height='1500' frameborder='0'></iframe>
  )
}

export default Operation
