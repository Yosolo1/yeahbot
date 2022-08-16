from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += ' 【 '
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='◆'
			else: make_text+='◇'
			index_make+=1
		make_text += ' 】 '
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = "📥Descargando...\n\n"
    msg += "📔Nombre "+filename+'\n\n'
    msg += "⬇️Descargado: "+sizeof_fmt(currentBits) + ' de ' + sizeof_fmt(totalBits) + '\n'
    msg += "⚡️Velocidad: "+sizeof_fmt(speed)+'/s '\n'
    msg += "⏰Tiempo restante: '+str(datetime.timedelta(seconds=int(time)))+'s '\n'
    if tid!='':
        msg+= '🚫 /cancel_' + tid
    return msg

def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = "Subiendo...\n\n"
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '📚: ' + str(filename)+'\n\n'
    else:
        msg += '📚Nombre '+filename+'\n\n'
    msg += "⬆️Subido: "+sizeof_fmt(currentBits) + ' de ' + sizeof_fmt(totalBits) + '\n'
    msg += "⚡Velocidad: "+sizeof_fmt(speed)+'/s '\n'
    msg += "⏰Tiempo restante: '+str(datetime.timedelta(seconds=int(time)))+'s '\n'
    return msg

def createCompresing(filename,filesize,splitsize):
    msg  = "🗜️Comprimiendo...\n\n"
    msg += "🗜Comprimiendo "+ str(round(int(filesize/splitsize)+1,1))+" en partes de "+str(sizeof_fmt(splitsize))+'\n\n'
    return msg

def createFinishUploading(filename,filesize,split_size,current,count,findex,username):
    msg = "✅PROCESO FINALIZADO...\n\n"
    msg += "📓Nombre "+ str(filename)+'\n\n'
    msg += "📦 ¡Han sido guardados correctamente "+str(sizeof_fmt(filesize)) + " por el usuario @"+username+"\n"
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>🔗𝐄𝐧𝐥𝐚𝐜𝐞𝐬 𝐝𝐞 𝐝𝐞𝐬𝐜𝐚𝐫𝐠𝐚:</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['name'] + '🔗</a>'
            msg+= "<a href='"+url+"'>➾"+f['name']+'</a>\n'
        msg += "\n⚡️¡Toque los enlaces para descargarlos o descargue desde los TXT!⚡️\n\n"
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '➣ Archivos ('+str(len(evfiles))+')\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = "👥 Usuario: "+str(userdata['moodle_user'])+'\n'
    msg += "🔑 Contraseña: "+str(userdata['moodle_password'])+'\n'
    msg += "☁️Página: "+ str(userdata['moodle_host'])+'\n'
    msg += "🗜Tamaño por archivo: "+ sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    proxy = '❌'
    if userdata['proxy'] !='':
       proxy = '✅'
    msg += "🔌 Proxy: " + proxy +"\n"
    msgAdmin = '❌'
    if isadmin:
        msgAdmin = '✅'
    msg+= '🦾Admin : ' + msgAdmin + '\n\n'
    
    return msg
