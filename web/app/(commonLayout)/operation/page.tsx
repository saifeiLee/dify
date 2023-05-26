import s from './page.module.css'
import { getLocaleOnServer } from '@/i18n/server'
import { useTranslation } from '@/i18n/i18next-serverside-config'

const Operation = async () => {
  const locale = getLocaleOnServer()
  const { t } = await useTranslation(locale, 'common')

  return (
    // CVTE 嵌入运营报表
    <iframe src='https://grafana.cvte.com/d/ef91266f-b375-448c-9461-5ffa1bfb4884/dify-abstract?orgId=1&kiosk=full&var-channel=All&var-loan_no=&theme=light&refresh=1h' width='100%' height='1000' frameborder='0'></iframe>
  )
}

export default Operation
